import vcf
from pprint import pprint


files_cases = [
    '/home/rgarcia/MCAC/vcf/complete/B01.PTL.vcf',
    '/home/rgarcia/MCAC/vcf/complete/A01.JATE.vcf',
]


files_controls = [
    '/home/rgarcia/MCAC/vcf/complete/C01.JPAM.vcf',
    '/home/rgarcia/MCAC/vcf/complete/D01.LACA.vcf',
]




cases = {}
for path in files_cases:
    f = open(path, 'r')
    cases[f.name] = set()
    vcfr = vcf.Reader( f )
    for v in vcfr:
        variant = "%s:%s %s/%s" % (v.CHROM, v.POS, v.REF, v.ALT)
        cases[f.name].add(variant)


        
controls = {}
for path in files_controls:
    f = open(path, 'r')    
    controls[f.name] = set()
    vcfr = vcf.Reader( f )
    for v in vcfr:
        variant = "%s:%s %s/%s" % (v.CHROM, v.POS, v.REF, v.ALT)
        controls[f.name].add(variant)


       
case_intersection = set.intersection( *cases.values() )
control_union     = set.union( *controls.values() )

interesting       = case_intersection - control_union



inhandle = open( '/home/rgarcia/MCAC/vcf/complete/B01.PTL.vcf', 'r' )
invcf   = vcf.Reader( inhandle )
outhandle = open('/home/rgarcia/MCAC/vcf/complete/family_filtered_PTLiJATE-JPAMuLACA_con_alelos.vcf', 'w')
outvcf  = vcf.Writer( outhandle, invcf )

for v in invcf:
    variant = "%s:%s %s/%s" % (v.CHROM, v.POS, v.REF, v.ALT)
    if variant in interesting:
        outvcf.write_record(v)    

inhandle.close()
outhandle.close()

