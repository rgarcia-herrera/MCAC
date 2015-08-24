#!/bin/bash

QUALIMAP=/home/rgarcia/downloads/qualimap_v2.1.1/qualimap
BASE=/home/rgarcia/MCAC
BED=$BASE/targets/Miocardiopatias_y_canalopatias_Amplicons.bed

BAMDIR=$BASE/sam/sam_miseq_hg19
QCDIR=$BASE/qc/qualimap
mkdir -p $QCDIR

find $BAMDIR -iname 'S*_rg_realigned.bam' \
     -printf "$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam %p -outdir $QCDIR/%f \n" 
