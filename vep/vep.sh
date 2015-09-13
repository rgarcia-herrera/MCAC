#!/bin/bash

VEP=/home/rgarcia/downloads/ensembl-tools-release-81/scripts/variant_effect_predictor/variant_effect_predictor.pl

VCFDIR=/home/rgarcia/MCAC/vcf




# for SAMPLE in $(seq -f "%02g" 1 48)
# do
#     for BATCH in {300,500,300et500}
#     do
#         $VEP -i $VCFDIR/$BATCH/S${SAMPLE}.norepeats.vcf --json -o $VCFDIR/$BATCH/S${SAMPLE}.vep.json --everything --fork 30 --offline --assembly GRCh37
#     done
# done





COMPLETE_VCF="family_filtered_PTLiJATEiJIAT-JPAMuLACA_con_alelos.vcf
family_filtered_PTLiJATEiJIAT-JPAMuLACA_sin_alelos.vcf
family_filtered_PTLiJATE-JPAMuLACA_con_alelos.vcf
family_filtered_PTLiJATE-JPAMuLACA_sin_alelos.vcf"

for VCF in $COMPLETE_VCF
do
    OUT=`basename $VCF .vcf`
    $VEP -i $VCFDIR/complete/$VCF --json -o $VCFDIR/complete/${OUT}.vep.json --everything --fork 30 --offline --assembly GRCh37    
done
