#!/usr/bin/env python

# A simple tool to take a .csv containing name data and to generate a set of "cleaned" names that can be used for joins.

import sys
import csv
from nameparser import HumanName

def go():
    if not len(sys.argv) in (3, 5):
        print("NAME CLEANER")
        print("===============")
        print("Call me like this:\n\tclean_names.py infile outfile [fieldname idname]")
        return

    if len(sys.argv) == 5:
        (me, infile, outfile, fieldname, idname) = sys.argv

    else:
        (me, infile, outfile) = sys.argv
        fieldname = "Name"
        idname = "ID"
    
    inf = open(infile, 'rU')
    res = csv.DictReader(inf)
    
    with open(outfile, 'wb') as out:
        writer = csv.writer(out)
        writer.writerow(["row_id", "name", "last_name", "first_name", "middle_name", "name_suffix"])

        for row in res:
            t = row[fieldname]
            hn = HumanName(t)
            writer.writerow([row[idname], t, hn.last, hn.first, hn.middle, hn.suffix])
    
    inf.close()

    print("NAME CLEANER")
    print("===============")
    print("I read everything from %s, cleaned up the names and wrote them into %s." % (infile, outfile))

if __name__=="__main__":
    go()
