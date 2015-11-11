#!/bin/bash

DIR=/home/rgarcia/MCAC/sam
GATK=/home/rgarcia/downloads/GenomeAnalysisTK.jar
REF=/home/rgarcia/MCAC/reference/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFASTA/genome.fa
KNOWN=/home/rgarcia/MCAC/reference/1000G_phase1.indels.b37.vcf.gz


for SAMPLE in $(seq -f "%02g" 17 26)
do
    INTERVALS=$DIR/mau29/S${SAMPLE}.intervals
    SAM=$DIR/mau29/S${SAMPLE}_rg.bam

    # echo "creating intervals file"
    # echo $INTERVALS
    # java -Xmx1g -jar $GATK \
    #      -T RealignerTargetCreator \
    #      -R $REF \
    #      -I $SAM \
    #      --known $KNOWN \
    #      -dt NONE \
    #      -o $INTERVALS &

    echo "realigning"
    BAMOUT=$DIR/mau29/S${SAMPLE}_realigned.bam
    java -jar $GATK \
         -T IndelRealigner \
         -R $REF \
         -I $SAM \
         -dt NONE \
         -targetIntervals $INTERVALS \
         -o $BAMOUT &
done

