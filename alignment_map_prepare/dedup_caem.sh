#!/bin/bash

DEDUP="java -jar /home/rgarcia/downloads/picard-tools-1.121/MarkDuplicates.jar"

DIR=/home/rgarcia/MCAC/sam/exm_caem_fvi_rigo

for SAMPLE in $(seq -f "%02g" 1 17)           
do
    $DEDUP REMOVE_DUPLICATES=true I=$DIR/S${SAMPLE}_rg.bam O=$DIR/${SAMPLE}_rg_dedup.bam M=$DIR/${SAMPLE}.dedup_metrics
done
