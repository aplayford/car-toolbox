#!/usr/bin/env python

# A simple tool to take a .csv containing address data and to generate a set of "cleaned" addresses that can be used for joins.

#
# To-do:
# 1) Think about: How to clean up 3rd so it will also match third? What about 4th Street versus 4 Street? Can we write one-off code to handle?
# 2) The leave_spaces flag in strip_term() is broken. (\W matches a space regardless.)

import re
import sys
import csv
from repl.addr import replDict

def strip_term(stripstr):
    strip_pattern = re.compile('[\W]+')
    return strip_pattern.sub('', stripstr)
    
def clean_addy(str):
    terms = str.split(' ')
    
    terms = [strip_term(term).upper() for term in terms]
    terms = [replDict.get(term, term) for term in terms]
    terms.sort()
    
    return " ".join(terms)

def get_addy_start(v):
    ltrs = [l for l in strip_term(v.split(' ')[0])]
    res = ""
    while len(ltrs) and ltrs[0].isdigit():
        res += ltrs.pop(0)
    return res

def get_addy_numbers(v):
    return "".join([l for l in v if l.isdigit()])

def go():
    if not len(sys.argv) in (3, 5):
        print("ADDRESS CLEANER")
        print("===============")
        print("Call me like this:\n\taddresscleaner.py infile outfile [fieldname idname]")
        return

    if len(sys.argv) == 5:
        (me, infile, outfile, fieldname, idname) = sys.argv

    else:
        (me, infile, outfile) = sys.argv
        fieldname = "Address Text"
        idname = "Address ID"
    
    inf = open(infile, 'rU')
    res = csv.DictReader(inf)
    
    with open(outfile, 'wb') as out:
        writer = csv.writer(out)
        writer.writerow(["Row ID", "Original Address", "Clean Address", "Address Start"])

        for row in res:
            t = row[fieldname]
            writer.writerow([row[idname], t, clean_addy(t), get_addy_start(t)])
    
    inf.close()

    print("ADDRESS CLEANER")
    print("===============")
    print("I read everything from %s, cleaned up the addresses and wrote them into %s." % (infile, outfile))

if __name__=="__main__":
    go()
