import vcf
from pprint import pprint

vcfdir = '/home/rgarcia/MCAC/vcf/caem_fvi_rigo'

samples = [ 'S08','S11' ]

vars = {}
for sample in samples:
    path = "%s/%s.vcf" % (vcfdir, sample)
    f = open(path, 'r')
    vars[sample] = set()
    vcfr = vcf.Reader( f )
    for v in vcfr:
        variant = "%s:%s %s/%s" % (v.CHROM, v.POS, v.REF, v.ALT)
        vars[sample].add(variant)

        
interesting = set.intersection(vars['S08'], vars['S11'])


with open( '%s/S01.vcf' % vcfdir, 'r' ) as inhandle, \
     open('%s/family_filtered_8i11.vcf' % vcfdir, 'w') as outhandle:
    invcf   = vcf.Reader( inhandle )
    outvcf  = vcf.Writer( outhandle, invcf )

    for v in invcf:
        variant = "%s:%s %s/%s" % (v.CHROM, v.POS, v.REF, v.ALT)
        if variant in interesting:
            outvcf.write_record(v)    

