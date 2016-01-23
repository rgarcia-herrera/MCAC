import vcf
import os
from pprint import pprint
from samples import vcf_paths
from rvs_ann import rvs_annotate

variants = {}
for sample in vcf_paths:
    variants[sample] = set()
    vcfr = vcf.Reader( open(vcf_paths[sample], 'r') )

    for v in vcfr:
        if v.is_snp:
            variant = (v.CHROM.replace('chr',''), v.POS, str(v.ALT[0]))
            variants[sample].add(variant)


for sample in variants:
    for v in rvs_annotate(variants[sample]):
        v['sample'] = sample
        # load to mongo



