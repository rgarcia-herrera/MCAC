#!/bin/bash


DIR=/mnt/f/rgarcia/MCAC/sam/exm_caem_fvi_rigo

samtools merge $DIR/S01.bam $DIR/S01_L*.bam &
samtools merge $DIR/S02.bam $DIR/S02_L*.bam &
samtools merge $DIR/S03.bam $DIR/S03_L*.bam &
samtools merge $DIR/S04.bam $DIR/S04_L*.bam &
samtools merge $DIR/S05.bam $DIR/S05_L*.bam &
samtools merge $DIR/S06.bam $DIR/S06_L*.bam &
samtools merge $DIR/S07.bam $DIR/S07_L*.bam &
samtools merge $DIR/S08.bam $DIR/S08_L*.bam &
samtools merge $DIR/S09.bam $DIR/S09_L*.bam &
samtools merge $DIR/S10.bam $DIR/S10_L*.bam &
samtools merge $DIR/S11.bam $DIR/S11_L*.bam &
samtools merge $DIR/S12.bam $DIR/S12_L*.bam &
samtools merge $DIR/S13.bam $DIR/S13_L*.bam &
samtools merge $DIR/S14.bam $DIR/S14_L*.bam &
samtools merge $DIR/S15.bam $DIR/S15_L*.bam &
samtools merge $DIR/S16.bam $DIR/S16_L*.bam &
samtools merge $DIR/S17.bam $DIR/S17_L*.bam &
