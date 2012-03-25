from nose.tools import *
import blocklist_types.phishtank_csv

def parse_test():

    with open('tests/examples/phishtank-example.csv') as f:
        data = f.read()
        domains = blocklist_types.phishtank_csv.parse(data)

        assert_equal(sorted(list(domains)), ['other.example.com', 'www.example.com'])


