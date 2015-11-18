import vcf
from pprint import pprint

vcfdir = '/home/rgarcia/MCAC/vcf'

samples = [ 'caem_fvi_rigo/S08','exm_illumina/LMG' ]

vars = {}
for sample in samples:
    path = "%s/%s.vcf" % (vcfdir, sample)
    f = open(path, 'r')
    vars[sample] = set()
    vcfr = vcf.Reader( f )
    for v in vcfr:
        variant = "%s:%s %s/%s" % (v.CHROM, v.POS, v.REF, v.ALT)
        vars[sample].add(variant)

        
interesting = set.intersection(vars['caem_fvi_rigo/S08'], vars['exm_illumina/LMG'])


with open( '%s/caem_fvi_rigo/S01.vcf' % vcfdir, 'r' ) as inhandle, \
     open('%s/family_filtered_8iLMG.vcf' % vcfdir, 'w') as outhandle:
    invcf   = vcf.Reader( inhandle )
    outvcf  = vcf.Writer( outhandle, invcf )

    for v in invcf:
        variant = "%s:%s %s/%s" % (v.CHROM, v.POS, v.REF, v.ALT)
        if variant in interesting:
            outvcf.write_record(v)    

