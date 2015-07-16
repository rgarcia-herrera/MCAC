#!/bin/bash

DIR=/export/home/rgarcia/MCAC/sam_miseq_hg19
GATK=/export/home/rgarcia/software/GenomeAnalysisTK.jar
REF=/export/home/rgarcia/MCAC/reference/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFASTA/genome.fa
KNOWN=/export/home/rgarcia/MCAC/reference/1000G_phase1.indels.b37.vcf.gz

SAMS="/export/home/rgarcia/MCAC/sam_miseq_hg19/S01.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S02.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S03.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S04.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S05.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S06.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S07.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S08.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S09.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S10.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S11.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S12.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S13.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S14.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S15.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S16.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S17.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S18.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S19.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S20.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S21.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S22.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S23.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S24.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S25.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S26.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S27.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S28.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S29.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S30.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S31.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S32.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S33.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S34.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S35.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S36.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S37.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S38.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S39.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S40.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S41.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S42.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S43.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S44.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S45.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S46.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S47.bam
/export/home/rgarcia/MCAC/sam_miseq_hg19/S48.bam"

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
