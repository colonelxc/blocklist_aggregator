from nose.tools import *
import blocklist_types.hosts

before_string = """
123.123.123.123     a.example.com
# hosts file comment, should be ignored
234.234.234.234     b.example.com # more comments
1.1.1.1             example.com otherexample.com #multiple domains per line
"""
test_list = ['a.example.com', 'b.example.com', 'example.com', 'otherexample.com']

def test_parse():
    
    blist = blocklist_types.hosts.parse(before_string)
    assert_equal(sorted(test_list), sorted(blist))


def test_write():

    header = "abc\n123"
    after_string = """# abc
# 123

127.0.0.1\ta.example.com
127.0.0.1\tb.example.com
127.0.0.1\texample.com
127.0.0.1\totherexample.com
"""

    output = blocklist_types.hosts.write(header, test_list, "127.0.0.1")
    assert_equal(after_string, output)

