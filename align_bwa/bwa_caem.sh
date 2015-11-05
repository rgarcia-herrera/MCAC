#!/bin/bash

DIR=/home/rgarcia/MCAC
BWA=/home/rgarcia/downloads/bwa.kit/bwa
REF=$DIR/reference/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFASTA/genome.fa


R1=$DIR/fastq/exm_caen_fvi_rigo/S01_L001_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S01_L001_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S01_L001.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S01_L002_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S01_L002_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S01_L002.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S01_L003_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S01_L003_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S01_L003.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S01_L004_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S01_L004_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S01_L004.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S02_L001_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S02_L001_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S02_L001.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S02_L002_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S02_L002_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S02_L002.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S02_L003_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S02_L003_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S02_L003.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S02_L004_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S02_L004_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S02_L004.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S03_L001_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S03_L001_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S03_L001.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S03_L002_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S03_L002_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S03_L002.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S03_L003_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S03_L003_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S03_L003.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S03_L004_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S03_L004_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S03_L004.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S04_L001_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S04_L001_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S04_L001.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S04_L002_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S04_L002_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S04_L002.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S04_L003_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S04_L003_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S04_L003.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S04_L004_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S04_L004_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S04_L004.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S05_L001_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S05_L001_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S05_L001.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S05_L002_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S05_L002_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S05_L002.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S05_L003_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S05_L003_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S05_L003.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S05_L004_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S05_L004_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S05_L004.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S06_L001_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S06_L001_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S06_L001.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S06_L002_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S06_L002_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S06_L002.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S06_L003_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S06_L003_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S06_L003.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S06_L004_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S06_L004_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S06_L004.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S07_L001_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S07_L001_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S07_L001.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S07_L002_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S07_L002_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S07_L002.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S07_L003_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S07_L003_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S07_L003.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S07_L004_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S07_L004_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S07_L004.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S08_L001_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S08_L001_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S08_L001.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S08_L002_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S08_L002_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S08_L002.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S08_L003_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S08_L003_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S08_L003.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S08_L004_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S08_L004_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S08_L004.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S09_L001_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S09_L001_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S09_L001.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S09_L002_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S09_L002_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S09_L002.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S09_L003_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S09_L003_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S09_L003.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S09_L004_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S09_L004_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S09_L004.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S10_L001_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S10_L001_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S10_L001.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S10_L002_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S10_L002_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S10_L002.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S10_L003_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S10_L003_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S10_L003.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S10_L004_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S10_L004_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S10_L004.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S11_L001_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S11_L001_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S11_L001.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S11_L002_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S11_L002_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S11_L002.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S11_L003_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S11_L003_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S11_L003.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S11_L004_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S11_L004_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S11_L004.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S12_L001_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S12_L001_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S12_L001.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S12_L002_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S12_L002_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S12_L002.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S12_L003_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S12_L003_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S12_L003.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S12_L004_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S12_L004_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S12_L004.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S13_L001_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S13_L001_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S13_L001.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S13_L002_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S13_L002_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S13_L002.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S13_L003_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S13_L003_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S13_L003.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S13_L004_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S13_L004_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S13_L004.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S14_L001_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S14_L001_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S14_L001.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S14_L002_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S14_L002_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S14_L002.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S14_L003_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S14_L003_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S14_L003.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S14_L004_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S14_L004_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S14_L004.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S15_L001_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S15_L001_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S15_L001.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S15_L002_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S15_L002_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S15_L002.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S15_L003_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S15_L003_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S15_L003.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S15_L004_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S15_L004_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S15_L004.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S16_L001_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S16_L001_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S16_L001.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S16_L002_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S16_L002_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S16_L002.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S16_L003_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S16_L003_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S16_L003.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S16_L004_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S16_L004_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S16_L004.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S17_L001_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S17_L001_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S17_L001.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S17_L002_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S17_L002_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S17_L002.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S17_L003_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S17_L003_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S17_L003.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT

R1=$DIR/fastq/exm_caen_fvi_rigo/S17_L004_R1.fastq.gz
R2=$DIR/fastq/exm_caen_fvi_rigo/S17_L004_R2.fastq.gz
SAMOUT=$DIR/sam/exm_caem_fvi_rigo/S17_L004.sam
$BWA mem -M -t 30 $REF $R1 $R2 > $SAMOUT
