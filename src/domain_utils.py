#collection of functions for extracting/evaluating domains

from urlparse import urlparse
import socket

def URLtoHost(url):
    """Gives just the host (an IP or domain) from a full URL"""

    host = urlparse(url).netloc
    
    port = host.find(':')
    if port != -1:
        host = host[:port]

    return host


def isIPAddress(host):
    """Returns true if it looks like an IPv4 or IPv6 address"""
    try:
        socket.inet_pton(socket.AF_INET, host)
        return True
    except:
        pass

    try:
        socket.inet_pton(socket.AF_INET6, host)
        return True
    except:
        pass

    return False
