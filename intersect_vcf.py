import vcf
import argparse

from pprint import pprint

parser = argparse.ArgumentParser(description='Generate a VCF with the intersection of the variants of input VCFs')
parser.add_argument('--vcfs', type=argparse.FileType('r'), nargs='+', required=True )
args   = parser.parse_args()


file_names = []
variants = {}
for f in args.vcfs:
    file_names.append(f.name)
    vcfr = vcf.Reader( f )
    for v in vcfr:
        variant = "%s:%s %s/%s" % (v.CHROM, v.POS, v.REF, v.ALT)
        if f.name in variants:
            variants[f.name].update([variant])
        else:
            variants[f.name] = set([variant])


    
intersection = set.intersection( *variants.values() )

print len(intersection)

for path in file_names:
    inhandle = open( path, 'r' )
    invcf   = vcf.Reader( inhandle )
    outname = path.replace('.vcf', '.intersected.vcf')
    outhandle = open(outname, 'w')
    outvcf  = vcf.Writer( outhandle, invcf )

    for v in invcf:
        variant = "%s:%s %s/%s" % (v.CHROM, v.POS, v.REF, v.ALT)
        if variant in intersection:
            outvcf.write_record(v)    

    inhandle.close()
    outhandle.close()
