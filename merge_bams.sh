#!/bin/bash

DIR=/home/rgarcia/MCAC

for SAMPLE in $(seq -f "%02g" 1 48)
do
    IN300=$DIR/sam/300/S${SAMPLE}_realigned.bam
    IN500=$DIR/sam/500/S${SAMPLE}_realigned.bam     
    OUTBAM=$DIR/sam/300et500/S${SAMPLE}_merged_realigned.bam
    samtools merge $OUTBAM $IN300 $IN500 &
done
