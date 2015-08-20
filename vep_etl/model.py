from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean, create_engine

##################
# DataBase Model #
##################
Base = declarative_base()

class Colocated_variant(Base):
    __tablename__ = 'colocated_variants' 
    id                    = Column(Integer, primary_key=True)
    sample                = Column(String)
    pipeline              = Column(String) 
    variant_id            = Column(String)
    chrom                 = Column(String) # v['seq_region_name'],
    start                 = Column(Integer) 
    end                   = Column(Integer)
    biotype               = Column(String)
    
    aa_allele             = Column(String)
    aa_maf                = Column(String)
    afr_allele            = Column(String)
    afr_maf               = Column(String)
    allele_string         = Column(String)
    amr_allele            = Column(String)
    amr_maf               = Column(String)
    clin_sig              = Column(String)
    ea_allele             = Column(String)
    ea_maf                = Column(String)
    EAS                   = Column(String)
    end                   = Column(String)
    eur_allele            = Column(String)
    eur_maf               = Column(String)
    colocation_id         = Column(String)
    minor_allele          = Column(String)
    minor_allele_freq     = Column(String)
    pubmed                = Column(String)
    SAS                   = Column(String)
    somatic               = Column(String)
    start                 = Column(String)
    strand                = Column(String)



class Regulatory_feature_consequence(Base):
    __tablename__ = 'regulatory_features' 
    id                    = Column(Integer, primary_key=True)
    sample                = Column(String)
    pipeline              = Column(String) 
    variant_id            = Column(String)
    chrom                 = Column(String) # v['seq_region_name'],
    start                 = Column(Integer) 
    end                   = Column(Integer)
    biotype               = Column(String)
    impact                = Column(String)
    regulatory_feature_id = Column(String)
    variant_allele        = Column(String)    
    sas_maf               = Column(String)
    eas_maf               = Column(String)



class Three_prime_UTR_variant(Base):
    __tablename__ = 'three_prime_UTR_variant'
    id                 = Column(Integer, primary_key=True)
    sample             = Column(String)
    pipeline           = Column(String) 
    variant_id         = Column(String)
    chrom              = Column(String) # v['seq_region_name'],
    start              = Column(Integer) 
    end                = Column(Integer)
    biotype            = Column(String)
    canonical          = Column(Boolean)
    ccds               = Column(String, nullable=True)
    cdna_end           = Column(Integer, nullable=True)
    cdna_start         = Column(Integer, nullable=True)
    consequence_terms  = Column(String, nullable=True)
    eas_maf            = Column(String, nullable=True)
    exon               = Column(String, nullable=True)
    gene_id            = Column(String, nullable=True)
    gene_symbol        = Column(String, nullable=True)
    gene_symbol_source = Column(String, nullable=True)
    hgnc_id            = Column(Integer, nullable=True)
    impact             = Column(String, nullable=True)
    protein_id         = Column(String, nullable=True)
    sas_maf            = Column(String, nullable=True)
    strand             = Column(Integer, nullable=True)
    swissprot          = Column(String, nullable=True)
    transcript_id      = Column(String, nullable=True)
    trembl             = Column(String, nullable=True)
    uniparc            = Column(String, nullable=True)
    variant_allele     = Column(String, nullable=True)

 
