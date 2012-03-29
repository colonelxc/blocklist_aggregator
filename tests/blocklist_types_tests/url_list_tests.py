from nose.tools import *
import blocklist_types.url_list


teststring = """http://a.example.com
http://b.example.com/
http://c.example.com/bad.exe
http://c.example.com/index.html
http://192.168.0.1/index.html
"""
testlist = ['a.example.com', 'b.example.com', 'c.example.com']

outputstring = """http://a.example.com/
http://b.example.com/
http://c.example.com/
"""


def test_parse():
    blist = sorted(list(blocklist_types.url_list.parse(teststring)))
    assert_equal(blist, testlist)


def test_write():
    bstring = blocklist_types.url_list.write(testlist)
    assert_equal(bstring, outputstring)

