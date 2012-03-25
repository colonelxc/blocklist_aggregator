from nose.tools import *
import blocklist_aggregator.domain_utils as domain_utils

def URLtoHost_test():

    t = domain_utils.URLtoHost('http://www.example.com/index.php')
    assert_equal(t, 'www.example.com')
    
    t = domain_utils.URLtoHost('http://www.example.com:8080/index.php')
    assert_equal(t, 'www.example.com')
    
    t = domain_utils.URLtoHost('http://192.168.0.1/index.php?a=b&c=d')
    assert_equal(t, '192.168.0.1')

def isIPAddress_test():

    assert_true(domain_utils.isIPAddress('192.168.0.1'))
    assert_true(domain_utils.isIPAddress('255.255.255.255'))
    assert_true(domain_utils.isIPAddress('0.0.0.0'))

    assert_true(domain_utils.isIPAddress('2001:0db8:85a3:0000:0000:8a2e:0370:7334'))
    assert_true(domain_utils.isIPAddress('2001:0db8:85a3:0:0:8a2e:0370:7334'))
    assert_true(domain_utils.isIPAddress('::1'))
    assert_true(domain_utils.isIPAddress('::'))
    assert_true(domain_utils.isIPAddress('::ffff:192.168.0.1'))
    
    assert_false(domain_utils.isIPAddress('www.example.com'))
    assert_false(domain_utils.isIPAddress('192.168.0.1.cn'))

