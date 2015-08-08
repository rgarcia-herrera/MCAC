#!/bin/bash

BASE=/state/partition1/home/rgarcia/MCAC
BED=$BASE/targets/solo_genes.bed

BAMDIR=$BASE/sam_miseq_hg19
QCDIR=$BASE/qc/depth_miseq_hg19
mkdir -p $QCDIR

find $BAMDIR -iname 'S*_rg_realigned.bam' \
     -printf "bedtools coverage -d -abam %p -b $BED | awk '{print \$4,\$6}' > $QCDIR/%f.genes_depthtsv \n"
