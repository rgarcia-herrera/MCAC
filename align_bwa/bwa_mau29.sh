#!/bin/bash

DIR=/home/rgarcia/MCAC
BWA=/home/rgarcia/downloads/bwa.kit/bwa
REF=$DIR/reference/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFASTA/genome.fa


for SAMPLE in $(seq -f "%02g" 17 26)
do
    R1=$DIR/fastq/mau29/S${SAMPLE}.fastq.gz
    SAMOUT=$DIR/sam/mau29/S${SAMPLE}.sam
    $BWA mem -M -t 30 $REF $R1 > $SAMOUT
done

