import argparse
import json
import pymongo
from bson.objectid import ObjectId
from pprint import pprint
from os import path
from clinical_data import clinical_data

parser = argparse.ArgumentParser(description='Load Variant Effect Prediction JSON file to MongoDB.')
parser.add_argument('--url', default='mongodb://localhost:27017/', help="MongoDB URL, default: mongodb://localhost:27017/")
#parser.add_argument('--veps', type=argparse.FileType('r'), nargs="+", required=True, help='one or more VEP JSON files')
args = parser.parse_args()



client = pymongo.MongoClient(args.url)
mcac   = client.mcac
veps   = mcac.veps



for v in veps.find( { '$or': [{ "transcript_consequences.polyphen_prediction" : "probably_damaging" },
                              {  "transcript_consequences.sift_prediction"     : "deleterious"}] } ):

    for tc in v['transcript_consequences']:
        if 'missense_variant' in tc['consequence_terms']:

            sample_filename = path.basename(v['vep_json']).split('.')
            sample          = sample_filename[0]
            pipeline        = "->".join(sample_filename[1:-2])
            
            print [
                sample,
                pipeline,
                v['id'],
                v['seq_region_name'],
                v['start'],
                v['end'],
                tc['amino_acids'],
                tc[u'biotype'],
                tc[u'cdna_end'],
                tc[u'cdna_start'],
                tc[u'cds_end'],
                tc[u'cds_start'],
                tc[u'codons'],
                tc[u'eas_maf'],
                tc[u'exon'],
                tc[u'gene_id'],
                tc[u'gene_symbol'],
                tc[u'hgnc_id'],
                tc[u'impact'],
                tc[u'protein_start'],
                tc[u'protein_end'],
                tc[u'protein_id'],
                tc[u'sas_maf'],
                ";".join(tc['consequence_terms']),
                tc[u'transcript_id'],
                tc[u'uniparc'],
                tc[u'variant_allele'],
            ]

