#!/bin/bash

DIR=/export/home/rgarcia/MCAC/sam_miseq_hg19
GATK=/export/home/rgarcia/software/GenomeAnalysisTK.jar
REF=/export/home/rgarcia/MCAC/reference/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFASTA/genome.fa
KNOWN=/export/home/rgarcia/MCAC/reference/1000G_phase1.indels.b37.vcf.gz

SAMS="/export/home/rgarcia/MCAC/sam_miseq_hg19/S01_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S02_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S03_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S04_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S05_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S06_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S07_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S08_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S09_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S10_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S11_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S12_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S13_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S14_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S15_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S16_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S17_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S18_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S19_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S20_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S21_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S22_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S23_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S24_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S25_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S26_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S27_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S28_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S29_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S30_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S31_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S32_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S33_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S34_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S35_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S36_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S37_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S38_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S39_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S40_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S41_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S42_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S43_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S44_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S45_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S46_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S47_rg.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S48_rg.bam"

for SAM in $SAMS
do
    INTERVALS=$DIR/`basename $SAM .bam`.intervals
    echo "creating intervals file"
    echo $INTERVALS
    java -Xmx1g -jar $GATK \
         -T RealignerTargetCreator \
         -R $REF \
         -I $SAM \
         --known $KNOWN \
         -dt NONE \
         -o $INTERVALS

    echo "realigning"
    BAMOUT=$DIR/`basename $SAM .bam`_realigned.bam
    java -jar $GATK \
         -T IndelRealigner \
         -R $REF \
         -I $SAM \
         -dt NONE \
         -targetIntervals $INTERVALS \
         -o $BAMOUT

done
