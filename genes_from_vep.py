import csv
import argparse

from pprint import pprint

parser = argparse.ArgumentParser(description='filter vep')
parser.add_argument('--inputs', type=argparse.FileType('r'), nargs="+", required=True )
args   = parser.parse_args()

genes = set()

for f in args.inputs:
    csvr = csv.reader( f, delimiter='\t' )
    for l in csvr:
        if not l[0].startswith('#'):
            (Uploaded_variation, Location, Allele, Gene, Feature, Feature_type, Consequence, cDNA_position, CDS_position, Protein_position, Amino_acids, Codons, Existing_variation, Extra) = l
            extraslist = Extra.split(';')
            extras = {'SYMBOL'  : '-', }
            for e in extraslist:
                (k,v) = e.split('=')
                extras[k] = v

            genes.add(extras['SYMBOL'])



for g in genes:
    print g

