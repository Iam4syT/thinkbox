"""Offline fixture for the release-notes parser."""
from app import parse_feed
import xml.etree.ElementTree as ET

def main():
    feed = '<feed xmlns="http://www.w3.org/2005/Atom"><title>Synthetic lab</title><entry><title>Example release</title><updated>2026-01-01T00:00:00Z</updated><content>&lt;h3&gt;Feature&lt;/h3&gt;Example change</content></entry></feed>'
    result = parse_feed(feed)
    assert len(result['entries']) == 1
    assert result['entries'][0]['categories'] == ['Feature']
    try: parse_feed('broken XML')
    except ET.ParseError: pass
    else: raise AssertionError('Malformed XML must fail')
    print('PASS: one synthetic Atom entry parsed, category extracted and malformed XML rejected. No feed or Drive request.')
if __name__=='__main__':main()
