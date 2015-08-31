from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean, create_engine, ForeignKey
from sqlalchemy.orm import relationship, backref

##################
# DataBase Model #
##################
Base = declarative_base()

class Variant(Base):
    __tablename__ = 'variants' 
    id                    = Column(Integer, primary_key=True)
    sample                = Column(String(16))
    pipeline              = Column(String(16)) 
    variant_id            = Column(String(32))
    chrom                 = Column(String(4)) # v['seq_region_name'],
    start                 = Column(Integer) 
    end                   = Column(Integer)
    most_severe_consequence = Column(String(100))    



class Regulatory_feature_consequence(Base):
    __tablename__ = 'regulatory_features' 
    id                    = Column(Integer, primary_key=True)

    variant_id = Column(Integer,
                        ForeignKey('variants.id'))
    variant    = relationship(Variant,
                              primaryjoin=variant_id==Variant.id,
                              backref='regulatory_features')

    impact                = Column(String(32))
    regulatory_feature_id = Column(String(132))
    variant_allele        = Column(String(32))    


    
class Colocated_variant(Base):
    __tablename__ = 'colocated_variants' 
    id                    = Column(Integer, primary_key=True)

    variant_id = Column(Integer,
                        ForeignKey('variants.id'))
    variant    = relationship(Variant,
                              primaryjoin=variant_id==Variant.id,
                              backref='colocated_variants')

    key                   = Column(String(332))
    aa_allele             = Column(String(32))
    aa_maf                = Column(String(32))
    afr_allele            = Column(String(32))
    afr_maf               = Column(String(32))
    allele_string         = Column(String(32))
    amr_allele            = Column(String(32))
    amr_maf               = Column(String(32))
    clin_sig              = Column(String(132))
    ea_allele             = Column(String(32))
    ea_maf                = Column(String(32))
    eas_allele            = Column(String(32))
    eas_maf = Column(String(32))
    eur_allele            = Column(String(32))
    eur_maf               = Column(String(32))
    colocation_id         = Column(String(132))
    minor_allele          = Column(String(32))
    minor_allele_freq     = Column(String(32))
    phenotype_or_disease = Column(String(32))
    pubmed                = Column(String(332))
    sas_allele = Column(String(32))
    sas_maf = Column(String(32))
    somatic               = Column(String(32))
    start                 = Column(String(32))
    end                   = Column(String(32))
    strand                = Column(String(32))





class Three_prime_UTR_variant(Base):
    __tablename__ = 'three_prime_UTR_variant'
    id                 = Column(Integer, primary_key=True)

    variant_id = Column(Integer,
                        ForeignKey('variants.id'))
    variant    = relationship(Variant,
                              primaryjoin=variant_id==Variant.id,
                              backref='three_prime_UTR_variants')

    biotype               = Column(String(32))    
    canonical          = Column(Boolean)
    ccds               = Column(String(32), nullable=True)
    cdna_end           = Column(Integer, nullable=True)
    cdna_start         = Column(Integer, nullable=True)
    consequence_terms  = Column(String(1024), nullable=True)
    exon               = Column(String(132), nullable=True)
    gene_id            = Column(String(132), nullable=True)
    gene_symbol        = Column(String(132), nullable=True)
    gene_symbol_source = Column(String(132), nullable=True)
    hgnc_id            = Column(Integer, nullable=True)
    impact             = Column(String(132), nullable=True)
    protein_id         = Column(String(132), nullable=True)
    strand             = Column(Integer, nullable=True)
    swissprot          = Column(String(32), nullable=True)
    transcript_id      = Column(String(32), nullable=True)
    trembl             = Column(String(132), nullable=True)
    uniparc            = Column(String(32), nullable=True)
    variant_allele     = Column(String(32), nullable=True)

 
