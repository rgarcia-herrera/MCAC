import vcf
import os
from pprint import pprint

from samples import vcf_paths


cases = {}
for path in vcf_paths:

    vcfr = vcf.Reader( open(path, 'r') )
    for sample in vcfr.samples:
        cases[sample] = set()
        for v in vcfr:
            if v.ID and 'GMAF' in v.INFO:
                for gmaf in v.INFO['GMAF']:
                    variant = (v.CHROM, v.POS, gmaf)
                    cases[sample].add(variant)



                
union     = set.union( *cases.values() )

frequencies = {v: 0 for v in union}

for v in union:
    for sample in cases:
        if v in cases[sample]:
            frequencies[v]+=1


pprint(frequencies)
exit(0)
