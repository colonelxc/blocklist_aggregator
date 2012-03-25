from nose.tools import *
import blocklist_aggregator.blocklist_types.phishtank_csv as phishtank

def parse_test():

    with open('tests/examples/phishtank-example.csv') as f:
        data = f.read()
        domains = phishtank.parse(data)

        assert_equal(sorted(list(domains)), ['other.example.com', 'www.example.com'])