class NMD_transcript_variant(Base):
    __tablename__ = 'nmd_transcript_variant'
    id                 = Column(Integer, primary_key=True)

    variant_id = Column(Integer,
                        ForeignKey('variants.id'))
    variant    = relationship(Variant,
                              primaryjoin=variant_id==Variant.id,
                              backref='nmd_transcript_variants')
    
    biotype               = Column(String(32))    
    amino_acids        = Column(String(32), nullable=True)
    canonical          = Column(Boolean, nullable=True)
    cdna_end           = Column(Integer, nullable=True)
    cdna_start         = Column(Integer, nullable=True)
    cds_end            = Column(Integer, nullable=True)
    cds_start          = Column(Integer, nullable=True)
    codons             = Column(String(132), nullable=True)
    consequence_terms  = Column(String(1024), nullable=True)
    domains            = Column(String(4096), nullable=True)
    exon               = Column(String(32), nullable=True)
    gene_id            = Column(String(32), nullable=True)
    gene_symbol        = Column(String(32), nullable=True)
    gene_symbol_source = Column(String(32), nullable=True)
    hgnc_id            = Column(Integer, nullable=True)
    impact             = Column(String(32), nullable=True)
    intron             = Column(String(32), nullable=True)
    polyphen_prediction = Column(String(132), nullable=True)
    polyphen_score     = Column(Float, nullable=True)
    protein_end        = Column(Integer, nullable=True)
    protein_id         = Column(String(132), nullable=True)
    protein_start      = Column(Integer, nullable=True)
    sift_prediction    = Column(String(132), nullable=True)
    sift_score         = Column(Float, nullable=True)
    strand             = Column(Integer, nullable=True)
    swissprot          = Column(String(32), nullable=True)
    transcript_id      = Column(String(32), nullable=True)
    trembl             = Column(String(132), nullable=True)
    uniparc            = Column(String(32), nullable=True)
    variant_allele     = Column(String(32), nullable=True)




    
class Downstream_gene_variant(Base):
    __tablename__      = 'downstream_gene_variant'
    id                 = Column(Integer, primary_key=True)

    variant_id = Column(Integer,
                        ForeignKey('variants.id'))
    variant    = relationship(Variant,
                              primaryjoin=variant_id==Variant.id,
                              backref='downstream_gene_variants')

    biotype               = Column(String(32))    
    canonical          = Column(Boolean)
    ccds               = Column(String(32), nullable=True)
    consequence_terms  = Column(String(1024), nullable=True)
    distance           = Column(Integer, nullable=True)
    gene_id            = Column(String(32), nullable=True)
    gene_symbol        = Column(String(32), nullable=True)
    gene_symbol_source = Column(String(32), nullable=True)
    hgnc_id            = Column(Integer, nullable=True)
    impact             = Column(String(132), nullable=True)
    protein_id         = Column(String(32), nullable=True)
    strand             = Column(Integer, nullable=True)
    swissprot          = Column(String(32), nullable=True)
    transcript_id      = Column(String(32), nullable=True)
    trembl             = Column(String(132), nullable=True)
    uniparc            = Column(String(32), nullable=True)
    variant_allele     = Column(String(32), nullable=True)


class Intron_variant(Base):
    __tablename__ = 'intron_variant'
    id                 = Column(Integer, primary_key=True)

    variant_id = Column(Integer,
                        ForeignKey('variants.id'))
    variant    = relationship(Variant,
                              primaryjoin=variant_id==Variant.id,
                              backref='intron_variants')

    biotype               = Column(String(32))    
    canonical          = Column(Boolean)
    ccds               = Column(String(32), nullable=True)
    consequence_terms  = Column(String(1024), nullable=True)
    gene_id            = Column(String(32), nullable=True)
    gene_symbol        = Column(String(32), nullable=True)
    gene_symbol_source = Column(String(32), nullable=True)
    hgnc_id            = Column(Integer, nullable=True)
    impact             = Column(String(32), nullable=True)
    intron             = Column(String(32), nullable=True)
    protein_id         = Column(String(32), nullable=True)
    strand             = Column(Integer, nullable=True)
    swissprot          = Column(String(32), nullable=True)
    transcript_id      = Column(String(32), nullable=True)
    trembl             = Column(String(132), nullable=True)
    uniparc            = Column(String(32), nullable=True)
    variant_allele     = Column(String(32), nullable=True)



    