class NMD_transcript_variant(Base):
    __tablename__ = 'nmd_transcript_variant'
    id                 = Column(Integer, primary_key=True)
    sample             = Column(String)
    pipeline           = Column(String) 
    variant_id         = Column(String)
    chrom              = Column(String) # v['seq_region_name'],
    start              = Column(Integer) 
    end                = Column(Integer)
    amino_acids        = Column(String, nullable=True)
    biotype            = Column(String, nullable=True)
    canonical          = Column(Boolean, nullable=True)
    cdna_end           = Column(Integer, nullable=True)
    cdna_start         = Column(Integer, nullable=True)
    cds_end            = Column(Integer, nullable=True)
    cds_start          = Column(Integer, nullable=True)
    codons             = Column(String, nullable=True)
    consequence_terms  = Column(String, nullable=True)
    domains            = Column(String, nullable=True)
    eas_maf            = Column(String, nullable=True)
    exon               = Column(String, nullable=True)
    gene_id            = Column(String, nullable=True)
    gene_symbol        = Column(String, nullable=True)
    gene_symbol_source = Column(String, nullable=True)
    hgnc_id            = Column(Integer, nullable=True)
    impact             = Column(String, nullable=True)
    intron             = Column(String, nullable=True)
    polyphen_prediction = Column(String, nullable=True)
    polyphen_score     = Column(Float, nullable=True)
    protein_end        = Column(Integer, nullable=True)
    protein_id         = Column(String, nullable=True)
    protein_start      = Column(Integer, nullable=True)
    sas_maf            = Column(String, nullable=True)
    sift_prediction    = Column(String, nullable=True)
    sift_score         = Column(Float, nullable=True)
    strand             = Column(Integer, nullable=True)
    swissprot          = Column(String, nullable=True)
    transcript_id      = Column(String, nullable=True)
    trembl             = Column(String, nullable=True)
    uniparc            = Column(String, nullable=True)
    variant_allele     = Column(String, nullable=True)




    
class Downstream_gene_variant(Base):
    __tablename__      = 'downstream_gene_variant'
    id                 = Column(Integer, primary_key=True)
    sample             = Column(String)
    pipeline           = Column(String) 
    variant_id         = Column(String)
    chrom              = Column(String) # v['seq_region_name'],
    start              = Column(Integer) 
    end                = Column(Integer)
    biotype            = Column(String)
    canonical          = Column(Boolean)
    ccds               = Column(String, nullable=True)
    consequence_terms  = Column(String, nullable=True)
    distance           = Column(Integer, nullable=True)
    eas_maf            = Column(String, nullable=True)
    gene_id            = Column(String, nullable=True)
    gene_symbol        = Column(String, nullable=True)
    gene_symbol_source = Column(String, nullable=True)
    hgnc_id            = Column(Integer, nullable=True)
    impact             = Column(String, nullable=True)
    protein_id         = Column(String, nullable=True)
    sas_maf            = Column(String, nullable=True)
    strand             = Column(Integer, nullable=True)
    swissprot          = Column(String, nullable=True)
    transcript_id      = Column(String, nullable=True)
    trembl             = Column(String, nullable=True)
    uniparc            = Column(String, nullable=True)
    variant_allele     = Column(String, nullable=True)


class Intron_variant(Base):
    __tablename__ = 'intron_variant'
    id                 = Column(Integer, primary_key=True)
    sample             = Column(String)
    pipeline           = Column(String) 
    variant_id         = Column(String)
    chrom              = Column(String) # v['seq_region_name'],
    start              = Column(Integer) 
    end                = Column(Integer)
    biotype            = Column(String)
    canonical          = Column(Boolean)
    ccds               = Column(String, nullable=True)
    consequence_terms  = Column(String, nullable=True)
    eas_maf            = Column(String, nullable=True)
    gene_id            = Column(String, nullable=True)
    gene_symbol        = Column(String, nullable=True)
    gene_symbol_source = Column(String, nullable=True)
    hgnc_id            = Column(Integer, nullable=True)
    impact             = Column(String, nullable=True)
    intron             = Column(String, nullable=True)
    protein_id         = Column(String, nullable=True)
    sas_maf            = Column(String, nullable=True)
    strand             = Column(Integer, nullable=True)
    swissprot          = Column(String, nullable=True)
    transcript_id      = Column(String, nullable=True)
    trembl             = Column(String, nullable=True)
    uniparc            = Column(String, nullable=True)
    variant_allele     = Column(String, nullable=True)



    
