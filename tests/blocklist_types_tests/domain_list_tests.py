from nose.tools import *
import blocklist_types.domain_list


teststring = """a.example.com
b.example.com
c.example.com
"""
testlist = ['a.example.com', 'b.example.com', 'c.example.com']


def test_parse():
    blist = blocklist_types.domain_list.parse(teststring)
    assert_equal(blist, testlist)


def test_write():
    bstring = blocklist_types.domain_list.write(testlist)
    assert_equal(bstring, teststring)

