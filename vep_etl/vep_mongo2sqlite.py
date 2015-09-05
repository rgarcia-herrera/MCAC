import argparse
import json
import pymongo
from bson.objectid import ObjectId
from pprint import pformat, pprint
from os import path

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy import Column, Integer, String, Float, create_engine

# from clinical_data import clinical_data
from model import *

parser = argparse.ArgumentParser(description='Load Variant Effect Prediction MongoDB docs to RDB.')
parser.add_argument('--mongo_url', default='mongodb://localhost:27017/', help="MongoDB URL, default: mongodb://localhost:27017/")
parser.add_argument('--rdb_url', default='sqlite:///variant_consequences.sqlite', help="DB URL, default: sqlite:///consequences.sqlite")
parser.add_argument('--init', choices=['true','false'], default='false', help="create relational database and tables, default: false")
args = parser.parse_args()


##############
# Mongo init #
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
    Base.metadata.create_all(engine)
session = Session()


cterms = {}
for v in veps.find( { '$or': [{ "transcript_consequences.polyphen_prediction" : { '$in' : ["probably_damaging",
                                                                                           "possibly_damaging"]} },
                              {  "transcript_consequences.sift_prediction"     : "deleterious"}] } ):

    sample_filename = path.basename(v['vep_json']).split('.')
    sample          = sample_filename[0]
    pipeline        = "->".join(sample_filename[1:-2])

    variant = {
        'sample'                : sample,
        'pipeline'              : pipeline,
        'variant_id'            : v['id'],
        'chrom'                 : v['seq_region_name'],
        'start'                 : v['start'],
        'end'                   : v['end'],
        'most_severe_consequence' : v.get('most_severe_consequence'),
        
        'colocated_variants'                  : [],        
        'intron_variants'                     : [],
        'missense_variants'                   : [],
        'nmd_transcript_variants'             : [],
        'non_coding_transcript_exon_variants' : [],
        'non_coding_transcript_variants'      : [],
        'splice_region_variants'              : [],
        'synonymous_variants'                 : [],
        'three_prime_UTR_variants'            : [],
        'upstream_gene_variants'              : [],
        'downstream_gene_variants'            : [],
         
         'regulatory_features'   : [ Regulatory_feature_consequence(**{'regulatory_feature_id' : rfc['regulatory_feature_id'],
                                                                       'impact'                : rfc['impact'],
                                                                       'variant_allele'        : rfc['variant_allele'] } )
                                     for rfc in v.get('regulatory_feature_consequences',[]) ],

    }

    for cv  in v.get('colocated_variants',[]):
        variant['colocated_variants'].append( Colocated_variant(**{ 'key'               : cv.get('id'),
                                                                    'aa_allele'         : cv.get('aa_allele'),
                                                                    'aa_maf'            : cv.get('aa_maf'),
                                                                    'afr_allele'        : cv.get('afr_allele'),
                                                                    'afr_maf'           : cv.get('afr_maf'),
                                                                    'allele_string'     : cv.get('allele_string'),
                                                                    'amr_allele'        : cv.get('amr_allele'),
                                                                    'amr_maf'           : cv.get('amr_maf'),
                                                                    'clin_sig'          : ",".join(cv.get('clin_sig',[])),
                                                                    'ea_allele'         : cv.get('ea_allele'),
                                                                    'ea_maf'            : cv.get('ea_maf'),
                                                                    'eas_allele'        : cv.get('eas_allele'),
                                                                    'eas_maf'           : cv.get('eas_maf'),
                                                                    'eur_allele'        : cv.get('eur_allele'),
                                                                    'eur_maf'           : cv.get('eur_maf'),
                                                                    'colocation_id'     : cv.get('colocation_id'),
                                                                    'minor_allele'      : cv.get('minor_allele'),
                                                                    'minor_allele_freq' : cv.get('minor_allele_freq'),
                                                                    'phenotype_or_disease' : cv.get('phenotype_or_disease'),
                                                                    'pubmed'            : ",".join([str(s) for s in cv.get('pubmed',[])]),
                                                                    'sas_allele'        : cv.get('sas_allele'),
                                                                    'sas_maf'           : cv.get('sas_maf'),
                                                                    'somatic'           : cv.get('somatic'),
                                                                    'start'             : cv.get('start'),
                                                                    'end'               : cv.get('end'),
                                                                    'strand'            : cv.get('strand') } ))


    
    for tc in v.get('transcript_consequences'):
        if '3_prime_UTR_variant' in tc.get('consequence_terms'):
            c = { 'canonical' : tc.get('canonical'),
                  'biotype'   : tc.get('biotype'),
                  'ccds' : tc.get('ccds'),
                  'cdna_end' : tc.get('cdna_end'),
                  'cdna_start' : tc.get('cdna_start'),
                  'consequence_terms' : ",".join(tc.get('consequence_terms')),
                  'exon' : tc.get('exon'),
                  'gene_id' : tc.get('gene_id'),
                  'gene_symbol' : tc.get('gene_symbol'),
                  'gene_symbol_source' : tc.get('gene_symbol_source'),
                  'hgnc_id' : tc.get('hgnc_id'),
                  'impact' : tc.get('impact'),
                  'protein_id' : tc.get('protein_id'),
                  'strand' : tc.get('strand'),
                  'swissprot' : tc.get('swissprot'),
                  'transcript_id' : tc.get('transcript_id'),
                  'trembl' : tc.get('trembl'),
                  'uniparc' : tc.get('uniparc'),
                  'variant_allele' : tc.get('variant_allele')                 
            }
            variant['three_prime_UTR_variants'].append( Three_prime_UTR_variant(**c) )

        if 'NMD_transcript_variant' in tc['consequence_terms']:
            c = { 'amino_acids' : tc.get('amino_acids'),
                  'biotype'   : tc.get('biotype'),
                  'canonical' : tc.get('canonical'),
                  'cdna_end' : tc.get('cdna_end'),
                  'cdna_start' : tc.get('cdna_start'),
                  'cds_end' : tc.get('cds_end'),
                  'cds_start' : tc.get('cds_start'),
                  'codons' : tc.get('codons'),
                  'consequence_terms' : ",".join(tc.get('consequence_terms')),
                  'domains' : pformat(tc.get('domains')),
                  'exon' : tc.get('exon'),
                  'gene_id' : tc.get('gene_id'),
                  'gene_symbol' : tc.get('gene_symbol'),
                  'gene_symbol_source' : tc.get('gene_symbol_source'),
                  'hgnc_id' : tc.get('hgnc_id'),
                  'impact' : tc.get('impact'),
                  'intron' : tc.get('intron'),
                  'polyphen_prediction' : tc.get('polyphen_prediction'),
                  'polyphen_score' : tc.get('polyphen_score'),
                  'protein_end' : tc.get('protein_end'),
                  'protein_id' : tc.get('protein_id'),
                  'protein_start' : tc.get('protein_start'),
                  'sift_prediction' : tc.get('sift_prediction'),
                  'sift_score' : tc.get('sift_score'),
                  'strand' : tc.get('strand'),
                  'swissprot' : tc.get('swissprot'),
                  'transcript_id' : tc.get('transcript_id'),
                  'trembl' : tc.get('trembl'),
                  'uniparc' : tc.get('uniparc'),
                  'variant_allele' : tc.get('variant_allele')             
            } 
            variant['nmd_transcript_variants'].append( NMD_transcript_variant(**c) )

        if 'downstream_gene_variant' in tc['consequence_terms']:
            c = { 'canonical' : tc.get('canonical'),
                  'biotype'   : tc.get('biotype'),
                  'ccds' : tc.get('ccds'),
                  'consequence_terms' : ",".join(tc.get('consequence_terms')),
                  'distance' : tc.get('distance'),
                  'gene_id' : tc.get('gene_id'),
                  'gene_symbol' : tc.get('gene_symbol'),
                  'gene_symbol_source' : tc.get('gene_symbol_source'),
                  'hgnc_id' : tc.get('hgnc_id'),
                  'impact' : tc.get('impact'),
                  'protein_id' : tc.get('protein_id'),
                  'strand' : tc.get('strand'),
                  'swissprot' : tc.get('swissprot'),
                  'transcript_id' : tc.get('transcript_id'),
                  'trembl' : tc.get('trembl'),
                  'uniparc' : tc.get('uniparc'),
                  'variant_allele' : tc.get('variant_allele'),
            } 
            variant['downstream_gene_variants'].append( Downstream_gene_variant(**c) )

        if 'intron_variant' in tc['consequence_terms']:
            c = { 'canonical' : tc.get('canonical'),
                  'biotype'   : tc.get('biotype'),
                  'ccds' : tc.get('ccds'),
                  'consequence_terms' : ",".join(tc.get('consequence_terms')),
                  'gene_id' : tc.get('gene_id'),
                  'gene_symbol' : tc.get('gene_symbol'),
                  'gene_symbol_source' : tc.get('gene_symbol_source'),
                  'hgnc_id' : tc.get('hgnc_id'),
                  'impact' : tc.get('impact'),
                  'intron' : tc.get('intron'),
                  'protein_id' : tc.get('protein_id'),
                  'strand' : tc.get('strand'),
                  'swissprot' : tc.get('swissprot'),
                  'transcript_id' : tc.get('transcript_id'),
                  'trembl' : tc.get('trembl'),
                  'uniparc' : tc.get('uniparc'),
                  'variant_allele' : tc.get('variant_allele'),
            } 
            variant['intron_variants'].append( Intron_variant(**c) )

        if 'missense_variant' in tc['consequence_terms']:
            c = { 'amino_acids' : tc.get('amino_acids'),
                  'canonical' : tc.get('canonical'),
                  'biotype'   : tc.get('biotype'),
                  'ccds' : tc.get('ccds'),
                  'cdna_end' : tc.get('cdna_end'),
                  'cdna_start' : tc.get('cdna_start'),
                  'cds_end' : tc.get('cds_end'),
                  'cds_start' : tc.get('cds_start'),
                  'codons' : tc.get('codons'),
                  'consequence_terms' : ",".join(tc.get('consequence_terms')),
                  'domains' : pformat(tc.get('domains')),
                  'exon' : tc.get('exon'),
                  'gene_id' : tc.get('gene_id'),
                  'gene_symbol' : tc.get('gene_symbol'),
                  'gene_symbol_source' : tc.get('gene_symbol_source'),
                  'hgnc_id' : tc.get('hgnc_id'),
                  'impact' : tc.get('impact'),
                  'polyphen_prediction' : tc.get('polyphen_prediction'),
                  'polyphen_score' : tc.get('polyphen_score'),
                  'protein_end' : tc.get('protein_end'),
                  'protein_id' : tc.get('protein_id'),
                  'protein_start' : tc.get('protein_start'),
                  'sift_prediction' : tc.get('sift_prediction'),
                  'sift_score' : tc.get('sift_score'),
                  'strand' : tc.get('strand'),
                  'swissprot' : tc.get('swissprot'),
                  'transcript_id' : tc.get('transcript_id'),
                  'trembl' : tc.get('trembl'),
                  'uniparc' : tc.get('uniparc'),
                  'variant_allele' : tc.get('variant_allele')
            } 
            variant['missense_variants'].append( Missense_variant(**c) )

        if 'non_coding_transcript_exon_variant' in tc['consequence_terms']:
            c = { 'canonical' : tc.get('canonical'),
                  'biotype'   : tc.get('biotype'),
                  'cdna_end' : tc.get('cdna_end'),
                  'cdna_start' : tc.get('cdna_start'),
                  'consequence_terms' : ",".join(tc.get('consequence_terms')),
                  'exon' : tc.get('exon'),
                  'gene_id' : tc.get('gene_id'),
                  'gene_symbol' : tc.get('gene_symbol'),
                  'gene_symbol_source' : tc.get('gene_symbol_source'),
                  'hgnc_id' : tc.get('hgnc_id'),
                  'impact' : tc.get('impact'),
                  'strand' : tc.get('strand'),
                  'transcript_id' : tc.get('transcript_id'),
                  'variant_allele' : tc.get('variant_allele'),
            } 
            variant['non_coding_transcript_exon_variants'].append( Non_coding_transcript_exon_variant(**c) )

        if 'non_coding_transcript_variant' in tc['consequence_terms']:
            c = { 'canonical' : tc.get('canonical'),
                  'biotype'   : tc.get('biotype'),
                  'cdna_end' : tc.get('cdna_end'),
                  'cdna_start' : tc.get('cdna_start'),
                  'consequence_terms' : ",".join(tc.get('consequence_terms')),
                  'exon' : tc.get('exon'),
                  'gene_id' : tc.get('gene_id'),
                  'gene_symbol' : tc.get('gene_symbol'),
                  'gene_symbol_source' : tc.get('gene_symbol_source'),
                  'hgnc_id' : tc.get('hgnc_id'),
                  'impact' : tc.get('impact'),
                  'intron' : tc.get('intron'),
                  'strand' : tc.get('strand'),
                  'transcript_id' : tc.get('transcript_id'),
                  'variant_allele' : tc.get('variant_allele'),
            } 
            variant['non_coding_transcript_variants'].append( Non_coding_transcript_variant(**c) )

        if 'splice_region_variant' in tc['consequence_terms']:
            c = { 'amino_acids' : tc.get('amino_acids'),
                  'biotype'   : tc.get('biotype'),
                  'canonical' : tc.get('canonical'),
                  'ccds' : tc.get('ccds'),
                  'cdna_end' : tc.get('cdna_end'),
                  'cdna_start' : tc.get('cdna_start'),
                  'cds_end' : tc.get('cds_end'),
                  'cds_start' : tc.get('cds_start'),
                  'codons' : tc.get('codons'),
                  'consequence_terms' : ",".join(tc.get('consequence_terms')),
                  'domains' : pformat(tc.get('domains')),
                  'exon' : tc.get('exon'),
                  'gene_id' : tc.get('gene_id'),
                  'gene_symbol' : tc.get('gene_symbol'),
                  'gene_symbol_source' : tc.get('gene_symbol_source'),
                  'hgnc_id' : tc.get('hgnc_id'),
                  'impact' : tc.get('impact'),
                  'intron' : tc.get('intron'),
                  'polyphen_prediction' : tc.get('polyphen_prediction'),
                  'polyphen_score' : tc.get('polyphen_score'),
                  'protein_end' : tc.get('protein_end'),
                  'protein_id' : tc.get('protein_id'),
                  'protein_start' : tc.get('protein_start'),
                  'sift_prediction' : tc.get('sift_prediction'),
                  'sift_score' : tc.get('sift_score'),
                  'strand' : tc.get('strand'),
                  'swissprot' : tc.get('swissprot'),
                  'transcript_id' : tc.get('transcript_id'),
                  'trembl' : tc.get('trembl'),
                  'uniparc' : tc.get('uniparc'),
                  'variant_allele' : tc.get('variant_allele'),
            } 
            variant['splice_region_variants'].append( Splice_region_variant(**c) )

        if 'synonymous_variant' in tc['consequence_terms']:
            c = { 'amino_acids' : tc.get('amino_acids'),
                  'biotype'   : tc.get('biotype'),                  
                  'canonical' : tc.get('canonical'),
                  'ccds' : tc.get('ccds'),
                  'cdna_end' : tc.get('cdna_end'),
                  'cdna_start' : tc.get('cdna_start'),
                  'cds_end' : tc.get('cds_end'),
                  'cds_start' : tc.get('cds_start'),
                  'codons' : tc.get('codons'),
                  'consequence_terms' : ",".join(tc.get('consequence_terms')),
                  'domains' : pformat(tc.get('domains')),
                  'exon' : tc.get('exon'),
                  'gene_id' : tc.get('gene_id'),
                  'gene_symbol' : tc.get('gene_symbol'),
                  'gene_symbol_source' : tc.get('gene_symbol_source'),
                  'hgnc_id' : tc.get('hgnc_id'),
                  'impact' : tc.get('impact'),
                  'protein_end' : tc.get('protein_end'),
                  'protein_id' : tc.get('protein_id'),
                  'protein_start' : tc.get('protein_start'),
                  'strand' : tc.get('strand'),
                  'swissprot' : tc.get('swissprot'),
                  'transcript_id' : tc.get('transcript_id'),
                  'trembl' : tc.get('trembl'),
                  'uniparc' : tc.get('uniparc'),
                  'variant_allele' : tc.get('variant_allele'),
            } 
            variant['synonymous_variants'].append( Synonymous_variant(**c) )

        if 'upstream_gene_variant' in tc['consequence_terms']:
            c = { 'canonical' : tc.get('canonical'),
                  'biotype'   : tc.get('biotype'),
                  'ccds' : tc.get('ccds'),
                  'consequence_terms' : ",".join(tc.get('consequence_terms')),
                  'distance' : tc.get('distance'),
                  'gene_id' : tc.get('gene_id'),
                  'gene_symbol' : tc.get('gene_symbol'),
                  'gene_symbol_source' : tc.get('gene_symbol_source'),
                  'hgnc_id' : tc.get('hgnc_id'),
                  'impact' : tc.get('impact'),
                  'protein_id' : tc.get('protein_id'),
                  'strand' : tc.get('strand'),
                  'swissprot' : tc.get('swissprot'),
                  'transcript_id' : tc.get('transcript_id'),
                  'trembl' : tc.get('trembl'),
                  'uniparc' : tc.get('uniparc'),
                  'variant_allele' : tc.get('variant_allele'),
            } 
            variant['upstream_gene_variants'].append( Upstream_gene_variant(**c) )
    
    session.add(Variant(**variant))
    session.commit()

