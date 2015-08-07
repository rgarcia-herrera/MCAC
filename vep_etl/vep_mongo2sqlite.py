import argparse
import json
import pymongo
from bson.objectid import ObjectId
from pprint import pprint
from os import path

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy import Column, Integer, String, Float, create_engine

from clinical_data import clinical_data

parser = argparse.ArgumentParser(description='Load Variant Effect Prediction MongoDB docs to RDB.')
parser.add_argument('--mongo_url', default='mongodb://localhost:27017/', help="MongoDB URL, default: mongodb://localhost:27017/")
parser.add_argument('--rdb_url', default='sqlite:///missense.sqlite', help="DB URL, default: sqlite:///missense.sqlite")
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


##################
# DataBase Model #
##################
Base = declarative_base()
class Consequence(Base):
    __tablename__ = 'consequences'
    id                = Column(Integer, primary_key=True)
    sample            = Column(String)
    pipeline          = Column(String) 
    variant_id        = Column(String)
    chrom             = Column(String) # v['seq_region_name'],
    start             = Column(Integer) 
    end               = Column(Integer)
    amino_acids       = Column(String)
    biotype           = Column(String)
    cdna_start        = Column(Integer)    
    cdna_end          = Column(Integer)
    cds_start         = Column(Integer)        
    cds_end           = Column(Integer)
    codons            = Column(String)
    exon              = Column(String)
    gene_id           = Column(String)
    gene_symbol       = Column(String)
    hgnc_id           = Column(String)
    impact            = Column(String)
    protein_start     = Column(Integer)
    protein_end       = Column(Integer)
    sas_maf           = Column(String)
    protein_id        = Column(String)
    consequence_terms = Column(String)
    transcript_id     = Column(String)
    uniparc           = Column(String)
    variant_allele    = Column(String)
    

#############
# init rdb? #
#############
if args.init == 'true':
    Base.metadata.create_all(engine)
session = Session()
    



for v in veps.find( { '$or': [{ "transcript_consequences.polyphen_prediction" : "probably_damaging" },
                              {  "transcript_consequences.sift_prediction"     : "deleterious"}] } ):

    for tc in v['transcript_consequences']:
        if 'missense_variant' in tc['consequence_terms']:

            sample_filename = path.basename(v['vep_json']).split('.')
            sample          = sample_filename[0]
            pipeline        = "->".join(sample_filename[1:-2])
            
            consequence = Consequence(
                sample            = sample,
                pipeline          = pipeline,
                variant_id        = v['id'],
                chrom             = v['seq_region_name'],
                start             = v['start'],
                end               = v['end'],
                amino_acids       = tc['amino_acids'],
                biotype           = tc[u'biotype'],
                cdna_start        = tc[u'cdna_start'],                
                cdna_end          = tc[u'cdna_end'],
                cds_start         = tc[u'cds_start'],                
                cds_end           = tc[u'cds_end'],
                codons            = tc[u'codons'],
                exon              = tc[u'exon'],
                gene_id           = tc[u'gene_id'],
                gene_symbol       = tc[u'gene_symbol'],
                hgnc_id           = tc[u'hgnc_id'],
                impact            = tc[u'impact'],
                protein_start     = tc[u'protein_start'],
                protein_end       = tc[u'protein_end'],
                protein_id        = tc[u'protein_id'],
                consequence_terms = ";".join(tc['consequence_terms']),
                transcript_id     = tc[u'transcript_id'],
                uniparc           = tc[u'uniparc'],
                variant_allele    = tc[u'variant_allele'] )
            session.add(consequence)
            session.commit()

