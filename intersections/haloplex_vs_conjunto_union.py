import vcf
from pprint import pprint


files_cases = [
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/11_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/12_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/13_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/14_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/15_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/16_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/17_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/18_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/19_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/20_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/21_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/22_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/23_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/24_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/25_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/26_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/27_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/28_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/29_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/30_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/31_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/32_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/33_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/34_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/35_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/36_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/37_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/38_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/39_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/40_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/41_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/42_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/43_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/44_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/45_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/46_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/47_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/48_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/CFOG_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/CYDR_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/EEPO_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/FJGA_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/IXH_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/JCVM_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/JDJM_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/JOS_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/JSMC_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/MJG_S1.vcf',
    '/home/rgarcia/MCAC/vcf/haloplex500basespace/RRR_S1.vcf',    
]

cases = {}
for path in files_cases:
    f = open(path, 'r')
    cases[f.name] = set()
    vcfr = vcf.Reader( f )
    for v in vcfr:
        variant = "%s:%s" % (v.CHROM, v.POS)
        cases[f.name].add(variant)

union     = set.union( *cases.values() )

print [sample for sample in cases]
for v in union:
    found = [v,]
    for sample in cases:
        if v in cases[sample]:
            found.append(1)
        else:
            found.append(0)
    print found
