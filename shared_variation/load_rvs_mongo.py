import vcf
import os
from pprint import pprint
from samples import vcf_paths
from rvs_ann import rvs_annotate

cases = {}
for sample in vcf_paths:
    cases[sample] = set()
    vcfr = vcf.Reader( open(vcf_paths[sample], 'r') )

    for v in vcfr:
        if v.is_snp:
            variant = (v.CHROM.replace('chr',''), v.POS, str(v.ALT[0]))
            cases[sample].add(variant)

pprint( rvs_annotate([("1",955553,"C"), ("7",140434407,"A")]) )

# for sample in cases:
#     print sample
#     print rvs_annotate(cases[sample])
#     for resource in rvs_annotate(cases[sample])


