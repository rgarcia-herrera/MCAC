#!/bin/bash

DIR=/home/rgarcia/MCAC/sam
ADDORREPLACEREADGROUPS=/home/rgarcia/downloads/picard-tools-1.121/AddOrReplaceReadGroups.jar

for SAMPLE in $(seq -f "%02g" 1 48)           
do
    BAM=$DIR/300/S${SAMPLE}.bam
    BAMOUT=$DIR/300/S${SAMPLE}_rg.bam
    java -jar $ADDORREPLACEREADGROUPS \
                 I=$BAM \
                 LB='mcac' \
                 PL='illumina' \
                 PU='nil' \
                 SM=$SAMPLE \
                 O=$BAMOUT

done


for SAMPLE in $(seq -f "%02g" 1 48)           
do
    BAM=$DIR/500/S${SAMPLE}.bam
    BAMOUT=$DIR/500/S${SAMPLE}_rg.bam
    java -jar $ADDORREPLACEREADGROUPS \
                 I=$BAM \
                 LB='mcac' \
                 PL='illumina' \
                 PU='nil' \
                 SM=$SAMPLE \
                 O=$BAMOUT

done
