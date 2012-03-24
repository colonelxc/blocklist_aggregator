#Simple reading and writing of a list of domains

def parse(blob):

    blist = []

    for line in blob.splitlines():
        line = line.strip()
        if line != "":
            blist.append(line)

    return blist


def write(domainlist):
    output = ""
    for domain in domainlist:
        output+= "%s\n" % domain

    return output