class Missense_variant(Base):
    __tablename__     = 'missense_variant'
    id                = Column(Integer, primary_key=True)
    sample            = Column(String)
    pipeline          = Column(String) 
    variant_id        = Column(String)
    chrom             = Column(String) # v['seq_region_name'],
    start             = Column(Integer) 
    end               = Column(Integer)
    amino_acids        = Column(String)
    biotype            = Column(String)
    canonical          = Column(Boolean)
    ccds               = Column(String, nullable=True)
    cdna_end           = Column(Integer, nullable=True)
    cdna_start         = Column(Integer, nullable=True)
    cds_end            = Column(Integer, nullable=True)
    cds_start          = Column(Integer, nullable=True)
    codons             = Column(String, nullable=True)
    consequence_terms  = Column(String, nullable=True)
    domains            = Column(String, nullable=True)
    eas_maf            = Column(String, nullable=True)
    exon               = Column(String, nullable=True)
    gene_id            = Column(String, nullable=True)
    gene_symbol        = Column(String, nullable=True)
    gene_symbol_source = Column(String, nullable=True)
    hgnc_id            = Column(Integer, nullable=True)
    impact             = Column(String, nullable=True)
    polyphen_prediction = Column(String, nullable=True)
    polyphen_score     = Column(Float, nullable=True)
    protein_end        = Column(Integer, nullable=True)
    protein_id         = Column(String, nullable=True)
    protein_start      = Column(Integer, nullable=True)
    sas_maf            = Column(String, nullable=True)
    sift_prediction    = Column(String, nullable=True)
    sift_score         = Column(Float, nullable=True)
    strand             = Column(Integer, nullable=True)
    swissprot          = Column(String, nullable=True)
    transcript_id      = Column(String, nullable=True)
    trembl             = Column(String, nullable=True)
    uniparc            = Column(String, nullable=True)
    variant_allele     = Column(String, nullable=True)



class Non_coding_transcript_exon_variant(Base):
    __tablename__ = 'non_coding_transcript_exon_variant'
    id                = Column(Integer, primary_key=True)
    sample            = Column(String)
    pipeline          = Column(String) 
    variant_id        = Column(String)
    chrom             = Column(String) # v['seq_region_name'],
    start             = Column(Integer) 
    end               = Column(Integer)
    biotype            = Column(String)
    canonical          = Column(Boolean)
    cdna_end           = Column(Integer, nullable=True)
    cdna_start         = Column(Integer, nullable=True)
    consequence_terms  = Column(String, nullable=True)
    eas_maf            = Column(String, nullable=True)
    exon               = Column(String, nullable=True)
    gene_id            = Column(String, nullable=True)
    gene_symbol        = Column(String, nullable=True)
    gene_symbol_source = Column(String, nullable=True)
    hgnc_id            = Column(Integer, nullable=True)
    impact             = Column(String, nullable=True)
    sas_maf            = Column(String, nullable=True)
    strand             = Column(Integer, nullable=True)
    transcript_id      = Column(String, nullable=True)
    variant_allele     = Column(String, nullable=True)

    


class Non_coding_transcript_variant(Base):
    __tablename__ = 'non_coding_transcript_variant'
    id                 = Column(Integer, primary_key=True)
    sample             = Column(String)
    pipeline           = Column(String) 
    variant_id         = Column(String)
    chrom              = Column(String) # v['seq_region_name'],
    start              = Column(Integer) 
    end                = Column(Integer)
    biotype            = Column(String)
    canonical          = Column(Boolean)
    cdna_end           = Column(Integer, nullable=True)
    cdna_start         = Column(Integer, nullable=True)
    consequence_terms  = Column(String, nullable=True)
    eas_maf            = Column(String, nullable=True)
    exon               = Column(String, nullable=True)
    gene_id            = Column(String, nullable=True)
    gene_symbol        = Column(String, nullable=True)
    gene_symbol_source = Column(String, nullable=True)
    hgnc_id            = Column(Integer, nullable=True)
    impact             = Column(String, nullable=True)
    intron             = Column(String, nullable=True)
    sas_maf            = Column(String, nullable=True)
    strand             = Column(Integer, nullable=True)
    transcript_id      = Column(String, nullable=True)
    variant_allele     = Column(String, nullable=True)


    


