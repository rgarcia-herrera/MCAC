#!/bin/bash

DIR=/home/rgarcia/MCAC
BWA=/home/rgarcia/downloads/bwa.kit/bwa
REF=$DIR/reference/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFASTA/genome.fa


for SAMPLE in {06,26}
do
    R1=$DIR/fastq/gea/S${SAMPLE}_R1.fastq.gz
    R2=$DIR/fastq/gea/S${SAMPLE}_R2.fastq.gz
    SAMOUT=$DIR/sam/gea/S${SAMPLE}.sam
    $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT
done
