# Parses the phishtank.com xml format
# See: https://www.phishtank.com/developer_info.php

from lxml import etree
from urlparse import urlparse
from StringIO import StringIO

def parse(data):
    dataio = StringIO(data)

    blockset = set()

    for event, element in etree.iterparse(dataio):
        if element.tag == "url":
            host = urlparse(element.text).netloc

            port_idx = host.find(':')
            if port_idx != -1:
                host = host[:port_idx]
                
            #TODO: verify host isn't an ip address
            blockset.add(host)

    return blockset