class Splice_region_variant(Base):
    __tablename__ = 'splice_region_variant'
    id                 = Column(Integer, primary_key=True)
    sample             = Column(String)
    pipeline           = Column(String) 
    variant_id         = Column(String)
    chrom              = Column(String) # v['seq_region_name'],
    start              = Column(Integer) 
    end                = Column(Integer)
    amino_acids        = Column(String, nullable=True)
    biotype            = Column(String)
    canonical          = Column(Boolean)
    ccds               = Column(String, nullable=True)
    cdna_end           = Column(Integer, nullable=True)
    cdna_start         = Column(Integer, nullable=True)
    cds_end            = Column(Integer, nullable=True)
    cds_start          = Column(Integer, nullable=True)
    codons             = Column(String, nullable=True)
    consequence_terms  = Column(String, nullable=True)
    domains            = Column(String, nullable=True)
    eas_maf            = Column(String, nullable=True)
    exon               = Column(String, nullable=True)
    gene_id            = Column(String, nullable=True)
    gene_symbol        = Column(String, nullable=True)
    gene_symbol_source = Column(String, nullable=True)
    hgnc_id            = Column(Integer, nullable=True)
    impact             = Column(String, nullable=True)
    intron             = Column(String, nullable=True)
    polyphen_prediction = Column(String, nullable=True)
    polyphen_score     = Column(Float, nullable=True)
    protein_end        = Column(Integer, nullable=True)
    protein_id         = Column(String, nullable=True)
    protein_start      = Column(Integer, nullable=True)
    sas_maf            = Column(String, nullable=True)
    sift_prediction    = Column(String, nullable=True)
    sift_score         = Column(Float, nullable=True)
    strand             = Column(Integer, nullable=True)
    swissprot          = Column(String, nullable=True)
    transcript_id      = Column(String, nullable=True)
    trembl             = Column(String, nullable=True)
    uniparc            = Column(String, nullable=True)
    variant_allele     = Column(String, nullable=True)



class Synonymous_variant(Base):
    __tablename__ = 'synonymous_variant'
    id                 = Column(Integer, primary_key=True)
    sample             = Column(String)
    pipeline           = Column(String) 
    variant_id         = Column(String)
    chrom              = Column(String) # v['seq_region_name'],
    start              = Column(Integer) 
    end                = Column(Integer)
    amino_acids        = Column(String, nullable=True)
    canonical          = Column(Boolean)    
    biotype            = Column(String)
    ccds               = Column(String, nullable=True)
    cdna_end           = Column(Integer, nullable=True)
    cdna_start         = Column(Integer, nullable=True)
    cds_end            = Column(Integer, nullable=True)
    cds_start          = Column(Integer, nullable=True)
    codons             = Column(String, nullable=True)
    consequence_terms  = Column(String, nullable=True)
    domains            = Column(String, nullable=True)
    eas_maf            = Column(String, nullable=True)
    exon               = Column(String, nullable=True)
    gene_id            = Column(String, nullable=True)
    gene_symbol        = Column(String, nullable=True)
    gene_symbol_source = Column(String, nullable=True)
    hgnc_id            = Column(Integer, nullable=True)
    impact             = Column(String, nullable=True)
    protein_end        = Column(Integer, nullable=True)
    protein_id         = Column(String, nullable=True)
    protein_start      = Column(Integer, nullable=True)
    sas_maf            = Column(String, nullable=True)
    strand             = Column(Integer, nullable=True)
    swissprot          = Column(String, nullable=True)
    transcript_id      = Column(String, nullable=True)
    trembl             = Column(String, nullable=True)
    uniparc            = Column(String, nullable=True)
    variant_allele     = Column(String, nullable=True)



    

