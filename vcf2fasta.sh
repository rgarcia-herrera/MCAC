#!/bin/bash

GATK=/export/home/rgarcia/software/GenomeAnalysisTK.jar

REF=/export/home/rgarcia/reference/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFASTA/genome.fa
BED=/export/home/rgarcia/MCAC/targets/Miocardiopatias_y_canalopatias_Amplicons.bed

DIR=/export/home/rgarcia/MCAC/vcf_basespace

VCFS="S01_sorted.vcf
S02_sorted.vcf
S03_sorted.vcf
S04_sorted.vcf
S05_sorted.vcf
S06_sorted.vcf
S07_sorted.vcf
S08_sorted.vcf
S09_sorted.vcf
S10_sorted.vcf
S11_sorted.vcf
S12_sorted.vcf
S13_sorted.vcf
S14_sorted.vcf
S15_sorted.vcf
S16_sorted.vcf
S17_sorted.vcf
S18_sorted.vcf
S19_sorted.vcf
S20_sorted.vcf
S21_sorted.vcf
S22_sorted.vcf
S23_sorted.vcf
S24_sorted.vcf
S25_sorted.vcf
S26_sorted.vcf
S27_sorted.vcf
S28_sorted.vcf
S29_sorted.vcf
S30_sorted.vcf
S31_sorted.vcf
S32_sorted.vcf
S33_sorted.vcf
S34_sorted.vcf
S35_sorted.vcf
S36_sorted.vcf
S37_sorted.vcf
S38_sorted.vcf
S39_sorted.vcf
S40_sorted.vcf
S41_sorted.vcf
S42_sorted.vcf
S43_sorted.vcf
S44_sorted.vcf
S45_sorted.vcf
S46_sorted.vcf
S47_sorted.vcf
S48_sorted.vcf"

for VCF in $VCFS
do
    FASTA=`basename $VCF .vcf`.fasta
    java -jar $GATK \
         -T FastaAlternateReferenceMaker \
         -R $REF \
         -o $DIR/$FASTA \
         -L $BED \
         -V $DIR/$VCF
done
