from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean, create_engine

##################
# DataBase Model #
##################
Base = declarative_base()



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
    ccds               = Column(String)
    cdna_end           = Column(Integer)
    cdna_start         = Column(Integer)
    consequence_terms  = Column(String)
    eas_maf            = Column(String)
    exon               = Column(String)
    gene_id            = Column(String)
    gene_symbol        = Column(String)
    gene_symbol_source = Column(String)
    hgnc_id            = Column(Integer)
    impact             = Column(String)
    protein_id         = Column(String)
    sas_maf            = Column(String)
    strand             = Column(Integer)
    swissprot          = Column(String)
    transcript_id      = Column(String)
    trembl             = Column(String)
    uniparc            = Column(String)
    variant_allele     = Column(String)

 
class NMD_transcript_variant(Base):
    __tablename__ = 'consequences'
    id                 = Column(Integer, primary_key=True)
    sample             = Column(String)
    pipeline           = Column(String) 
    variant_id         = Column(String)
    chrom              = Column(String) # v['seq_region_name'],
    start              = Column(Integer) 
    end                = Column(Integer)
    amino_acids        = Column(String)
    biotype            = Column(String)
    canonical          = Column(Boolean)
    cdna_end           = Column(Integer)
    cdna_start         = Column(Integer)
    cds_end            = Column(Integer)
    cds_start          = Column(Integer)
    codons             = Column(String)
    consequence_terms  = Column(String)
    domains            = Column(String)
    eas_maf            = Column(String)
    exon               = Column(String)
    gene_id            = Column(String)
    gene_symbol        = Column(String)
    gene_symbol_source = Column(String)
    hgnc_id            = Column(Integer)
    impact             = Column(String)
    intron             = Column(String)
    polyphen_prediction = Column(String)
    polyphen_score     = Column(Float)
    protein_end        = Column(Integer)
    protein_id         = Column(String)
    protein_start      = Column(Integer)
    sas_maf            = Column(String)
    sift_prediction    = Column(String)
    sift_score         = Column(Float)
    strand             = Column(Integer)
    swissprot          = Column(String)
    transcript_id      = Column(String)
    trembl             = Column(String)
    uniparc            = Column(String)
    variant_allele     = Column(String)




    
class Downstream_gene_variant(Base):
    __tablename__      = 'consequences'
    id                 = Column(Integer, primary_key=True)
    sample             = Column(String)
    pipeline           = Column(String) 
    variant_id         = Column(String)
    chrom              = Column(String) # v['seq_region_name'],
    start              = Column(Integer) 
    end                = Column(Integer)
    biotype            = Column(String)
    canonical          = Column(Boolean)
    ccds               = Column(String)
    consequence_terms  = Column(String)
    distance           = Column(Integer)
    eas_maf            = Column(String)
    gene_id            = Column(String)
    gene_symbol        = Column(String)
    gene_symbol_source = Column(String)
    hgnc_id            = Column(Integer)
    impact             = Column(String)
    protein_id         = Column(String)
    sas_maf            = Column(String)
    strand             = Column(Integer)
    swissprot          = Column(String)
    transcript_id      = Column(String)
    trembl             = Column(String)
    uniparc            = Column(String)
    variant_allele     = Column(String)


class Intron_variant(Base):
    __tablename__ = 'consequences'
    id                 = Column(Integer, primary_key=True)
    sample             = Column(String)
    pipeline           = Column(String) 
    variant_id         = Column(String)
    chrom              = Column(String) # v['seq_region_name'],
    start              = Column(Integer) 
    end                = Column(Integer)
    biotype            = Column(String)
    canonical          = Column(Boolean)
    ccds               = Column(String)
    consequence_terms  = Column(String)
    eas_maf            = Column(String)
    gene_id            = Column(String)
    gene_symbol        = Column(String)
    gene_symbol_source = Column(String)
    hgnc_id            = Column(Integer)
    impact             = Column(String)
    intron             = Column(String)
    protein_id         = Column(String)
    sas_maf            = Column(String)
    strand             = Column(Integer)
    swissprot          = Column(String)
    transcript_id      = Column(String)
    trembl             = Column(String)
    uniparc            = Column(String)
    variant_allele     = Column(String)



    
