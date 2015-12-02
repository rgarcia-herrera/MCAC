import vcf
from pprint import pprint


files_cases = [
    '/home/rgarcia/MCAC/vcf/complete/B01.PTL.vcf',
    '/home/rgarcia/MCAC/vcf/complete/A01.JATE.vcf',
]




cases = {}
for path in files_cases:
    f = open(path, 'r')
    cases[f.name] = set()
    vcfr = vcf.Reader( f )
    for v in vcfr:
        variant = "%s:%s %s/%s" % (v.CHROM, v.POS, v.REF, v.ALT)
        cases[f.name].add(variant)

       
case_intersection = set.intersection( *cases.values() )
interesting       = case_intersection


inhandle = open( '/home/rgarcia/MCAC/vcf/complete/B01.PTL.vcf', 'r' )
invcf   = vcf.Reader( inhandle )
outhandle = open('/home/rgarcia/MCAC/vcf/complete/family_filtered_PTLiJATE.vcf', 'w')
outvcf  = vcf.Writer( outhandle, invcf )

for v in invcf:
    variant = "%s:%s %s/%s" % (v.CHROM, v.POS, v.REF, v.ALT)
    if variant in interesting:
        outvcf.write_record(v)    

inhandle.close()
outhandle.close()

