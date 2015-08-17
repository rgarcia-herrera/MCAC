import argparse
import json
import pymongo
from bson.objectid import ObjectId
from pprint import pformat, pprint
from os import path

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy import Column, Integer, String, Float, create_engine

from clinical_data import clinical_data
from model import *

parser = argparse.ArgumentParser(description='Load Variant Effect Prediction MongoDB docs to RDB.')
parser.add_argument('--mongo_url', default='mongodb://localhost:27017/', help="MongoDB URL, default: mongodb://localhost:27017/")
parser.add_argument('--rdb_url', default='sqlite:///consequences.sqlite', help="DB URL, default: sqlite:///consequences.sqlite")
parser.add_argument('--init', choices=['true','false'], default='false', help="create relational database and tables, default: false")
args = parser.parse_args()


##############
# Monto init #
##############
client = pymongo.MongoClient(args.mongo_url)
mcac   = client.mcac
veps   = mcac.veps


####################
# database connect #
####################
engine = create_engine(args.rdb_url)
Session = sessionmaker(bind=engine)


#############
# init rdb? #
#############
if args.init == 'true':
#    Base = declarative_base()    
    Base.metadata.create_all(engine)
session = Session()
    


cterms = {}
for v in veps.find( { '$or': [{ "transcript_consequences.polyphen_prediction" : { '$in' : ["probably_damaging",
                                                                                           "possibly_damaging"]} },
                              {  "transcript_consequences.sift_prediction"     : "deleterious"}] } ):

    for tc in v['transcript_consequences']:
        sample_filename = path.basename(v['vep_json']).split('.')
        sample          = sample_filename[0]
        pipeline        = "->".join(sample_filename[1:-2])

        if 'domains' in tc:
            domains = pformat(tc['domains'])
        else:
            domains = None
        

        if 'three_prime_UTR_variant' in tc['consequence_terms']:
            c = void_Three_prime_UTR_variant.copy()
            c.update(tc)
            c.update({'sample'            : sample,
                      'pipeline'          : pipeline,
                      'variant_id'        : v['id'],
                      'chrom'             : v['seq_region_name'],
                      'start'             : v['start'],
                      'end'               : v['end'],
                      'consequence_terms' : ";".join(tc['consequence_terms'])})            
            consequence = Three_prime_UTR_variant(**c)
            session.add(consequence)
            session.commit()
            
        if 'NMD_transcript_variant' in tc['consequence_terms']:
            c = void_NMD_transcript_variant.copy()
            
            c.update(tc)
            c.update({'sample'            : sample,
                      'pipeline'          : pipeline,
                      'variant_id'        : v['id'],
                      'chrom'             : v['seq_region_name'],
                      'start'             : v['start'],
                      'end'               : v['end'],                      
                      'consequence_terms' : ";".join(tc['consequence_terms']),
                      'domains'           : domains})            
            consequence = NMD_transcript_variant(**c)
            session.add(consequence)
            session.commit()

            
        if 'downstream_gene_variant' in tc['consequence_terms']:
            c = void_Downstream_gene_variant.copy()
            c.update(tc)
            c.update({'sample'            : sample,
                      'pipeline'          : pipeline,
                      'variant_id'        : v['id'],
                      'chrom'             : v['seq_region_name'],
                      'start'             : v['start'],
                      'end'               : v['end'],                      
                      'consequence_terms' : ";".join(tc['consequence_terms'])})
            consequence = Downstream_gene_variant(**c)
            session.add(consequence)
            session.commit()

            
        if 'intron_variant' in tc['consequence_terms']:
            c = void_Intron_variant.copy()
            c.update(tc)
            c.update({'sample'            : sample,
                      'pipeline'          : pipeline,
                      'variant_id'        : v['id'],
                      'chrom'             : v['seq_region_name'],
                      'start'             : v['start'],
                      'end'               : v['end'],                      
                      'consequence_terms' : ";".join(tc['consequence_terms'])})            
            consequence = Intron_variant(**c)
            session.add(consequence)
            session.commit()

        if 'missense_variant' in tc['consequence_terms']:
            c = void_Missense_variant.copy()
            c.update(tc)
            c.update({'sample'            : sample,
                      'pipeline'          : pipeline,
                      'variant_id'        : v['id'],
                      'chrom'             : v['seq_region_name'],
                      'start'             : v['start'],
                      'end'               : v['end'],                      
                      'consequence_terms' : ";".join(tc['consequence_terms']),
                      'domains'           : domains})
            consequence = Missense_variant(**c)
            session.add(consequence)
            session.commit()
            
        if 'non_coding_transcript_exon_variant' in tc['consequence_terms']:
            c = void_Non_coding_transcript_exon_variant.copy()
            c.update(tc)
            c.update({'sample'            : sample,
                      'pipeline'          : pipeline,
                      'variant_id'        : v['id'],
                      'chrom'             : v['seq_region_name'],
                      'start'             : v['start'],
                      'end'               : v['end'],                      
                      'consequence_terms' : ";".join(tc['consequence_terms'])})            
            consequence = Non_coding_transcript_exon_variant(**c)
            session.add(consequence)
            session.commit()

        if 'non_coding_transcript_variant' in tc['consequence_terms']:
            c = void_Non_coding_transcript_variant.copy()
            c.update(tc)
            c.update({'sample'            : sample,
                      'pipeline'          : pipeline,
                      'variant_id'        : v['id'],
                      'chrom'             : v['seq_region_name'],
                      'start'             : v['start'],
                      'end'               : v['end'],                      
                      'consequence_terms' : ";".join(tc['consequence_terms'])})            
            consequence = Non_coding_transcript_variant(**c)
            session.add(consequence)
            session.commit()

        if 'splice_region_variant' in tc['consequence_terms']:
            c = void_Splice_region_variant.copy()            
            c.update(tc)
            c.update({'sample'            : sample,
                      'pipeline'          : pipeline,
                      'variant_id'        : v['id'],
                      'chrom'             : v['seq_region_name'],
                      'start'             : v['start'],
                      'end'               : v['end'],                      
                      'consequence_terms' : ";".join(tc['consequence_terms']),
                      'domains'           : domains} )
            consequence = Splice_region_variant(**c)
            session.add(consequence)
            session.commit()

        if 'synonymous_variant' in tc['consequence_terms']:
            c = void_Three_prime_UTR_variant.copy()
            c.update(tc)
            c.update({'sample'            : sample,
                      'pipeline'          : pipeline,
                      'variant_id'        : v['id'],
                      'chrom'             : v['seq_region_name'],
                      'start'             : v['start'],
                      'end'               : v['end'],                      
                      'consequence_terms' : ";".join(tc['consequence_terms']),
                      'domains'           : domains})            
            consequence = Synonymous_variant(**c)
            session.add(consequence)
            session.commit()
        
            
        # consequence = Consequence(
        #     sample            = sample,
        #     pipeline          = pipeline,
        #     variant_id        = v['id'],
        #     chrom             = v['seq_region_name'],
        #     start             = v['start'],
        #     end               = v['end'],
        #     amino_acids       = amino_acids,
        #     biotype           = tc[u'biotype'],
        #     cdna_start        = cdna_start, 
        #     cdna_end          = cdna_end,
        #     cds_start         = cds_start,
        #     cds_end           = cds_end,
        #     codons            = codons,
        #     exon              = exon,
        #     gene_id           = tc[u'gene_id'],
        #     gene_symbol       = tc[u'gene_symbol'],
        #     hgnc_id           = tc[u'hgnc_id'],
        #     impact            = tc[u'impact'],
        #     protein_start     = protein_start,
        #     protein_end       = protein_end,
        #     protein_id        = tc[u'protein_id'],
        #     consequence_terms = ";".join(tc['consequence_terms']),
        #     transcript_id     = tc[u'transcript_id'],
        #     uniparc           = tc[u'uniparc'],
        #     variant_allele    = tc[u'variant_allele'] )
        # session.add(consequence)
        # session.commit()


