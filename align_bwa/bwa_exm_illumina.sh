#!/bin/bash

DIR=/home/rgarcia/MCAC/fastq/exm_illumina
OUTDIR=/home/rgarcia/MCAC/sam/exm_illumina
BWA=/home/rgarcia/downloads/bwa.kit/bwa
REF=/home/rgarcia/MCAC/reference/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFASTA/genome.fa



# R1=$DIR/DLA/DLA_R1_001.fastq.gz
# R2=$DIR/DLA/DLA_R2_001.fastq.gz
# SAMOUT=$OUTDIR/DLA_001.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/DLA/DLA_R1_002.fastq.gz
# R2=$DIR/DLA/DLA_R2_002.fastq.gz
# SAMOUT=$OUTDIR/DLA_002.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/DLA/DLA_R1_003.fastq.gz
# R2=$DIR/DLA/DLA_R2_003.fastq.gz
# SAMOUT=$OUTDIR/DLA_003.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/DLA/DLA_R1_004.fastq.gz
# R2=$DIR/DLA/DLA_R2_004.fastq.gz
# SAMOUT=$OUTDIR/DLA_004.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/GEL/GEL_R1_001.fastq.gz
# R2=$DIR/GEL/GEL_R2_001.fastq.gz
# SAMOUT=$OUTDIR/GEL_001.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/GEL/GEL_R1_002.fastq.gz
# R2=$DIR/GEL/GEL_R2_002.fastq.gz
# SAMOUT=$OUTDIR/GEL_002.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/GMCA/GMCA_R1_001.fastq.gz
# R2=$DIR/GMCA/GMCA_R2_001.fastq.gz
# SAMOUT=$OUTDIR/GMCA_001.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/GMCA/GMCA_R1_002.fastq.gz
# R2=$DIR/GMCA/GMCA_R2_002.fastq.gz
# SAMOUT=$OUTDIR/GMCA_002.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/GMCA/GMCA_R1_003.fastq.gz
# R2=$DIR/GMCA/GMCA_R2_003.fastq.gz
# SAMOUT=$OUTDIR/GMCA_003.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/GMCA/GMCA_R1_004.fastq.gz
# R2=$DIR/GMCA/GMCA_R2_004.fastq.gz
# SAMOUT=$OUTDIR/GMCA_004.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/GMCA/GMCA_R1_005.fastq.gz
# R2=$DIR/GMCA/GMCA_R2_005.fastq.gz
# SAMOUT=$OUTDIR/GMCA_005.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/JLRL/JLRL_R1_001.fastq.gz
# R2=$DIR/JLRL/JLRL_R2_001.fastq.gz
# SAMOUT=$OUTDIR/JLRL_001.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/JLRL/JLRL_R1_002.fastq.gz
# R2=$DIR/JLRL/JLRL_R2_002.fastq.gz
# SAMOUT=$OUTDIR/JLRL_002.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/JLRL/JLRL_R1_003.fastq.gz
# R2=$DIR/JLRL/JLRL_R2_003.fastq.gz
# SAMOUT=$OUTDIR/JLRL_003.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/JLRL/JLRL_R1_004.fastq.gz
# R2=$DIR/JLRL/JLRL_R2_004.fastq.gz
# SAMOUT=$OUTDIR/JLRL_004.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/JLRM/JLRM_R1_001.fastq.gz
# R2=$DIR/JLRM/JLRM_R2_001.fastq.gz
# SAMOUT=$OUTDIR/JLRM_001.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/JLRM/JLRM_R1_002.fastq.gz
R2=$DIR/JLRM/JLRM_R2_002.fastq.gz
SAMOUT=$OUTDIR/JLRM_002.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/JLRM/JLRM_R1_003.fastq.gz
# R2=$DIR/JLRM/JLRM_R2_003.fastq.gz
# SAMOUT=$OUTDIR/JLRM_003.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/JLRM/JLRM_R1_004.fastq.gz
# R2=$DIR/JLRM/JLRM_R2_004.fastq.gz
# SAMOUT=$OUTDIR/JLRM_004.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/JLRM/JLRM_R1_005.fastq.gz
# R2=$DIR/JLRM/JLRM_R2_005.fastq.gz
# SAMOUT=$OUTDIR/JLRM_005.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/JLRM/JLRM_R1_006.fastq.gz
# R2=$DIR/JLRM/JLRM_R2_006.fastq.gz
# SAMOUT=$OUTDIR/JLRM_006.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/LMG/LMG_R1_001.fastq.gz
# R2=$DIR/LMG/LMG_R2_001.fastq.gz
# SAMOUT=$OUTDIR/LMG_001.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/LMG/LMG_R1_002.fastq.gz
# R2=$DIR/LMG/LMG_R2_002.fastq.gz
# SAMOUT=$OUTDIR/LMG_002.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/LMG/LMG_R1_003.fastq.gz
# R2=$DIR/LMG/LMG_R2_003.fastq.gz
# SAMOUT=$OUTDIR/LMG_003.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/LMG/LMG_R1_004.fastq.gz
# R2=$DIR/LMG/LMG_R2_004.fastq.gz
# SAMOUT=$OUTDIR/LMG_004.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/LMG/LMG_R1_005.fastq.gz
# R2=$DIR/LMG/LMG_R2_005.fastq.gz
# SAMOUT=$OUTDIR/LMG_005.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/LMG/LMG_R1_006.fastq.gz
# R2=$DIR/LMG/LMG_R2_006.fastq.gz
# SAMOUT=$OUTDIR/LMG_006.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/PTL/PTL_R1_001.fastq.gz
# R2=$DIR/PTL/PTL_R2_001.fastq.gz
# SAMOUT=$OUTDIR/PTL_001.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/PTL/PTL_R1_002.fastq.gz
# R2=$DIR/PTL/PTL_R2_002.fastq.gz
# SAMOUT=$OUTDIR/PTL_002.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/PTL/PTL_R1_003.fastq.gz
# R2=$DIR/PTL/PTL_R2_003.fastq.gz
# SAMOUT=$OUTDIR/PTL_003.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/PTL/PTL_R1_004.fastq.gz
# R2=$DIR/PTL/PTL_R2_004.fastq.gz
# SAMOUT=$OUTDIR/PTL_004.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/PTL/PTL_R1_005.fastq.gz
# R2=$DIR/PTL/PTL_R2_005.fastq.gz
# SAMOUT=$OUTDIR/PTL_005.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/PTL/PTL_R1_006.fastq.gz
# R2=$DIR/PTL/PTL_R2_006.fastq.gz
# SAMOUT=$OUTDIR/PTL_006.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/PTL/PTL_R1_007.fastq.gz
# R2=$DIR/PTL/PTL_R2_007.fastq.gz
# SAMOUT=$OUTDIR/PTL_007.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/PTL/PTL_R1_008.fastq.gz
# R2=$DIR/PTL/PTL_R2_008.fastq.gz
# SAMOUT=$OUTDIR/PTL_008.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/PTL/PTL_R1_009.fastq.gz
# R2=$DIR/PTL/PTL_R2_009.fastq.gz
# SAMOUT=$OUTDIR/PTL_009.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/PTL/PTL_R1_010.fastq.gz
# R2=$DIR/PTL/PTL_R2_010.fastq.gz
# SAMOUT=$OUTDIR/PTL_010.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/PTL/PTL_R1_011.fastq.gz
# R2=$DIR/PTL/PTL_R2_011.fastq.gz
# SAMOUT=$OUTDIR/PTL_011.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/YRN/YRN_R1_001.fastq.gz
# R2=$DIR/YRN/YRN_R2_001.fastq.gz
# SAMOUT=$OUTDIR/YRN_001.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/YRN/YRN_R1_002.fastq.gz
# R2=$DIR/YRN/YRN_R2_002.fastq.gz
# SAMOUT=$OUTDIR/YRN_002.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

# R1=$DIR/YRN/YRN_R1_003.fastq.gz
# R2=$DIR/YRN/YRN_R2_003.fastq.gz
# SAMOUT=$OUTDIR/YRN_003.sam
# $BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT
