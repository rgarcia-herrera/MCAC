#!/bin/bash

QUALIMAP=/export/home/rgarcia/software/qualimap_v2.1/qualimap
BASE=/state/partition1/home/rgarcia/MCAC
BED=$BASE/targets/Miocardiopatias_y_canalopatias_Amplicons.bed

BAMDIR=$BASE/sam_miseq_hg19
QCDIR=$BASE/qc/qualimap
mkdir -p $QCDIR


$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S39.bam -outdir $QCDIR/S39
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S25.bam -outdir $QCDIR/S25
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S43.bam -outdir $QCDIR/S43
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S18.bam -outdir $QCDIR/S18
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S23.bam -outdir $QCDIR/S23
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S28.bam -outdir $QCDIR/S28
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S15.bam -outdir $QCDIR/S15
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S17.bam -outdir $QCDIR/S17
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S44.bam -outdir $QCDIR/S44
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S13.bam -outdir $QCDIR/S13
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S10.bam -outdir $QCDIR/S10
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S33.bam -outdir $QCDIR/S33
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S11.bam -outdir $QCDIR/S11
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S05.bam -outdir $QCDIR/S05
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S40.bam -outdir $QCDIR/S40
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S06.bam -outdir $QCDIR/S06
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S34.bam -outdir $QCDIR/S34
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S37.bam -outdir $QCDIR/S37
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S04.bam -outdir $QCDIR/S04
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S09.bam -outdir $QCDIR/S09
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S21.bam -outdir $QCDIR/S21
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S42.bam -outdir $QCDIR/S42
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S27.bam -outdir $QCDIR/S27
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S45.bam -outdir $QCDIR/S45
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S20.bam -outdir $QCDIR/S20
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S30.bam -outdir $QCDIR/S30
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S36.bam -outdir $QCDIR/S36
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S47.bam -outdir $QCDIR/S47
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S26.bam -outdir $QCDIR/S26
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S19.bam -outdir $QCDIR/S19
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S46.bam -outdir $QCDIR/S46
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S02.bam -outdir $QCDIR/S02
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S32.bam -outdir $QCDIR/S32
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S07.bam -outdir $QCDIR/S07
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S48.bam -outdir $QCDIR/S48
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S03.bam -outdir $QCDIR/S03
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S29.bam -outdir $QCDIR/S29
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S41.bam -outdir $QCDIR/S41
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S16.bam -outdir $QCDIR/S16
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S31.bam -outdir $QCDIR/S31
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S08.bam -outdir $QCDIR/S08
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S38.bam -outdir $QCDIR/S38
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S12.bam -outdir $QCDIR/S12
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S14.bam -outdir $QCDIR/S14
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S01.bam -outdir $QCDIR/S01
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S35.bam -outdir $QCDIR/S35
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S22.bam -outdir $QCDIR/S22
$QUALIMAP bamqc --feature-file $BED -c -outformat HTML -bam $BAMDIR/S24.bam -outdir $QCDIR/S24
