#!/bin/bash

VCFDIR=/home/rgarcia/MCAC/vcf

for SAMPLE in $(seq -f "%02g" 1 48)
do
    for BATCH in {300,500,300et500}
    do
        grep \# $VCFDIR/$BATCH/S${SAMPLE}.vcf > $VCFDIR/$BATCH/S${SAMPLE}.norepeats.vcf
        grep -v \# $VCFDIR/$BATCH/S${SAMPLE}.vcf | sort | uniq >> $VCFDIR/$BATCH/S${SAMPLE}.norepeats.vcf
    done
done
