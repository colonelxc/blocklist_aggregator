#parses and writes hosts files


def parse(blob):

    blist = []

    for line in blob.splitlines():
        comment = line.find('#')
        if comment != -1:
            line = line[:comment]

        parts = line.split()
        blist.extend(parts[1:])

    return blist

def write(header, domainlist, ip):

    output = ""
    headerlines = header.splitlines(1)
    for line in headerlines:
        output += '#' + line

    output += '\n\n'

    for domain in domainlist:
        output += "%s\t%s\n" % (ip, domain)

    return output

