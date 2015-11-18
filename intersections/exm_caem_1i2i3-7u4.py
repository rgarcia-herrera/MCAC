import vcf
from pprint import pprint

vcfdir = '/home/rgarcia/MCAC/vcf/caem_fvi_rigo'

samples = [ 'S01','S02','S03','S04','S07' ]

vars = {}
for sample in samples:
    path = "%s/%s.vcf" % (vcfdir, sample)
    f = open(path, 'r')
    vars[sample] = set()
    vcfr = vcf.Reader( f )
    for v in vcfr:
        variant = "%s:%s %s/%s" % (v.CHROM, v.POS, v.REF, v.ALT)
        vars[sample].add(variant)

        
interesting = set.intersection(vars['S01'], vars['S02'], vars['S03']) - set.union(vars['S07'], vars['S04'])


with open( '%s/S01.vcf' % vcfdir, 'r' ) as inhandle, \
     open('%s/family_filtered_1i2i3-7u4.vcf' % vcfdir, 'w') as outhandle:
    invcf   = vcf.Reader( inhandle )
    outvcf  = vcf.Writer( outhandle, invcf )

    for v in invcf:
        variant = "%s:%s %s/%s" % (v.CHROM, v.POS, v.REF, v.ALT)
        if variant in interesting:
            outvcf.write_record(v)    

