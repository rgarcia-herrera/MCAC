import urllib2
from varnorm.varcharkey import VarCharKey
import json
from pprint import pprint

"""
This script uses the Reference Variant Store at https://rvs.u.hpc.mssm.edu/ to annotate loci from a bed file.
"""

def rvs_annotate( variants ):
    annotations = []
    for n in range(0,len(variants),20):
        batch = list(variants)[n:n+19]
        vkeys = []    

        for v in batch:
            (chrom,start,alt) = v
            # TODO: this grabs just snps
            vkey = VarCharKey.v2k(chrom, start, start, alt)
            vkeys.append(vkey)

        vkeysquery = ",".join(vkeys)


        for resource in [u'frequency', u'disease', u'prediction', u'impact']:
            url = 'https://rvs.u.hpc.mssm.edu/rest/%s/vkey/%s' % (resource, vkeysquery)
            results = urllib2.urlopen(
                urllib2.Request(url))
            for ann in json.loads(results.read()):
                ann[u'resource'] = resource
                annotations.append(ann)
            
            results.close()

    return annotations







# print rvs_annotate([("1",955553,"C"), ("7",140434407,"A")])
