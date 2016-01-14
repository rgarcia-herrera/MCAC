import csv
import argparse

from pprint import pprint

parser = argparse.ArgumentParser(description="Unfold VEP's extra field to create regular CSV files")
parser.add_argument('vep', type=argparse.FileType('r'))
args   = parser.parse_args()

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

        if (extras.get('IMPACT','-') == 'HIGH') \
           or (l[6] == 'frameshift_variant') \
           or (extras.get('CLIN_SIG','-').find("pathogenic") != -1 ) \
           or (extras.get('SIFT','-').find("deleterious") != -1 and extras.get('PolyPhen','-').startswith('p')):
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
                                   extras.get('REFSEQ_MATCH','-')
                                   ])
