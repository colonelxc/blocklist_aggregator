from nose.tools import *
import blocklist


def test_basic():
    b = blocklist.Blocklist()
    l = ['a.example.com', 'b.example.com']
    b.add('source', l)

    assert_equal(sorted(l), sorted(b.get_blocklist()))


def test_overlap():
    b = blocklist.Blocklist()
    b.add('source1', ['a.com', 'b.com'])
    b.add('source2', ['a.com', 'c.com'])

    bl = b.get_blocklist()
    assert_equal(sorted(bl), ['a.com', 'b.com', 'c.com'])

def test_whitelist():
    b = blocklist.Blocklist()
    b.add('source1', ['a.com', 'b.com'])

    b.add_whitelist(['a.com'])
    bl = b.get_blocklist()
    assert_equal(bl, ['b.com'])

def test_stats():
    b = blocklist.Blocklist()
    b.add('source1', ['a.com', 'b.com'])
    b.add('source2', ['a.com', 'c.com'])

    uniques = b.stats_uniques()
    totals = b.stats_totals()

    assert_equal(uniques['source1'], 1)
    assert_equal(uniques['source2'], 1)
    assert_equal(totals['source1'], 2)
    assert_equal(totals['source2'], 2)

