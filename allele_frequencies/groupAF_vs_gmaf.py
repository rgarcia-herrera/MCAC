import csv
import os
from pprint import pprint

from samples import vep_paths


cases = {}
for path in vep_paths:
    with open(path) as f:
        csvr = csv.reader(f, delimiter='\t')
        sample = os.path.basename(path)
        cases[sample] = set()
        for v in csvr:
            if not v[0].startswith('#'):

                extraslist = v[13].split(';')
                extras = {}
                for e in extraslist:
                    (key,value) = e.split('=')
                    extras[key] = value

                if 'GMAF' in extras:
                    rsids = v[12]
                    gmafs = extras['GMAF'].split(',')
                    for gmaf in gmafs:
                        variant = (extras.get('SYMBOL','-'), rsids, v[1], gmaf)
                        cases[sample].add(variant)


union     = set.union( *cases.values() )

frequencies = {v: 0 for v in union}

for v in union:
    for sample in cases:
        if v in cases[sample]:
            frequencies[v]+=1

grouplen = len(vep_paths)

print "symbol","location","gmaf","groupaf"
print "rsid", "pos", "gmaf", "groupaf"
for v in frequencies:
    # if len(v[2].split(':')) > 2:
    #     print v
    #     print v[2].split(',')
    groupaf = float(frequencies[v])/float(grouplen*2)
    (alt,gmaf) = v[3].split(':')
    print v[0],v[1],v[2],alt,gmaf,groupaf

