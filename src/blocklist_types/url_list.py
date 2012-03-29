#Simple reading and writing of a list of urls
import domain_utils

def parse(blob):

    domainset = set()

    for line in blob.splitlines():
        line = line.strip()
        if line != "":
            host = domain_utils.URLtoHost(line)
            if not domain_utils.isIPAddress(host):
                domainset.add(host)

    return domainset


def write(domainlist):
    """Note: just puts http:// on the domain"""

    output = ""
    for domain in domainlist:
        output+= "http://%s/\n" % domain

    return output