class Upstream_gene_variant(Base):
    __tablename__ = 'upstream_gene_variant'
    id                 = Column(Integer, primary_key=True)
    sample             = Column(String)
    pipeline           = Column(String) 
    variant_id         = Column(String)
    chrom              = Column(String) # v['seq_region_name'],
    start              = Column(Integer) 
    end                = Column(Integer)
    biotype            = Column(String)
    canonical          = Column(Boolean)
    ccds               = Column(String, nullable=True)
    consequence_terms  = Column(String, nullable=True)
    distance           = Column(Integer, nullable=True)
    eas_maf            = Column(String, nullable=True)
    gene_id            = Column(String, nullable=True)
    gene_symbol        = Column(String, nullable=True)
    gene_symbol_source = Column(String, nullable=True)
    hgnc_id            = Column(Integer, nullable=True)
    impact             = Column(String, nullable=True)
    protein_id         = Column(String, nullable=True)
    sas_maf            = Column(String, nullable=True)
    strand             = Column(Integer, nullable=True)
    swissprot          = Column(String, nullable=True)
    transcript_id      = Column(String, nullable=True)
    trembl             = Column(String, nullable=True)
    uniparc            = Column(String, nullable=True)
    variant_allele     = Column(String, nullable=True)












##############################
# Void dictionaries for init #
##############################
void_Three_prime_UTR_variant = {
    'canonical'        : None,
    'ccds'             : None,
    'cdna_end'         : None,
    'cdna_start'       : None,
    'consequence_terms': None,
    'eas_maf'          : None,
    'exon'             : None,
    'gene_id'          : None,
    'gene_symbol'      : None,
    'gene_symbol_source': None,
    'hgnc_id'          : None,
    'impact'           : None,
    'protein_id'       : None,
    'sas_maf'          : None,
    'strand'           : None,
    'swissprot'        : None,
    'transcript_id'    : None,
    'trembl'           : None,
    'uniparc'          : None,
    'variant_allele'   : None,
}
 
void_NMD_transcript_variant = {
    'amino_acids'      : None,
    'canonical'        : None,
    'cdna_end'         : None,
    'cdna_start'       : None,
    'cds_end'          : None,
    'cds_start'        : None,
    'codons'           : None,
    'consequence_terms': None,
    'domains'          : None,
    'eas_maf'          : None,
    'exon'             : None,
    'gene_id'          : None,
    'gene_symbol'      : None,
    'gene_symbol_source': None,
    'hgnc_id'          : None,
    'impact'           : None,
    'intron'           : None,
    'polyphen_prediction': None,
    'polyphen_score'   : None,
    'protein_end'      : None,
    'protein_id'       : None,
    'protein_start'    : None,
    'sas_maf'          : None,
    'sift_prediction'  : None,
    'sift_score'       : None,
    'strand'           : None,
    'swissprot'        : None,
    'transcript_id'    : None,
    'trembl'           : None,
    'uniparc'          : None,
    'variant_allele'   : None,
}



void_Downstream_gene_variant = {
    'canonical'        : None,
    'ccds'             : None,
    'consequence_terms': None,
    'distance'         : None,
    'eas_maf'          : None,
    'gene_id'          : None,
    'gene_symbol'      : None,
    'gene_symbol_source': None,
    'hgnc_id'          : None,
    'impact'           : None,
    'protein_id'       : None,
    'sas_maf'          : None,
    'strand'           : None,
    'swissprot'        : None,
    'transcript_id'    : None,
    'trembl'           : None,
    'uniparc'          : None,
    'variant_allele'   : None,
}

