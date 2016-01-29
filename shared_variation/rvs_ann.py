import urllib2
from varnorm.varcharkey import VarCharKey
import json
from pprint import pprint

"""
This script uses the Reference Variant Store at https://rvs.u.hpc.mssm.edu/ to annotate loci from a bed file.
"""



def rvs_annotate( vkeys, resource ):
    vkeysquery = ",".join(vkeys)
    url = 'https://rvs.u.hpc.mssm.edu/rest/%s/vkey/%s' % (resource, vkeysquery)
    print url
    results = urllib2.urlopen(
        urllib2.Request(url))

    found_vkeys = []
    annotations = []
    for ann in json.loads(results.read()):
        ann[u'resource'] = resource
        annotations.append(ann)
        found_vkeys.append(ann['vkey'])
    results.close()

    for unannotated in set(vkeys)-set(found_vkeys):
        annotations.append({u'resource': resource,
                            u'vkey'    : unannotated})
    
    return annotations