class Missense_variant(Base):
    __tablename__     = 'missense_variant'
    id                = Column(Integer, primary_key=True)
    variant_id = Column(Integer,
                        ForeignKey('variants.id'))
    variant    = relationship(Variant,
                              primaryjoin=variant_id==Variant.id,
                              backref='missense_variants')

    amino_acids        = Column(String(132), nullable=True)        
    biotype               = Column(String(32))    
    canonical          = Column(Boolean)
    ccds               = Column(String(32), nullable=True)
    cdna_end           = Column(Integer, nullable=True)
    cdna_start         = Column(Integer, nullable=True)
    cds_end            = Column(Integer, nullable=True)
    cds_start          = Column(Integer, nullable=True)
    codons             = Column(String(32), nullable=True)
    consequence_terms  = Column(String(1024), nullable=True)
    domains            = Column(String(4096), nullable=True)
    exon               = Column(String(32), nullable=True)
    gene_id            = Column(String(32), nullable=True)
    gene_symbol        = Column(String(32), nullable=True)
    gene_symbol_source = Column(String(32), nullable=True)
    hgnc_id            = Column(Integer, nullable=True)
    impact             = Column(String(132), nullable=True)
    polyphen_prediction = Column(String(132), nullable=True)
    polyphen_score     = Column(Float, nullable=True)
    protein_end        = Column(Integer, nullable=True)
    protein_id         = Column(String(32), nullable=True)
    protein_start      = Column(Integer, nullable=True)
    sift_prediction    = Column(String(32), nullable=True)
    sift_score         = Column(Float, nullable=True)
    strand             = Column(Integer, nullable=True)
    swissprot          = Column(String(32), nullable=True)
    transcript_id      = Column(String(32), nullable=True)
    trembl             = Column(String(132), nullable=True)
    uniparc            = Column(String(32), nullable=True)
    variant_allele     = Column(String(32), nullable=True)



class Non_coding_transcript_exon_variant(Base):
    __tablename__ = 'non_coding_transcript_exon_variant'
    id                = Column(Integer, primary_key=True)
    variant_id = Column(Integer,
                        ForeignKey('variants.id'))
    variant    = relationship(Variant,
                              primaryjoin=variant_id==Variant.id,
                              backref='non_coding_transcript_exon_variants')

    biotype               = Column(String(32))    
    canonical          = Column(Boolean)
    cdna_end           = Column(Integer, nullable=True)
    cdna_start         = Column(Integer, nullable=True)
    consequence_terms  = Column(String(1024), nullable=True)
    exon               = Column(String(32), nullable=True)
    gene_id            = Column(String(32), nullable=True)
    gene_symbol        = Column(String(32), nullable=True)
    gene_symbol_source = Column(String(32), nullable=True)
    hgnc_id            = Column(Integer, nullable=True)
    impact             = Column(String(132), nullable=True)
    strand             = Column(Integer, nullable=True)
    transcript_id      = Column(String(32), nullable=True)
    variant_allele     = Column(String(32), nullable=True)

    


class Non_coding_transcript_variant(Base):
    __tablename__ = 'non_coding_transcript_variant'
    id                 = Column(Integer, primary_key=True)

    variant_id = Column(Integer,
                        ForeignKey('variants.id'))
    variant    = relationship(Variant,
                              primaryjoin=variant_id==Variant.id,
                              backref='non_coding_transcript_variants')

    biotype               = Column(String(32))        
    canonical          = Column(Boolean)
    cdna_end           = Column(Integer, nullable=True)
    cdna_start         = Column(Integer, nullable=True)
    consequence_terms  = Column(String(1024), nullable=True)
    exon               = Column(String(32), nullable=True)
    gene_id            = Column(String(32), nullable=True)
    gene_symbol        = Column(String(32), nullable=True)
    gene_symbol_source = Column(String(32), nullable=True)
    hgnc_id            = Column(Integer, nullable=True)
    impact             = Column(String(132), nullable=True)
    intron             = Column(String(32), nullable=True)
    strand             = Column(Integer, nullable=True)
    transcript_id      = Column(String(32), nullable=True)
    variant_allele     = Column(String(32), nullable=True)


    