void_Intron_variant = {
    'canonical'        : None,
    'ccds'             : None,
    'consequence_terms': None,
    'eas_maf'          : None,
    'gene_id'          : None,
    'gene_symbol'      : None,
    'gene_symbol_source': None,
    'hgnc_id'          : None,
    'impact'           : None,
    'intron'           : None,
    'protein_id'       : None,
    'sas_maf'          : None,
    'strand'           : None,
    'swissprot'        : None,
    'transcript_id'    : None,
    'trembl'           : None,
    'uniparc'          : None,
    'variant_allele'   : None,
}


    
void_Missense_variant = {
    'amino_acids'      : None,
    'canonical'        : None,
    'ccds'             : None,
    'cdna_end'         : None,
    'cdna_start'       : None,
    'cds_end'          : None,
    'cds_start'        : None,
    'codons'           : None,
    'consequence_terms': None,
    'domains'          : None,
    'eas_maf'          : None,
    'exon'             : None,
    'gene_id'          : None,
    'gene_symbol'      : None,
    'gene_symbol_source': None,
    'hgnc_id'          : None,
    'impact'           : None,
    'polyphen_prediction': None,
    'polyphen_score'   : None,
    'protein_end'      : None,
    'protein_id'       : None,
    'protein_start'    : None,
    'sas_maf'          : None,
    'sift_prediction'  : None,
    'sift_score'       : None,
    'strand'           : None,
    'swissprot'        : None,
    'transcript_id'    : None,
    'trembl'           : None,
    'uniparc'          : None,
    'variant_allele'   : None,
}

void_Non_coding_transcript_exon_variant = {
    'canonical'        : None,
    'cdna_end'         : None,
    'cdna_start'       : None,
    'consequence_terms': None,
    'eas_maf'          : None,
    'exon'             : None,
    'gene_id'          : None,
    'gene_symbol'      : None,
    'gene_symbol_source': None,
    'hgnc_id'          : None,
    'impact'           : None,
    'sas_maf'          : None,
    'strand'           : None,
    'transcript_id'    : None,
    'variant_allele'   : None,
}
    


void_Non_coding_transcript_variant = {
    'canonical'        : None,
    'cdna_end'         : None,
    'cdna_start'       : None,
    'consequence_terms': None,
    'eas_maf'          : None,
    'exon'             : None,
    'gene_id'          : None,
    'gene_symbol'      : None,
    'gene_symbol_source': None,
    'hgnc_id'          : None,
    'impact'           : None,
    'intron'           : None,
    'sas_maf'          : None,
    'strand'           : None,
    'transcript_id'    : None,
    'variant_allele'   : None,
}

    


void_Splice_region_variant = {
    'amino_acids'      : None,
    'canonical'        : None,
    'ccds'             : None,
    'cdna_end'         : None,
    'cdna_start'       : None,
    'cds_end'          : None,
    'cds_start'        : None,
    'codons'           : None,
    'consequence_terms': None,
    'domains'          : None,
    'eas_maf'          : None,
    'exon'             : None,
    'gene_id'          : None,
    'gene_symbol'      : None,
    'gene_symbol_source': None,
    'hgnc_id'          : None,
    'impact'           : None,
    'intron'           : None,
    'polyphen_prediction': None,
    'polyphen_score'   : None,
    'protein_end'      : None,
    'protein_id'       : None,
    'protein_start'    : None,
    'sas_maf'          : None,
    'sift_prediction'  : None,
    'sift_score'       : None,
    'strand'           : None,
    'swissprot'        : None,
    'transcript_id'    : None,
    'trembl'           : None,
    'uniparc'          : None,
    'variant_allele'   : None,
}


void_Synonymous_variant = {
    'amino_acids'      : None,
    'canonical'        : None,
    'ccds'             : None,
    'cdna_end'         : None,
    'cdna_start'       : None,
    'cds_end'          : None,
    'cds_start'        : None,
    'codons'           : None,
    'consequence_terms': None,
    'domains'          : None,
    'eas_maf'          : None,
    'exon'             : None,
    'gene_id'          : None,
    'gene_symbol'      : None,
    'gene_symbol_source': None,
    'hgnc_id'          : None,
    'impact'           : None,
    'protein_end'      : None,
    'protein_id'       : None,
    'protein_start'    : None,
    'sas_maf'          : None,
    'strand'           : None,
    'swissprot'        : None,
    'transcript_id'    : None,
    'trembl'           : None,
    'uniparc'          : None,
    'variant_allele'   : None,
}
