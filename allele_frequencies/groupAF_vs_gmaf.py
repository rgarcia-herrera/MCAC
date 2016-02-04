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
            if v.ID and 'GMAF' in v.INFO and len(v.FILTER)==0:
                for gmaf in v.INFO['GMAF']:
                    if 'CSQT' in v.INFO:
                        gene_symbol = v.INFO['CSQT'][0].split('|')[0]
                    else:
                        gene_symbol = '?'
                    variant = (gene_symbol, v.CHROM, v.POS, gmaf)
                    cases[sample].add(variant)



                
union     = set.union( *cases.values() )

frequencies = {v: 0 for v in union}

for v in union:
    for sample in cases:
        if v in cases[sample]:
            frequencies[v]+=1


grouplen = len(vcf_paths)

for v in frequencies:
    print v[0],v[1],v[2],v[3].split('|')[0],v[3].split('|')[1], float(frequencies[v])/float(grouplen)


