"""This script will take the output of groupAF_vs_gmaf.py and add
annotations from a local cache of the RVS in a mongo db.

Input should have the following format, separated by ';':

    "vkey";"symbol";"existing";"gmaf";"het";"hom";"het_count";"hom_count"

TODO: Everything, for now it just counts the annotations from the
*hardcoded* file freqs.csv
"""

import csv
from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017")
db=client['rvs_annotations']
c=db['cache']

ks = set()
n=0
with open('freqs.csv') as f:
    reader = csv.reader(f, delimiter=';')
    # print csv header
    print ";".join(reader.next() + [ u'esp6500_aa_af',
                                     u'esp6500_af',
                                     u'esp6500_ea_af',
                                     u'exac_af',
                                     u'exac_afr_af',
                                     u'exac_amr_af',
                                     u'exac_eas_af',
                                     u'exac_eur_af',
                                     u'exac_fin_af',
                                     u'exac_sas_af',
                                     u'gera_control_af',
                                     u'tgp2_af',
                                     u'tgp2_afr_af',
                                     u'tgp2_amr_af',
                                     u'tgp2_asn_af',
                                     u'tgp2_eur_af',
                                     u'tgp2_san_af',
                                     u'tgp_af',
                                     u'uk10k_control_af',
                                     u'wellderly_af',])

    
    for v in reader:
        vkey = v[0]
        (pos, alleles) = vkey.split('_')
        (chrom, start) = pos.split(':')
        chrom = chrom.strip('chr')
        (ref, alt) = alleles.split('/')
        alt = alt.strip("[]")

        # find annotation for variant in local cache
        ann = c.find({
            'chr'      : chrom,
            'start'    : start,
            'ref'      : ref,
            'alt'      : alt,
            })

        if ann.count() == 0:
            row = v + ['-' for n in range(20)]
        else:
            for a in ann:
                row = v + [ a.get(u'esp6500_aa_af',u''),
                            a.get(u'esp6500_af',u''),
                            a.get(u'esp6500_ea_af',u''),
                            a.get(u'exac_af',u''),
                            a.get(u'exac_afr_af',u''),
                            a.get(u'exac_amr_af',u''),
                            a.get(u'exac_eas_af',u''),
                            a.get(u'exac_eur_af',u''),
                            a.get(u'exac_fin_af',u''),
                            a.get(u'exac_sas_af',u''),
                            a.get(u'gera_control_af',u''),
                            a.get(u'tgp2_af',u''),
                            a.get(u'tgp2_afr_af',u''),
                            a.get(u'tgp2_amr_af',u''),
                            a.get(u'tgp2_asn_af',u''),
                            a.get(u'tgp2_eur_af',u''),
                            a.get(u'tgp2_san_af',u''),
                            a.get(u'tgp_af',u''),
                            a.get(u'uk10k_control_af',u''),
                            a.get(u'wellderly_af',u'')]
            
        print ";".join(['-' if not r else r for r in row])
