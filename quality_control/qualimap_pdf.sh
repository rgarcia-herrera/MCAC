#!/bin/bash

QUALIMAP=/export/home/rgarcia/software/qualimap_v2.1/qualimap
BASE=/state/partition1/home/rgarcia/MCAC
BED=$BASE/targets/Miocardiopatias_y_canalopatias_Amplicons.bed

BAMDIR=$BASE/sam_miseq_hg19
QCDIR=$BASE/qc/qualimap
mkdir -p $QCDIR

$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S39.bam -outfile $QCDIR/S39.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S25.bam -outfile $QCDIR/S25.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S43.bam -outfile $QCDIR/S43.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S18.bam -outfile $QCDIR/S18.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S23.bam -outfile $QCDIR/S23.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S28.bam -outfile $QCDIR/S28.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S15.bam -outfile $QCDIR/S15.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S17.bam -outfile $QCDIR/S17.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S44.bam -outfile $QCDIR/S44.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S13.bam -outfile $QCDIR/S13.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S10.bam -outfile $QCDIR/S10.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S33.bam -outfile $QCDIR/S33.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S11.bam -outfile $QCDIR/S11.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S05.bam -outfile $QCDIR/S05.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S40.bam -outfile $QCDIR/S40.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S06.bam -outfile $QCDIR/S06.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S34.bam -outfile $QCDIR/S34.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S37.bam -outfile $QCDIR/S37.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S04.bam -outfile $QCDIR/S04.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S09.bam -outfile $QCDIR/S09.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S21.bam -outfile $QCDIR/S21.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S42.bam -outfile $QCDIR/S42.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S27.bam -outfile $QCDIR/S27.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S45.bam -outfile $QCDIR/S45.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S20.bam -outfile $QCDIR/S20.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S30.bam -outfile $QCDIR/S30.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S36.bam -outfile $QCDIR/S36.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S47.bam -outfile $QCDIR/S47.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S26.bam -outfile $QCDIR/S26.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S19.bam -outfile $QCDIR/S19.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S46.bam -outfile $QCDIR/S46.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S02.bam -outfile $QCDIR/S02.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S32.bam -outfile $QCDIR/S32.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S07.bam -outfile $QCDIR/S07.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S48.bam -outfile $QCDIR/S48.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S03.bam -outfile $QCDIR/S03.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S29.bam -outfile $QCDIR/S29.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S41.bam -outfile $QCDIR/S41.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S16.bam -outfile $QCDIR/S16.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S31.bam -outfile $QCDIR/S31.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S08.bam -outfile $QCDIR/S08.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S38.bam -outfile $QCDIR/S38.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S12.bam -outfile $QCDIR/S12.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S14.bam -outfile $QCDIR/S14.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S01.bam -outfile $QCDIR/S01.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S35.bam -outfile $QCDIR/S35.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S22.bam -outfile $QCDIR/S22.pdf
$QUALIMAP bamqc --feature-file $BED -c -outformat PDF -bam $BAMDIR/S24.bam -outfile $QCDIR/S24.pdf
