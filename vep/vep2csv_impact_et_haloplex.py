import csv
import argparse

from pprint import pprint

parser = argparse.ArgumentParser(description="Unfold VEP's extra field to create regular CSV files")
parser.add_argument('vep', type=argparse.FileType('r'))
# parser.add_argument('--csv', type=argparse.FileType('w'), required=True )
args   = parser.parse_args()


haloplex_genes = ['ABCC8', 'ABCC9','ACTC1','ACTN2','AKAP9','ANK2','ANKRD1','BAG3','CACNA1C','CACNA2D1','CACNB2','CALM1',
                  'CALR3','CAMK2A','CASQ2','CAV3','CSRP3','DES','DLG1','DPP6','DSC2','DSG2','DTNA','FGF12','GJA5','GJD4',
                  'GLA','GPD1L','HCN4','HEY2','JUP','KCNA5','KCND3','KCNE1','KCNE1L','KCNE2','KCNE3','KCNH2','KCNJ2',
                  'KCNJ5','KCNJ8','KCNQ1','LAMP2','LDB3','LMNA','MYBPC3','MYH6','MYH7','MYL2','MYL3','MYLK2','MYOZ2',
                  'MYPN','NEXN','NOS1AP','PKP2','PLN','PRKAG2','RANGRF','RYR2','SCN10A','SCN1B','SCN2B','SCN3B','SCN4B','SCN5A',
                  'SLMAP','SNTA1','TAZ','TCAP','TGFB3','TMEM43','TNNC1','TNNI3','TNNT2','TPM1','TRDN','TRPM4','TTN','TTR','VCL',]


print "\t".join( ["Uploaded_variation", "Location", "Allele", "Gene", "Feature", "Feature_type",
                  "Consequence", "cDNA_position", "CDS_position", "Protein_position", "Amino_acids", "Codons",
                  "colocated_variation",  'IMPACT', 'VARIANT_CLASS', 'SYMBOL', 'SYMBOL_SOURCE', 'STRAND', 'ENSP',
                  'SWISSPROT', 'TREMBL', 'UNIPARC', 'HGVSc', 'HGVSp', 'HGVS_OFFSET', 'SIFT', 'PolyPhen', 'MOTIF_NAME',
                  'MOTIF_POS', 'HIGH_INF_POS', 'MOTIF_SCORE_CHANGE', 'CELL_TYPE', 'CANONICAL', 'CCDS', 'INTRON',
                  'EXON', 'DOMAINS', 'DISTANCE', 'IND', 'ZYG', 'SV', 'FREQS', 'GMAF', 'AFR_MAF', 'AMR_MAF', 'ASN_MAF',
                  'EUR_MAF', 'EAS_MAF', 'SAS_MAF', 'AA_MAF', 'EA_MAF', 'CLIN_SIG', 'BIOTYPE', 'TSL', 'PUBMED',
                  'SOMATIC', 'PHENO', 'ALLELE_NUM', 'MINIMISED', 'PICK', 'REFSEQ_MATCH',])



csvr = csv.reader( args.vep, delimiter='\t' )
for l in csvr:
    if not l[0].startswith('#'):
        Extra = l[-1]
        extraslist = Extra.split(';')
        extras = dict()
        for e in extraslist:
            (k,v) = e.split('=')
            extras[k] = v

        if extras.get('IMPACT','-') == 'HIGH' and extras.get('SYMBOL','-') in haloplex_genes:
            print "\t".join(l[:-1] + [ extras.get('IMPACT','-'),
                                   extras.get('VARIANT_CLASS','-'),
                                   extras.get('SYMBOL','-'),
                                   extras.get('SYMBOL_SOURCE','-'),
                                   extras.get('STRAND','-'),
                                   extras.get('ENSP','-'),
                                   extras.get('SWISSPROT','-'),
                                   extras.get('TREMBL','-'),
                                   extras.get('UNIPARC','-'),
                                   extras.get('HGVSc','-'),
                                   extras.get('HGVSp','-'),
                                   extras.get('HGVS_OFFSET','-'),
                                   extras.get('SIFT','-'),
                                   extras.get('PolyPhen','-'),
                                   extras.get('MOTIF_NAME','-'),
                                   extras.get('MOTIF_POS','-'),
                                   extras.get('HIGH_INF_POS','-'),
                                   extras.get('MOTIF_SCORE_CHANGE','-'),
                                   extras.get('CELL_TYPE','-'),
                                   extras.get('CANONICAL','-'),
                                   extras.get('CCDS','-'),
                                   extras.get('INTRON','-'),
                                   extras.get('EXON','-'),
                                   extras.get('DOMAINS','-'),
                                   extras.get('DISTANCE','-'),
                                   extras.get('IND','-'),
                                   extras.get('ZYG','-'),
                                   extras.get('SV','-'),
                                   extras.get('FREQS','-'),
                                   extras.get('GMAF','-'),
                                   extras.get('AFR_MAF','-'),
                                   extras.get('AMR_MAF','-'),
                                   extras.get('ASN_MAF','-'),
                                   extras.get('EUR_MAF','-'),
                                   extras.get('EAS_MAF','-'),
                                   extras.get('SAS_MAF','-'),
                                   extras.get('AA_MAF','-'),
                                   extras.get('EA_MAF','-'),
                                   extras.get('CLIN_SIG','-'),
                                   extras.get('BIOTYPE','-'),
                                   extras.get('TSL','-'),
                                   extras.get('PUBMED','-'),
                                   extras.get('SOMATIC','-'),
                                   extras.get('PHENO','-'),
                                   extras.get('ALLELE_NUM','-'),
                                   extras.get('MINIMISED','-'),
                                   extras.get('PICK','-'),
                                   extras.get('REFSEQ_MATCH','-') ])
