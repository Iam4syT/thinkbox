"""Loopback training API. Not a production web server or identity system."""
import argparse
import hmac
import json
import os
import re
import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer

def connect(path):
    con = sqlite3.connect(path)
    con.execute('CREATE TABLE IF NOT EXISTS requests (request_key TEXT PRIMARY KEY, category TEXT NOT NULL)')
    return con

def dispatch(con, method, path, token, body, secret):
    if not secret:
        raise ValueError('A lab token must be configured')
    if not hmac.compare_digest(str(token), str(secret)):
        return 401, {'error': 'unauthorised'}
    if method == 'GET' and path == '/requests':
        return 200, {'requests': [dict(request_key=r[0], category=r[1]) for r in con.execute('SELECT request_key, category FROM requests ORDER BY request_key')]}
    if method != 'POST' or path != '/requests':
        return 404, {'error': 'not found'}
    if len(body) > 4096:
        return 413, {'error': 'request too large'}
    try:
        data = json.loads(body)
    except (ValueError, UnicodeError):
        return 400, {'error': 'invalid JSON'}
    if not isinstance(data, dict) or set(data) != {'request_key', 'category'}:
        return 400, {'error': 'expected request_key and category only'}
    key, category = data['request_key'], data['category']
    if not isinstance(key, str) or not re.fullmatch(r'[A-Za-z0-9-]{1,40}', key) or category not in ('access', 'mail', 'other'):
        return 400, {'error': 'invalid key or category'}
    with con:
        existing = con.execute('SELECT category FROM requests WHERE request_key = ?', (key,)).fetchone()
        if existing:
            if existing[0] != category:
                return 409, {'error': 'key already used for different content'}
            return 200, {'request_key': key, 'category': category, 'replayed': True}
        con.execute('INSERT INTO requests VALUES (?, ?)', (key, category))
    return 201, {'request_key': key, 'category': category, 'replayed': False}

def serve(db_path, secret, port):
    if not secret:
        raise ValueError('Set HANDOVER_TOKEN before starting the local API')
    class Handler(BaseHTTPRequestHandler):
        def handle_request(self):
            try:
                length = int(self.headers.get('Content-Length', '0'))
            except ValueError:
                length = -1
            if length < 0 or length > 4096:
                status, payload = 413, {'error': 'invalid or excessive length'}
            elif self.command == 'POST' and self.headers.get('Content-Type', '').split(';')[0] != 'application/json':
                status, payload = 415, {'error': 'use application/json'}
            else:
                body = self.rfile.read(length)
                con = connect(db_path)
                try:
                    status, payload = dispatch(con, self.command, self.path, self.headers.get('X-Lab-Token', ''), body, secret)
                finally:
                    con.close()
            encoded = json.dumps(payload).encode()
            self.send_response(status)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(encoded)))
            self.end_headers()
            self.wfile.write(encoded)
        do_GET = handle_request
        do_POST = handle_request
        def log_message(self, *args):
            pass  # Do not echo tokens, request content or synthetic identifiers.
    server = HTTPServer(('127.0.0.1', port), Handler)
    print(f'Lab only: http://127.0.0.1:{server.server_port}/requests', flush=True)
    try:
        server.serve_forever()
    finally:
        server.server_close()

def demo():
    con = connect(':memory:')
    body = b'{"request_key":"demo-1","category":"access"}'
    for token in ('wrong', 'local-demo', 'local-demo'):
        status, result = dispatch(con, 'POST', '/requests', token, body, 'local-demo')
        print(status, json.dumps(result))
    print(dispatch(con, 'GET', '/requests', 'local-demo', b'', 'local-demo')[0])
    con.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['demo', 'serve'])
    parser.add_argument('--db', default='lab.sqlite')
    parser.add_argument('--port', type=int, default=8765)
    args = parser.parse_args()
    if args.mode == 'demo': demo()
    else: serve(args.db, os.environ.get('HANDOVER_TOKEN'), args.port)
