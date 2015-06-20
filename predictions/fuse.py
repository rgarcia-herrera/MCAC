import argparse
import csv
import pymongo
from bson.objectid import ObjectId
from pprint import pprint

parser = argparse.ArgumentParser(description='Load variant effect prediction file to variants table.')
parser.add_argument('--type', required=True, choices=['provean','vep'])
parser.add_argument('--sample', required=True)
parser.add_argument('--file', type=argparse.FileType('r'))
args = parser.parse_args()

client = pymongo.MongoClient("notron", 27017)
db = client.mcac

if args.type == 'provean':
    bulk = db.mcac.initialize_ordered_bulk_op() 
    provean_file = csv.reader(args.file, delimiter="\t")
    for row in provean_file:
            
        (ROW_NO, INPUT, PROTEIN_ID,
         LENGTH, STRAND, CODON_CHANGE,
         POS, RESIDUE_REF, RESIDUE_ALT,
         TYPE, SCORE, PREDICTION2_5,
         SEQ1, CLUSTER, SCORE, PREDICTION0_05,
         MEDIAN_INFO, SEQ2, dbSNP_ID, GENE_ID,
         GENE_NAME, TRANSCRIPT_ID, TRANSCRIPT_STATUS,
         DESCRIPTION, GC_CONTENT, CHR_BAND, FAMILY_ID,
         FAMILY_DESC, UNIPROT_ID, REFSEQ_PROTEIN_ID,
         MIM_ACCESSION, PFAM_ID, TIGRFAM_ID, INTERPRO_ID,
         GO_TERM_ACCESSION, GO_SLIM_GOA_ACCESSION) = row

        if ROW_NO.startswith('#'):
            continue

        if PROTEIN_ID == 'record not found':
            continue
            
        (chrom, pos, ref, alt) = INPUT.split(',')

        v = { 'chrom': chrom, 'pos': pos, 'ref': ref, 'alt': alt,
              'protein_id'    : PROTEIN_ID,
              'gene_id'       : GENE_ID,
              'transcript_id' : TRANSCRIPT_ID,
              'provean_prediction_1': PREDICTION2_5,
              'provean_prediction_2': PREDICTION0_05,
              'sample'          : args.sample,
              #'provean_rows'    : []
        }

        bulk.find( { 'chrom': chrom, 'pos': pos, 'ref': ref, 'alt': alt,
                     'protein_id'    : PROTEIN_ID,
                     'gene_id'       : GENE_ID,
                     'transcript_id' : TRANSCRIPT_ID, }
        ).upsert().update( {'$set': v, '$push': {'provean_rows': row}} )
            
    result = bulk.execute()
        
    pprint(result)
    
if args.type == 'vep':
    pass
