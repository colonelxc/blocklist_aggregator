#! /usr/bin/env python

import argparse
import sys
import os
import ConfigParser
import urllib2
from urlparse import urlparse

import blocklist
import blocklist_types.hosts
import blocklist_types.domain_list
import blocklist_types.url_list
import blocklist_types.phishtank_csv

version = 0.1

def get_source(source):

    source = os.path.expanduser(source)

    try:
        with open(source, 'r') as f:
            data = f.read()
    except IOError, e:
        print >> sys.stderr, "Failed to read file %s" % source
        data = ""

    return data 

def main():

    args = process_args()


    configparser = ConfigParser.SafeConfigParser()
    configparser.readfp(args.config)

    blist = blocklist.Blocklist()

    if configparser.has_section("hosts"):
        for source,location in configparser.items("hosts"):
            data = get_source(location)
            blist.add(source, blocklist_types.hosts.parse(data)) 

    if configparser.has_section("domain_list"):
        for source,location in configparser.items("domain_list"):
            data = get_source(location)
            blist.add(source, blocklist_types.domain_list.parse(data))

    if configparser.has_section("url_list"):
        for source,location in configparser.items("url_list"):
            data = get_source(location)
            blist.add(source, blocklist_types.url_list.parse(data))

    if configparser.has_section("phishtank_csv"):
        for source, location in configparser.items("phishtank_csv"):
            data = get_source(location)
            blist.add(source, blocklist_types.phishtank_csv.parse(data))

    output(configparser, sorted(blist.get_blocklist()))


    #TODO: have a command line option to print out stats, and make them pretty
    print "uniques: " + str(blist.stats_uniques())
    print "totals: " + str(blist.stats_totals())


def output(config, datalist):

    outputfp = sys.stdout
    outputformat = "hosts"

    if config.has_section("output"):
        try:
            outputfile = os.path.expanduser(config.get("output", "file"))
            fp = open(outputfile, 'w')
            outputfp = fp
        except ConfigParser.NoOptionError:
            pass
        except IOError:
            print >> sys.stderr, "Could not write to file %s" % outputfile 
            return

        try:
            outputformat = config.get("output", "format")
        except ConfigParser.NoOptionError:
            pass

    #TODO: generate this somewhere
    header = "Hosts file, generated... recently\nSecond line of header"

    if outputformat == "hosts":
        output = blocklist_types.hosts.write(header, datalist, "127.0.0.1")

    outputfp.write(output)
    outputfp.close()


def process_args():
    global version

    parser = argparse.ArgumentParser(description='Aggregate blocklists from multiple sources', prog='blocklist_aggregator')

    parser.add_argument('--version', action='version', version="%(prog)s " + str(version))


    parser.add_argument('-c', '--config', type=argparse.FileType('rb'), required=True)

    return parser.parse_args()



if __name__ == '__main__':
    sys.exit(main())
