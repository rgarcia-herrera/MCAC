#!/bin/bash

QUALIMAP=/home/rgarcia/downloads/qualimap_v2.1.1/qualimap
BASE=/home/rgarcia/MCAC
BED=$BASE/targets/Miocardiopatias_y_canalopatias_Amplicons.bed

BAMDIR=$BASE/sam/300
QCDIR=$BASE/qc/qualimap/300
mkdir -p $QCDIR

find $BAMDIR -iname 'S*_realigned.bam' \
     -printf "$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam %p -outdir $QCDIR/%f \n" 



BAMDIR=$BASE/sam/500
QCDIR=$BASE/qc/qualimap/500
mkdir -p $QCDIR

find $BAMDIR -iname 'S*_realigned.bam' \
     -printf "$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam %p -outdir $QCDIR/%f \n" 
