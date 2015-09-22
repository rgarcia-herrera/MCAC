import vcf
from pprint import pprint

vcfdir = '/home/rgarcia/MCAC/vcf/exm_illumina'

samples = [ 'DLA', 'GEL', 'GMCA', 'JLRL', 'JLRM', 'LMG', 'PTL', 'YRN', ]

vars = {}
for sample in samples:
    path = "%s/%s.vcf" % (vcfdir, sample)
    f = open(path, 'r')
    vars[sample] = set()
    vcfr = vcf.Reader( f )
    for v in vcfr:
        variant = "%s:%s %s/%s" % (v.CHROM, v.POS, v.REF, v.ALT)
        vars[sample].add(variant)


        
interesting = set.intersection(vars['JLRL'], vars['JLRM'], vars['GEL'])


with open( '%s/JLRM.vcf' % vcfdir, 'r' ) as inhandle, \
     open('%s/family_filtered_JLRLiJLRMiGEL_con_alelos.vcf' % vcfdir, 'w') as outhandle:
    invcf   = vcf.Reader( inhandle )
    outvcf  = vcf.Writer( outhandle, invcf )

    for v in invcf:
        variant = "%s:%s %s/%s" % (v.CHROM, v.POS, v.REF, v.ALT)
        if variant in interesting:
            outvcf.write_record(v)    




interesting = set.intersection(vars['JLRM'], vars['YRN'])


with open( '%s/JLRM.vcf' % vcfdir, 'r' ) as inhandle, \
     open('%s/family_filtered_JLRMiYRM_con_alelos.vcf' % vcfdir, 'w') as outhandle:
    invcf   = vcf.Reader( inhandle )
    outvcf  = vcf.Writer( outhandle, invcf )

    for v in invcf:
        variant = "%s:%s %s/%s" % (v.CHROM, v.POS, v.REF, v.ALT)
        if variant in interesting:
            outvcf.write_record(v)    

            