class Issense_variant(Base):
    __tablename__ = 'consequences'
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
    ccds               = Column(String)
    cdna_end           = Column(Integer)
    cdna_start         = Column(Integer)
    cds_end            = Column(Integer)
    cds_start          = Column(Integer)
    codons             = Column(String)
    consequence_terms  = Column(String)
    domains            = Column(String)
    eas_maf            = Column(String)
    exon               = Column(String)
    gene_id            = Column(String)
    gene_symbol        = Column(String)
    gene_symbol_source = Column(String)
    hgnc_id            = Column(Integer)
    impact             = Column(String)
    polyphen_prediction = Column(String)
    polyphen_score     = Column(Float)
    protein_end        = Column(Integer)
    protein_id         = Column(String)
    protein_start      = Column(Integer)
    sas_maf            = Column(String)
    sift_prediction    = Column(String)
    sift_score         = Column(Float)
    strand             = Column(Integer)
    swissprot          = Column(String)
    transcript_id      = Column(String)
    trembl             = Column(String)
    uniparc            = Column(String)
    variant_allele     = Column(String)



class Nonn_coding_transcript_exon_variant(Base)String:
    __tablename__ = 'consequences'
    id                = Column(Integer, primary_key=True)
    sample            = Column(String)
    pipeline          = Column(String) 
    variant_id        = Column(String)
    chrom             = Column(String) # v['seq_region_name'],
    start             = Column(Integer) 
    end               = Column(Integer)
    biotype            = Column(String)
    canonical          = Column(Boolean)
    cdna_end           = Column(Integer)
    cdna_start         = Column(Integer)
    consequence_terms  = Column(String)
    eas_maf            = Column(String)
    exon               = Column(String)
    gene_id            = Column(String)
    gene_symbol        = Column(String)
    gene_symbol_source = Column(String)
    hgnc_id            = Column(Integer)
    impact             = Column(String)
    sas_maf            = Column(String)
    strand             = Column(Integer)
    transcript_id      = Column(String)
    variant_allele     = Column(String)

    


class Non_coding_transcript_variant(Base):
    __tablename__ = 'consequences'
    id                 = Column(Integer, primary_key=True)
    sample             = Column(String)
    pipeline           = Column(String) 
    variant_id         = Column(String)
    chrom              = Column(String) # v['seq_region_name'],
    start              = Column(Integer) 
    end                = Column(Integer)
    biotype            = Column(String)
    canonical          = Column(Boolean)
    cdna_end           = Column(Integer)
    cdna_start         = Column(Integer)
    consequence_terms  = Column(String)
    eas_maf            = Column(String)
    exon               = Column(String)
    gene_id            = Column(String)
    gene_symbol        = Column(String)
    gene_symbol_source = Column(String)
    hgnc_id            = Column(Integer)
    impact             = Column(String)
    intron             = Column(String)
    sas_maf            = Column(String)
    strand             = Column(Integer)
    transcript_id      = Column(String)
    variant_allele     = Column(String)


    


class Splice_region_variant(Base):
    __tablename__ = 'consequences'
    id                 = Column(Integer, primary_key=True)
    sample             = Column(String)
    pipeline           = Column(String) 
    variant_id         = Column(String)
    chrom              = Column(String) # v['seq_region_name'],
    start              = Column(Integer) 
    end                = Column(Integer)
    amino_acids        = Column(String)
    biotype            = Column(String)
    canonical          = Column(Boolean)
    ccds               = Column(String)
    cdna_end           = Column(Integer)
    cdna_start         = Column(Integer)
    cds_end            = Column(Integer)
    cds_start          = Column(Integer)
    codons             = Column(String)
    consequence_terms  = Column(String)
    domains            = Column(String)
    eas_maf            = Column(String)
    exon               = Column(String)
    gene_id            = Column(String)
    gene_symbol        = Column(String)
    gene_symbol_source = Column(String)
    hgnc_id            = Column(Integer)
    impact             = Column(String)
    intron             = Column(String)
    polyphen_prediction = Column(String)
    polyphen_score     = Column(Float)
    protein_end        = Column(Integer)
    protein_id         = Column(String)
    protein_start      = Column(Integer)
    sas_maf            = Column(String)
    sift_prediction    = Column(String)
    sift_score         = Column(Float)
    strand             = Column(Integer)
    swissprot          = Column(String)
    transcript_id      = Column(String)
    trembl             = Column(String)
    uniparc            = Column(String)
    variant_allele     = Column(String)



