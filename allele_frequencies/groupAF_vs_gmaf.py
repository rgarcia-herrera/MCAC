import vcf
import os
from pprint import pprint
from haloplex_symbols import symbol
from samples import vep_complete as vcf_probands

def freq_from_maf(MAF):
    try:
        (allele,freq) = MAF.split('&')[0].split(":")
        return float(freq) 
    except:
        return 0



def low_freq(GMAF,AFR_MAF,AMR_MAF,ASN_MAF,EAS_MAF,EUR_MAF,SAS_MAF,AA_MAF,EA_MAF):
    if float(GMAF) > 0.01:
        return False
    elif AFR_MAF and freq_from_maf(AFR_MAF) > 0.01:
        return False
    elif AMR_MAF and freq_from_maf(AMR_MAF) > 0.01:
        return False
    elif ASN_MAF and freq_from_maf(ASN_MAF) > 0.01:
        return False
    elif EAS_MAF and freq_from_maf(EAS_MAF) > 0.01:
        return False
    elif EUR_MAF and freq_from_maf(EUR_MAF) > 0.01:
        return False
    elif SAS_MAF and freq_from_maf(SAS_MAF) > 0.01:
        return False
    elif AA_MAF and freq_from_maf(AA_MAF) > 0.01:
        return False
    elif EA_MAF and freq_from_maf(EA_MAF) > 0.01:
        return False
    else:
        return True

variants = {}
samples = set()
for path in vcf_probands:
    with open(path) as f:
        vcfr = vcf.Reader(f)
        sample = "s_%s" % vcfr.samples[0]
        samples.add(sample)

        for v in vcfr:
            if 'CSQ' in v.INFO:
                for csq in v.INFO['CSQ']:
                    (Allele,Consequence,IMPACT,SYMBOL,Gene,Feature_type,Feature,
                     BIOTYPE,EXON,INTRON,HGVSc,HGVSp,cDNA_position,CDS_position,
                     Protein_position,Amino_acids,Codons,Existing_variation,DISTANCE,
                     STRAND,VARIANT_CLASS,SYMBOL_SOURCE,HGNC_ID,CANONICAL,TSL,CCDS,
                     ENSP,SWISSPROT,TREMBL,UNIPARC,SIFT,PolyPhen,DOMAINS,GMAF,
                     AFR_MAF,AMR_MAF,ASN_MAF,EAS_MAF,EUR_MAF,SAS_MAF,AA_MAF,EA_MAF,
                     CLIN_SIG,SOMATIC,PHENO,PUBMED,MOTIF_NAME,MOTIF_POS,HIGH_INF_POS,MOTIF_SCORE_CHANGE) = csq.split('|')

                    chrom = v.CHROM
                    if chrom.find('chr') == -1:
                        chrom = 'chr' + chrom
                    
                    if not GMAF:
                        GMAF = 'N.D.'
                        gmaf = 0
                    else:
                        gmaf = freq_from_maf(GMAF)
                        
                    if low_freq(gmaf,AFR_MAF,AMR_MAF,ASN_MAF,EAS_MAF,EUR_MAF,SAS_MAF,AA_MAF,EA_MAF) \
                       and PolyPhen.startswith('p') \
                       and SIFT.startswith('d'):
                        vkey = "%s:%s_%s/%s" % (chrom,v.POS,v.REF,v.ALT)
                        if not vkey in variants:
                            variants[vkey] = {'symbol'  : SYMBOL,
                                          'existing': Existing_variation,
                                          'Protein_position' : Protein_position,
                                          'Amino_acids' : Amino_acids,
                                          'gmaf'    : GMAF,
                                          'AFR_MAF' : AFR_MAF,
                                          'AMR_MAF' : AMR_MAF,
                                          'ASN_MAF' : ASN_MAF,
                                          'EAS_MAF' : EAS_MAF,
                                          'EUR_MAF' : EUR_MAF,
                                          'SAS_MAF' : SAS_MAF,
                                          'AA_MAF'  : AA_MAF,
                                          'EA_MAF'  : EA_MAF,
                                          'het'     : set(),
                                          'hom'     : set(),
                                          'Allele' : Allele,
                                          'Consequence' : Consequence,
                                          'IMPACT' : IMPACT,
                                          'Gene' : Gene,
                                          'Feature_type': Feature,
                                          'BIOTYPE' : BIOTYPE,
                                          'EXON' : EXON,
                                          'INTRON' : INTRON,
                                          'HGVSc' : HGVSc,
                                          'HGVSp' : HGVSp,
                                          'cDNA_position' : cDNA_position,
                                          'CDS_position' : CDS_position,
                                          'Codons': Codons,
                                          'DISTANCE': DISTANCE,
                                          'STRAND': STRAND,
                                          'VARIANT_CLASS': VARIANT_CLASS,
                                          'SYMBOL_SOURCE': SYMBOL_SOURCE,
                                          'HGNC_ID': HGNC_ID,
                                          'CANONICAL': CANONICAL,
                                          'TSL': TSL,
                                          'CCDS': CCDS,
                                          'ENSP': ENSP,
                                          'SWISSPROT': SWISSPROT,
                                          'TREMBL': TREMBL,
                                          'UNIPARC': UNIPARC,
                                          'SIFT': SIFT,
                                          'PolyPhen': PolyPhen,
                                          'DOMAINS': DOMAINS,
                                          'CLIN_SIG': CLIN_SIG,
                                          'SOMATIC': SOMATIC,
                                          'PHENO': PHENO,
                                          'PUBMED': PUBMED,
                                          'MOTIF_NAME': MOTIF_NAME,
                                          'MOTIF_POS': MOTIF_POS,
                                          'HIGH_INF_POS': HIGH_INF_POS,
                                          'MOTIF_SCORE_CHANGE': MOTIF_SCORE_CHANGE
                                      }

                        if v.num_het == 0:
                            variants[vkey]['hom'].add(sample)
                        else:
                            variants[vkey]['het'].add(sample)

