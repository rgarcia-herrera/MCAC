import vcf

import argparse
import sys

parser = argparse.ArgumentParser(description='filtra un vcf por calidad')

parser.add_argument('--vcfin',  type=argparse.FileType('r'), required=True, help="vcf a filtrar")
parser.add_argument('--qual', type=int, default=25, help="quedarse variantes con calidad arriba de este numero, default 25")
parser.add_argument('--vcfout', type=argparse.FileType('w'), default=sys.stdout, help="vcf filtrado")

args = parser.parse_args()

variants = vcf.Reader( args.vcfin, compressed=False)

out = vcf.Writer( args.vcfout, variants)


for v in variants:
    if v.QUAL > args.qual:
        out.write_record(v)