class Synonymous_variant(Base):
    __tablename__ = 'consequences'
    id                 = Column(Integer, primary_key=True)
    sample             = Column(String)
    pipeline           = Column(String) 
    variant_id         = Column(String)
    chrom              = Column(String) # v['seq_region_name'],
    start              = Column(Integer) 
    end                = Column(Integer)
    amino_acids        = Column(String)
    biotype            = Column(String)
    ccds               = Column(String)
    cdna_end           = Column(Integer)
    cdna_start         = Column(Integer)
    cds_end            = Column(Integer)
    cds_start          = Column(Integer)
    codons             = Column(String)
    consequence_terms  = Column(String)
    domains            = Column(String)
    eas_maf            = Column(String)
    exon               = Column(String)
    gene_id            = Column(String)
    gene_symbol        = Column(String)
    gene_symbol_source = Column(String)
    hgnc_id            = Column(Integer)
    impact             = Column(String)
    protein_end        = Column(Integer)
    protein_id         = Column(String)
    protein_start      = Column(Integer)
    sas_maf            = Column(String)
    strand             = Column(Integer)
    swissprot          = Column(String)
    transcript_id      = Column(String)
    trembl             = Column(String)
    uniparc            = Column(String)
    variant_allele     = Column(String)



    

class Upstream_gene_variant(Base):
    __tablename__ = 'consequences'
    id                 = Column(Integer, primary_key=True)
    sample             = Column(String)
    pipeline           = Column(String) 
    variant_id         = Column(String)
    chrom              = Column(String) # v['seq_region_name'],
    start              = Column(Integer) 
    end                = Column(Integer)
    biotype            = Column(String)
    canonical          = Column(Boolean)
    ccds               = Column(String)
    consequence_terms  = Column(String)
    distance           = Column(Integer)
    eas_maf            = Column(String)
    gene_id            = Column(String)
    gene_symbol        = Column(String)
    gene_symbol_source = Column(String)
    hgnc_id            = Column(Integer)
    impact             = Column(String)
    protein_id         = Column(String)
    sas_maf            = Column(String)
    strand             = Column(Integer)
    swissprot          = Column(String)
    transcript_id      = Column(String)
    trembl             = Column(String)
    uniparc            = Column(String)
    variant_allele     = Column(String)












##############################
# Void dictionaries for init #
##############################
void_Three_prime_UTR_variant = {
    sample             :
    pipeline           :
    variant_id         :
    chrom              :
    start              :
    end                :
    biotype            :
    canonical          :
    ccds               :
    cdna_end           :
    cdna_start         :
    consequence_terms  :
    eas_maf            :
    exon               :
    gene_id            :
    gene_symbol        :
    gene_symbol_source :
    hgnc_id            :
    impact             :
    protein_id         :
    sas_maf            :
    strand             :
    swissprot          :
    transcript_id      :
    trembl             :
    uniparc            :
    variant_allele     :
}
 
void_NMD_transcript_variant = {
    sample             :
    pipeline           :
    variant_id         :
    chrom              :
    start              :
    end                :
    amino_acids        :
    biotype            :
    canonical          :
    cdna_end           :
    cdna_start         :
    cds_end            :
    cds_start          :
    codons             :
    consequence_terms  :
    domains            :
    eas_maf            :
    exon               :
    gene_id            :
    gene_symbol        :
    gene_symbol_source :
    hgnc_id            :
    impact             :
    intron             :
    polyphen_prediction :
    polyphen_score     :
    protein_end        :
    protein_id         :
    protein_start      :
    sas_maf            :
    sift_prediction    :
    sift_score         :
    strand             :
    swissprot          :
    transcript_id      :
    trembl             :
    uniparc            :
    variant_allele     :
}