samples = list(samples)

print ";".join(["vkey","existing",'Protein_position','Amino_acids',
                'Allele', 'Consequence', 'IMPACT', 'Gene', 'Feature_type', 'BIOTYPE', 'EXON', 'INTRON',
                'HGVSc', 'HGVSp', 'cDNA_position', 'CDS_position', 'Codons', 'DISTANCE', 'STRAND',
                'VARIANT_CLASS', 'SYMBOL_SOURCE', 'HGNC_ID', 'CANONICAL', 'TSL', 'CCDS', 'ENSP',
                'SWISSPROT', 'TREMBL', 'UNIPARC', 'SIFT', 'PolyPhen', 'DOMAINS', 'CLIN_SIG', 'SOMATIC',
                'PHENO', 'PUBMED', 'MOTIF_NAME', 'MOTIF_POS', 'HIGH_INF_POS', 'MOTIF_SCORE_CHANGE', 
                'symbol',
                "gmaf",'AFR_MAF','AMR_MAF','ASN_MAF','EAS_MAF','EUR_MAF','SAS_MAF','AA_MAF','EA_MAF',
                "het","hom","het_count", "hom_count"]+samples)

for v in variants:
    
    row = [v,
           variants[v]['existing'],
           variants[v]['Protein_position'],           
           variants[v]['Amino_acids'],
           variants[v]['Allele'],
           variants[v]['Consequence'],
           variants[v]['IMPACT'],
           variants[v]['Gene'],
           variants[v]['Feature_type'],
           variants[v]['BIOTYPE'],
           variants[v]['EXON'],
           variants[v]['INTRON'],
           variants[v]['HGVSc'],
           variants[v]['HGVSp'],
           variants[v]['cDNA_position'],
           variants[v]['CDS_position'],
           variants[v]['Codons'],
           variants[v]['DISTANCE'],
           variants[v]['STRAND'],
           variants[v]['VARIANT_CLASS'],
           variants[v]['SYMBOL_SOURCE'],
           variants[v]['HGNC_ID'],
           variants[v]['CANONICAL'],
           variants[v]['TSL'],
           variants[v]['CCDS'],
           variants[v]['ENSP'],
           variants[v]['SWISSPROT'],
           variants[v]['TREMBL'],
           variants[v]['UNIPARC'],
           variants[v]['SIFT'],
           variants[v]['PolyPhen'],
           variants[v]['DOMAINS'],
           variants[v]['CLIN_SIG'],
           variants[v]['SOMATIC'],
           variants[v]['PHENO'],
           variants[v]['PUBMED'],
           variants[v]['MOTIF_NAME'],
           variants[v]['MOTIF_POS'],
           variants[v]['HIGH_INF_POS'],
           variants[v]['MOTIF_SCORE_CHANGE'],
           variants[v]['symbol'],
           variants[v]['gmaf'],
           variants[v]['AFR_MAF'],
           variants[v]['AMR_MAF'],
           variants[v]['ASN_MAF'],
           variants[v]['EAS_MAF'],
           variants[v]['EUR_MAF'],
           variants[v]['SAS_MAF'],
           variants[v]['AA_MAF'],
           variants[v]['EA_MAF'],
           ",".join(variants[v]['het']),
           ",".join(variants[v]['hom']),
           str(len(variants[v]['het'])),
           str(len(variants[v]['hom']))]

    for s in samples:
        if s in variants[v]['het']:
            alleles = '1'
        elif s in variants[v]['hom']:
            alleles = '2'
        else:
            alleles = '0'
        row.append(alleles)
    print ";".join(row)
              