class Splice_region_variant(Base):
    __tablename__ = 'splice_region_variant'
    id                 = Column(Integer, primary_key=True)

    variant_id = Column(Integer,
                        ForeignKey('variants.id'))
    variant    = relationship(Variant,
                              primaryjoin=variant_id==Variant.id,
                              backref='splice_region_variants')

    biotype               = Column(String(32))    
    amino_acids        = Column(String(132), nullable=True)    
    canonical          = Column(Boolean)
    ccds               = Column(String(32), nullable=True)
    cdna_end           = Column(Integer, nullable=True)
    cdna_start         = Column(Integer, nullable=True)
    cds_end            = Column(Integer, nullable=True)
    cds_start          = Column(Integer, nullable=True)
    codons             = Column(String(32), nullable=True)
    consequence_terms  = Column(String(1024), nullable=True)
    domains            = Column(String(4096), nullable=True)
    exon               = Column(String(32), nullable=True)
    gene_id            = Column(String(32), nullable=True)
    gene_symbol        = Column(String(32), nullable=True)
    gene_symbol_source = Column(String(32), nullable=True)
    hgnc_id            = Column(Integer, nullable=True)
    impact             = Column(String(32), nullable=True)
    intron             = Column(String(32), nullable=True)
    polyphen_prediction = Column(String(132), nullable=True)
    polyphen_score     = Column(Float, nullable=True)
    protein_end        = Column(Integer, nullable=True)
    protein_id         = Column(String(32), nullable=True)
    protein_start      = Column(Integer, nullable=True)
    sift_prediction    = Column(String(32), nullable=True)
    sift_score         = Column(Float, nullable=True)
    strand             = Column(Integer, nullable=True)
    swissprot          = Column(String(32), nullable=True)
    transcript_id      = Column(String(32), nullable=True)
    trembl             = Column(String(132), nullable=True)
    uniparc            = Column(String(32), nullable=True)
    variant_allele     = Column(String(32), nullable=True)



class Synonymous_variant(Base):
    __tablename__ = 'synonymous_variant'
    id                 = Column(Integer, primary_key=True)
    variant_id = Column(Integer,
                        ForeignKey('variants.id'))
    variant    = relationship(Variant,
                              primaryjoin=variant_id==Variant.id,
                              backref='synonymous_variants')

    biotype               = Column(String(32))    
    amino_acids        = Column(String(32), nullable=True)
    canonical          = Column(Boolean)    
    ccds               = Column(String(32), nullable=True)
    cdna_end           = Column(Integer, nullable=True)
    cdna_start         = Column(Integer, nullable=True)
    cds_end            = Column(Integer, nullable=True)
    cds_start          = Column(Integer, nullable=True)
    codons             = Column(String(32), nullable=True)
    consequence_terms  = Column(String(1024), nullable=True)
    domains            = Column(String(4096), nullable=True)
    exon               = Column(String(32), nullable=True)
    gene_id            = Column(String(32), nullable=True)
    gene_symbol        = Column(String(32), nullable=True)
    gene_symbol_source = Column(String(32), nullable=True)
    hgnc_id            = Column(Integer, nullable=True)
    impact             = Column(String(32), nullable=True)
    protein_end        = Column(Integer, nullable=True)
    protein_id         = Column(String(32), nullable=True)
    protein_start      = Column(Integer, nullable=True)
    strand             = Column(Integer, nullable=True)
    swissprot          = Column(String(32), nullable=True)
    transcript_id      = Column(String(32), nullable=True)
    trembl             = Column(String(132), nullable=True)
    uniparc            = Column(String(32), nullable=True)
    variant_allele     = Column(String(32), nullable=True)



    

class Upstream_gene_variant(Base):
    __tablename__ = 'upstream_gene_variant'
    id                 = Column(Integer, primary_key=True)
    variant_id = Column(Integer,
                        ForeignKey('variants.id'))
    variant    = relationship(Variant,
                              primaryjoin=variant_id==Variant.id,
                              backref='upstream_gene_variants')

    biotype               = Column(String(132))        
    canonical          = Column(Boolean)
    ccds               = Column(String(32), nullable=True)
    consequence_terms  = Column(String(1024), nullable=True)
    distance           = Column(Integer, nullable=True)
    gene_id            = Column(String(32), nullable=True)
    gene_symbol        = Column(String(32), nullable=True)
    gene_symbol_source = Column(String(32), nullable=True)
    hgnc_id            = Column(Integer, nullable=True)
    impact             = Column(String(32), nullable=True)
    protein_id         = Column(String(32), nullable=True)
    strand             = Column(Integer, nullable=True)
    swissprot          = Column(String(32), nullable=True)
    transcript_id      = Column(String(32), nullable=True)
    trembl             = Column(String(132), nullable=True)
    uniparc            = Column(String(32), nullable=True)
    variant_allele     = Column(String(32), nullable=True)

