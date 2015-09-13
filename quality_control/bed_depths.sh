#!/bin/bash

BASE=/home/rgarcia/MCAC
BED=$BASE/targets/solo_genes.bed

BAMDIR=$BASE/sam/500
QCDIR=$BASE/qc/depths/500
mkdir -p $QCDIR

find $BAMDIR -iname 'S*_realigned.bam' \
     -printf "bedtools coverage -d -abam %p -b $BED | awk '{print \$4,\$6}' > $QCDIR/%f.genes_depth.tsv &\n"
