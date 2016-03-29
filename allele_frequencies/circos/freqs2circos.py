import argparse
import sys
import csv

parser = argparse.ArgumentParser(description='create circos compatible file from freqs file')

parser.add_argument('freqs',  type=argparse.FileType('r'), help="frequencies table")
args = parser.parse_args()

reader = csv.DictReader(args.freqs, delimiter=';')


def write_af(f, chrom, pos, af):
    try:
        freq = af.split("&")[0].split(":")[1]
        f.write( " ".join(["hs"+chrom, str(pos), str(pos+1), freq])+"\n")
    except:
        pass

with open('cohort_af.tsv','w') as cohort_af, \
     open('gm_af.tsv', 'w') as gm_af, \
     open('AFR_MAF.tsv', 'w') as afr_maf, \
     open('AMR_MAF.tsv', 'w') as amr_maf, \
     open('EAS_MAF.tsv', 'w') as eas_maf, \
     open('EUR_MAF.tsv', 'w') as eur_maf, \
     open('SAS_MAF.tsv', 'w') as sas_maf, \
     open('AA_MAF.tsv', 'w') as aa_maf, \
     open('EA_MAF.tsv', 'w') as ea_maf :
    for v in reader:
        vkey = v['vkey']
        try:
            (chrom, etc) = vkey.split(':')
        except:
            pass
        chrom = chrom.strip('chr')
        pos = int(etc.split('_')[0])

        
        N = len( v.keys() ) - 18
        cohortaf = (int(v['het_count']) + (int(v['hom_count']) * 2) ) / float(N)
        cohort_af.write( " ".join(["hs"+chrom, str(pos), str(pos+1), "%s" % cohortaf]) + "\n")

        write_af(gm_af,   chrom, pos, v['gmaf'])
        write_af(afr_maf, chrom, pos, v['AFR_MAF'])
        write_af(amr_maf, chrom, pos, v['AMR_MAF'])
        write_af(eas_maf, chrom, pos, v['EAS_MAF'])
        write_af(eur_maf, chrom, pos, v['EUR_MAF'])
        write_af(sas_maf, chrom, pos, v['SAS_MAF'])
        write_af(aa_maf,  chrom, pos, v['AA_MAF'])
        write_af(ea_maf,  chrom, pos, v['EA_MAF'])
        
