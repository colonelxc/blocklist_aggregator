# Parses the phishtank.com csv format
# See: https://www.phishtank.com/developer_info.php

import csv
import cStringIO

import domain_utils

def parse(data):

    csvdata = csv.DictReader(cStringIO.StringIO(data))
    
    domainset = set()
    for row in csvdata:
        url = row['url']
        host = domain_utils.URLtoHost(url)
        if not domain_utils.isIPAddress(host):
            domainset.add(host)

    return domainset



