from time import sleep
import random as rd
import networkx as nx
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


#######################
# init some variables #
#######################
theta = 1


#############
# ORM setup #
#############
Base    = declarative_base()

# predictions may have more zero or more existing variation
prediction_variation = Table(
    "prediction_variation",
    Base.metadata,
    Column("fk_predictions", Integer, ForeignKey("predictions.id")),
    Column("fk_variation", Integer, ForeignKey("variations.id")),
)

# prediction model
class Prediction(Base):
    __tablename__='predictions'
    
    id      = Column(Integer, primary_key=True)
    sample  = Column(String)
    #file
    #score    
    # Uploaded_variation
    #Location
    #Allele
    #Gene
    #Feature
    #Feature_type
    #Consequence
    #cDNA_position
    #CDS_position
    #Protein_position
    #Amino_acids
    #Codons
    #Existing_variation
    #Extra

## Extra column keys:
## IMPACT : Subjective impact classification
## DISTANCE : Shortest distance from variant to transcript
## STRAND : Strand of the feature (1/-1)
## SYMBOL : Gene symbol (e.g. HGNC)
## SYMBOL_SOURCE : Source of gene symbol
## HGNC_ID : Stable identifer of HGNC gene symbol
## BIOTYPE : Biotype of transcript or regulatory feature
## CANONICAL : Indicates if transcript is canonical for this gene
## TSL : Transcript support level
## CCDS : Indicates if transcript is a CCDS transcript
## ENSP : Ensembl protein identifer
## SWISSPROT : UniProtKB/Swiss-Prot identifier
## TREMBL : UniProtKB/TrEMBL identifier
## UNIPARC : UniParc identifier
## SIFT : SIFT prediction and/or score
## PolyPhen : PolyPhen prediction and/or score
## EXON : Exon number(s) / total
## INTRON : Intron number(s) / total
## DOMAINS : The source and identifer of any overlapping protein
## domains
## GMAF : Minor allele and frequency of existing variant in 1000
## Genomes combined population
## AFR_MAF : Frequency of existing variant in 1000 Genomes combined
## African population
## AMR_MAF : Frequency of existing variant in 1000 Genomes combined
## American population
## ASN_MAF : Frequency of existing variant in 1000 Genomes combined
## Asian population
## EAS_MAF : Frequency of existing variant in 1000 Genomes combined
## East Asian population
## EUR_MAF : Frequency of existing variant in 1000 Genomes combined
## European population
## SAS_MAF : Frequency of existing variant in 1000 Genomes combined
## South Asian population
## AA_MAF : Frequency of existing variant in NHLBI-ESP African
## American population
## EA_MAF : Frequency of existing variant in NHLBI-ESP European
## American population
## CLIN_SIG : Clinical significance of variant from dbSNP
## SOMATIC : Somatic status of existing variant
## PUBMED : Pubmed ID(s) of publications that cite existing variant
## MOTIF_NAME : The source and identifier of a transcription factor
## binding profile (TFBP) aligned at this position
## MOTIF_POS : The relative position of the variation in the aligned
## TFBP
## HIGH_INF_POS : A flag indicating if the variant falls in a high
## information position of the TFBP
## MOTIF_SCORE_CHANGE : The difference in motif score of the reference
## and variant sequences for the TFBP



    # use this for existing variation?
    # edges   = relationship(
    #     "Edge",
    #     secondary=nodes_edges
    # )



# Edge model     #
class Variation(Base):
    __tablename__='variations'
    
    id    = Column(Integer, primary_key=True)
    rs    = Column(Integer)
    
    nodes = relationship(
        "Prediction",
        secondary=prediction_variation
    )



        
    def __repr__(self):
        return '<Edge %s, w=%s>' % (self.nodes, self.w)




