import vcf
import csv
import argparse
import sys

parser = argparse.ArgumentParser(description='Convert VCF to PROVEAN format.')

parser.add_argument('--vcfin',  type=argparse.FileType('r'), required=True, help="input VCF")
parser.add_argument('--out', type=argparse.FileType('w'), default=sys.stdout, help="provean output file")

args = parser.parse_args()

variants = vcf.Reader( args.vcfin, compressed=False)
writer = csv.writer(args.out)

for v in variants:
    if v.is_snp or v.is_indel:
        chrom = v.CHROM.replace('chr','')
        alt = "".join([str(n) for n in v.ALT])
        writer.writerow([chrom, v.POS, v.REF, alt])
