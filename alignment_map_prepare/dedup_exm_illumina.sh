#!/bin/bash

DEDUP="java -jar /home/rgarcia/downloads/picard-tools-1.121/MarkDuplicates.jar"
DIR=/home/rgarcia/MCAC/sam/exm_illumina

EXM_ILLUMINA="DLA
GEL
GMCA
JLRL
JLRM
LMG
PTL
YRN"

for SAMPLE in $EXM_ILLUMINA
do
    $DEDUP REMOVE_DUPLICATES=true I=$DIR/${SAMPLE}_rg.bam O=$DIR/${SAMPLE}_rg_dedup.bam M=$DIR/${SAMPLE}.dedup_metrics
done
