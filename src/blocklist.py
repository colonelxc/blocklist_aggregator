"""
blocklist.py

Stores the values, keeps track of stats
"""

from collections import defaultdict

class Blocklist(object):
   
    def __init__(self):
        self._domains = defaultdict(list)
        self._source_totals = dict()


    def add(self, source, domain_list):

        self._source_totals[source] = len(domain_list)
        
        for domain in domain_list:
            self._domains[domain].append(source)


    def get_blocklist(self):
        return self._domains.keys()


    def stats_uniques(self):
        
        uniques = defaultdict(int)

        for domain, sources in self._domains.iteritems():
            if len(sources) == 1:
                uniques[sources[0]] += 1

        return uniques


    def stats_totals(self):
        return self._source_totals

