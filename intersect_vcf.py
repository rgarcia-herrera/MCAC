import vcf
import argparse

from pprint import pprint

parser = argparse.ArgumentParser(description='Generate a VCF with the intersection of the variants of input VCFs')
parser.add_argument('--vcfs', type=argparse.FileType('r'), nargs='+', required=True )
parser.add_argument('--intersection_vcf', type=argparse.FileType('w'), required=True )
args   = parser.parse_args()


variants = {}
for f in args.vcfs:
    vcfr = vcf.Reader( f )
    for v in vcfr:
        variant = "%s:%s %s" % (v.CHROM, v.POS, v.ALT)
        if f.name in variants:
            variants[f.name].update([variant])
        else:
            variants[f.name] = set([variant])


    
candidates = set.intersection( *variants.values() )



candidatos_vcf = vcf.Writer( args.interction_vcf, f )

# for v in exmvcf:
#     key = "%s:%s" % (v.CHROM, v.POS)
#     if key in candidatos:
#         candidatos_vcf.write_record(v)


    
# exmvcf = vcf.Reader( open( 'e1_SNP.vcf', 'r' ) )
# candidatos_vcf = vcf.Writer( open('candidatos_e1.vcf', 'w'), exmvcf )

# for v in exmvcf:
#     key = "%s:%s" % (v.CHROM, v.POS)
#     if key in candidatos:
#         candidatos_vcf.write_record(v)
                                                                        