void_Downstream_gene_variant = {
    sample             :
    pipeline           :
    variant_id         :
    chrom              :
    start              :
    end                :
    biotype            :
    canonical          :
    ccds               :
    consequence_terms  :
    distance           :
    eas_maf            :
    gene_id            :
    gene_symbol        :
    gene_symbol_source :
    hgnc_id            :
    impact             :
    protein_id         :
    sas_maf            :
    strand             :
    swissprot          :
    transcript_id      :
    trembl             :
    uniparc            :
    variant_allele     :
        }

void_Intron_variant = {
    sample             :
    pipeline           :
    variant_id         :
    chrom              :
    start              :
    end                :
    biotype            :
    canonical          :
    ccds               :
    consequence_terms  :
    eas_maf            :
    gene_id            :
    gene_symbol        :
    gene_symbol_source :
    hgnc_id            :
    impact             :
    intron             :
    protein_id         :
    sas_maf            :
    strand             :
    swissprot          :
    transcript_id      :
    trembl             :
    uniparc            :
    variant_allele     :
}


    
void_Issense_variant = {
    sample            :
    pipeline          :
    variant_id        :
    chrom             :
    start             :
    end               :
    amino_acids        :
    biotype            :
    canonical          :
    ccds               :
    cdna_end           :
    cdna_start         :
    cds_end            :
    cds_start          :
    codons             :
    consequence_terms  :
    domains            :
    eas_maf            :
    exon               :
    gene_id            :
    gene_symbol        :
    gene_symbol_source :
    hgnc_id            :
    impact             :
    polyphen_prediction :
    polyphen_score     :
    protein_end        :
    protein_id         :
    protein_start      :
    sas_maf            :
    sift_prediction    :
    sift_score         :
    strand             :
    swissprot          :
    transcript_id      :
    trembl             :
    uniparc            :
    variant_allele     :
}

void_Non_coding_transcript_exon_variant = {
    sample            :
    pipeline          :
    variant_id        :
    chrom             :
    start             :
    end               :
    biotype            :
    canonical          :
    cdna_end           :
    cdna_start         :
    consequence_terms  :
    eas_maf            :
    exon               :
    gene_id            :
    gene_symbol        :
    gene_symbol_source :
    hgnc_id            :
    impact             :
    sas_maf            :
    strand             :
    transcript_id      :
    variant_allele     :
}
    


void_Non_coding_transcript_variant = {
    sample             :
    pipeline           :
    variant_id         :
    chrom              :
    start              :
    end                :
    biotype            :
    canonical          :
    cdna_end           :
    cdna_start         :
    consequence_terms  :
    eas_maf            :
    exon               :
    gene_id            :
    gene_symbol        :
    gene_symbol_source :
    hgnc_id            :
    impact             :
    intron             :
    sas_maf            :
    strand             :
    transcript_id      :
    variant_allele     :
}

    


void_Splice_region_variant = {
    sample             :
    pipeline           :
    variant_id         :
    chrom              :
    start              :
    end                :
    amino_acids        :
    biotype            :
    canonical          :
    ccds               :
    cdna_end           :
    cdna_start         :
    cds_end            :
    cds_start          :
    codons             :
    consequence_terms  :
    domains            :
    eas_maf            :
    exon               :
    gene_id            :
    gene_symbol        :
    gene_symbol_source :
    hgnc_id            :
    impact             :
    intron             :
    polyphen_prediction :
    polyphen_score     :
    protein_end        :
    protein_id         :
    protein_start      :
    sas_maf            :
    sift_prediction    :
    sift_score         :
    strand             :
    swissprot          :
    transcript_id      :
    trembl             :
    uniparc            :
    variant_allele     :
}


void_Synonymous_variant = {
    sample             :
    pipeline           :
    variant_id         :
    chrom              :
    start              :
    end                :
    amino_acids        :
    biotype            :
    ccds               :
    cdna_end           :
    cdna_start         :
    cds_end            :
    cds_start          :
    codons             :
    consequence_terms  :
    domains            :
    eas_maf            :
    exon               :
    gene_id            :
    gene_symbol        :
    gene_symbol_source :
    hgnc_id            :
    impact             :
    protein_end        :
    protein_id         :
    protein_start      :
    sas_maf            :
    strand             :
    swissprot          :
    transcript_id      :
    trembl             :
    uniparc            :
    variant_allele     :
}
