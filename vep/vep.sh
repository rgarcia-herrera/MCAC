#!/bin/bash

VEP=/home/rgarcia/downloads/ensembl-tools-release-81/scripts/variant_effect_predictor/variant_effect_predictor.pl

VCFDIR=/home/rgarcia/MCAC/vcf


# for SAMPLE in $(seq -f "%02g" 1 48)
# do
#     for BATCH in {500,}
#     do
#         $VEP -i $VCFDIR/$BATCH/S${SAMPLE}.norepeats.vcf -o $VCFDIR/$BATCH/S${SAMPLE}.vep.csv --everything --fork 30 --offline --assembly GRCh37
#     done
# done



COMPLETE_VCF="family_filtered_PTLiJATEiJIAT-JPAMuLACA.vcf
family_filtered_PTLiJATE-JPAMuLACA.vcf
family_filtered_PTLiJATEiJIAT.vcf
family_filtered_PTLiJATE.vcf"

for VCF in $COMPLETE_VCF
do
    OUT=`basename $VCF .vcf`
    $VEP -i $VCFDIR/complete/$VCF -o $VCFDIR/complete/${OUT}.vep.csv --everything --fork 30 --offline --assembly GRCh37    
done


# EXM_ILLUMINA_VCF="family_filtered_JLRLiJLRMiGEL_con_alelos.vcf
# family_filtered_JLRMiYRM_con_alelos.vcf
# family_filtered_JLRLiJLRMiGEL_sin_alelos.vcf
# family_filtered_JLRMiYRM_sin_alelos.vcf"

# EXM_ILLUMINA_VCF="LMG.vcf
# JLRM.vcf
# YRN.vcf"
# # DLA.vcf
# # GEL.vcf
# # GMCA.vcf
# # JLRL.vcf
# # PTL.vcf
# # LMG.vcf"

# for VCF in $EXM_ILLUMINA_VCF
# do
#     OUT=`basename $VCF .vcf`
#     $VEP --force_overwrite -i $VCFDIR/exm_illumina/$VCF -o $VCFDIR/exm_illumina/${OUT}.vep.csv --everything --fork 30 --offline --assembly GRCh37    
# done



#for SAMPLE in $(seq -f "%02g" 1 11)
#do
#    $VEP -i $VCFDIR/caem_fvi_rigo/S${SAMPLE}.vcf -o $VCFDIR/caem_fvi_rigo/S${SAMPLE}.vep.csv --everything --fork 30 --offline --assembly GRCh37
#done
