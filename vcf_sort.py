
import vcf

import argparse
import sys

parser = argparse.ArgumentParser(description='sort vcf by genomic position')

parser.add_argument('--vcfin',  type=argparse.FileType('r'), required=True, help="unsorted")
parser.add_argument('--vcfout', type=argparse.FileType('w'), default=sys.stdout, help="sorted")

args = parser.parse_args()

variants = vcf.Reader( args.vcfin, compressed=False)

out = vcf.Writer( args.vcfout, variants)

loci = {}
for v in variants:
    try:
        n = int(v.CHROM.replace('chr', ''))
        chrom = "%02d" % n        
    except:
        chrom = v.CHROM.replace('chr', '')

    loci[ (chrom, v.POS) ] = v

sloci = loci.keys()
sloci.sort()


for l in sloci:
    out.write_record(loci[l])


