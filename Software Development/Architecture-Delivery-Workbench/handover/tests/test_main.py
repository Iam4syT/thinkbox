import json
import tempfile
import unittest
from pathlib import Path
from main import connect, dispatch

class HandoverTests(unittest.TestCase):
    def setUp(self): self.con = connect(':memory:')
    def tearDown(self): self.con.close()
    def call(self, data=None, token='demo', method='POST', path='/requests'):
        return dispatch(self.con, method, path, token, json.dumps(data if data is not None else {'request_key':'a-1','category':'mail'}).encode(), 'demo')
    def test_create(self): self.assertEqual(self.call()[0], 201)
    def test_replay_one_row(self):
        self.call();self.assertEqual(self.call()[0], 200)
        self.assertEqual(self.con.execute('SELECT count(*) FROM requests').fetchone()[0],1)
    def test_conflict(self):
        self.call();self.assertEqual(self.call({'request_key':'a-1','category':'access'})[0],409)
    def test_wrong_token_no_write(self):
        self.assertEqual(self.call(token='wrong')[0],401)
        self.assertEqual(self.con.execute('SELECT count(*) FROM requests').fetchone()[0],0)
    def test_get_requires_token(self): self.assertEqual(self.call(token='',method='GET')[0],401)
    def test_list(self):
        self.call();self.assertEqual(len(self.call(method='GET')[1]['requests']),1)
    def test_bad_json(self): self.assertEqual(dispatch(self.con,'POST','/requests','demo',b'{','demo')[0],400)
    def test_large(self): self.assertEqual(dispatch(self.con,'POST','/requests','demo',b'x'*4097,'demo')[0],413)
    def test_reject_extra_fields(self): self.assertEqual(self.call({'request_key':'x','category':'mail','name':'private'})[0],400)
    def test_reject_invalid_key(self): self.assertEqual(self.call({'request_key':"a'; DROP TABLE requests;--",'category':'mail'})[0],400)
    def test_invalid_category(self): self.assertEqual(self.call({'request_key':'x','category':'private'})[0],400)
    def test_route(self): self.assertEqual(self.call(path='/unknown')[0],404)
    def test_missing_secret(self):
        with self.assertRaises(ValueError): dispatch(self.con,'GET','/requests','',b'','')
    def test_persistence(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=str(Path(tmp)/'db.sqlite');c=connect(p)
            dispatch(c,'POST','/requests','demo',b'{"request_key":"saved","category":"other"}','demo');c.close()
            c=connect(p);self.assertEqual(c.execute('SELECT request_key FROM requests').fetchone()[0],'saved');c.close()
if __name__ == '__main__': unittest.main()
