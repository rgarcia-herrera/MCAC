import csv
import argparse

from pprint import pprint

parser = argparse.ArgumentParser(description="Unfold VEP's extra field to create regular CSV files")
parser.add_argument('vep', type=argparse.FileType('r'))
# parser.add_argument('--csv', type=argparse.FileType('w'), required=True )
args   = parser.parse_args()


extras = { 'IMPACT': '-',
           'VARIANT_CLASS': '-',
           'SYMBOL': '-',
           'SYMBOL_SOURCE': '-',
           'STRAND': '-',
           'ENSP': '-',
           'SWISSPROT': '-',
           'TREMBL': '-',
           'UNIPARC': '-',
           'HGVSc': '-',
           'HGVSp': '-',
           'HGVS_OFFSET': '-',
           'SIFT': '-',
           'PolyPhen': '-',
           'MOTIF_NAME': '-',
           'MOTIF_POS': '-',
           'HIGH_INF_POS': '-',
           'MOTIF_SCORE_CHANGE': '-',
           'CELL_TYPE': '-',
           'CANONICAL': '-',
           'CCDS': '-',
           'INTRON': '-',
           'EXON': '-',
           'DOMAINS': '-',
           'DISTANCE': '-',
           'IND': '-',
           'ZYG': '-',
           'SV': '-',
           'FREQS': '-',
           'GMAF': '-',
           'AFR_MAF': '-',
           'AMR_MAF': '-',
           'ASN_MAF': '-',
           'EUR_MAF': '-',
           'EAS_MAF': '-',
           'SAS_MAF': '-',
           'AA_MAF': '-',
           'EA_MAF': '-',
           'CLIN_SIG': '-',
           'BIOTYPE': '-',
           'TSL': '-',
           'PUBMED': '-',
           'SOMATIC': '-',
           'PHENO': '-',
           'ALLELE_NUM': '-',
           'MINIMISED': '-',
           'PICK': '-',
           'REFSEQ_MATCH': '-' }




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
            
        for e in extraslist:
            (k,v) = e.split('=')
            extras[k] = v

        if extras['CLIN_SIG'].find("pathogenic") != -1: 
            print "\t".join(l[:-1] + [ extras['IMPACT'],
                                   extras['VARIANT_CLASS'],
                                   extras['SYMBOL'],
                                   extras['SYMBOL_SOURCE'],
                                   extras['STRAND'],
                                   extras['ENSP'],
                                   extras['SWISSPROT'],
                                   extras['TREMBL'],
                                   extras['UNIPARC'],
                                   extras['HGVSc'],
                                   extras['HGVSp'],
                                   extras['HGVS_OFFSET'],
                                   extras['SIFT'],
                                   extras['PolyPhen'],
                                   extras['MOTIF_NAME'],
                                   extras['MOTIF_POS'],
                                   extras['HIGH_INF_POS'],
                                   extras['MOTIF_SCORE_CHANGE'],
                                   extras['CELL_TYPE'],
                                   extras['CANONICAL'],
                                   extras['CCDS'],
                                   extras['INTRON'],
                                   extras['EXON'],
                                   extras['DOMAINS'],
                                   extras['DISTANCE'],
                                   extras['IND'],
                                   extras['ZYG'],
                                   extras['SV'],
                                   extras['FREQS'],
                                   extras['GMAF'],
                                   extras['AFR_MAF'],
                                   extras['AMR_MAF'],
                                   extras['ASN_MAF'],
                                   extras['EUR_MAF'],
                                   extras['EAS_MAF'],
                                   extras['SAS_MAF'],
                                   extras['AA_MAF'],
                                   extras['EA_MAF'],
                                   extras['CLIN_SIG'],
                                   extras['BIOTYPE'],
                                   extras['TSL'],
                                   extras['PUBMED'],
                                   extras['SOMATIC'],
                                   extras['PHENO'],
                                   extras['ALLELE_NUM'],
                                   extras['MINIMISED'],
                                   extras['PICK'],
                                   extras['REFSEQ_MATCH']])
