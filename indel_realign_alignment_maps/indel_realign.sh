#!/bin/bash

DIR=/home/rgarcia/MCAC/sam
GATK=/home/rgarcia/downloads/GenomeAnalysisTK.jar
REF=/home/rgarcia/MCAC/reference/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFASTA/genome.fa
KNOWN=/home/rgarcia/MCAC/reference/1000G_phase1.indels.b37.vcf.gz


# for SAMPLE in $(seq -f "%02g" 1 48)           
# do
#     INTERVALS=$DIR/300/S${SAMPLE}.intervals
#     SAM=$DIR/300/S${SAMPLE}_rg.bam

#     # echo "creating intervals file"
#     # echo $INTERVALS
#     # java -Xmx1g -jar $GATK \
#     #      -T RealignerTargetCreator \
#     #      -R $REF \
#     #      -I $SAM \
#     #      --known $KNOWN \
#     #      -dt NONE \
#     #      -o $INTERVALS &

#     echo "realigning"
#     BAMOUT=$DIR/300/S${SAMPLE}_realigned.bam
#     java -jar $GATK \
#          -T IndelRealigner \
#          -R $REF \
#          -I $SAM \
#          -dt NONE \
#          -targetIntervals $INTERVALS \
#          -o $BAMOUT
# done




# for SAMPLE in $(seq -f "%02g" 1 48)           
# do
#     INTERVALS=$DIR/500/S${SAMPLE}.intervals
#     SAM=$DIR/500/S${SAMPLE}_rg.bam


#     echo "creating intervals file"
#     echo $INTERVALS
#     java -Xmx1g -jar $GATK \
#          -T RealignerTargetCreator \
#          -R $REF \
#          -I $SAM \
#          --known $KNOWN \
#          -dt NONE \
#          -o $INTERVALS &

#     echo "realigning"
#     BAMOUT=$DIR/500/S${SAMPLE}_realigned.bam
#     java -jar $GATK \
#          -T IndelRealigner \
#          -R $REF \
#          -I $SAM \
#          -dt NONE \
#          -targetIntervals $INTERVALS \
#          -o $BAMOUT
# done



# MAU29="S17.aqm
# S26.MGV
# S18.IXH
# S22.CYDR
# S24.MRMT
# S20.CEV
# S19.CFOG
# S23.MEAR
# S21.PAHH
# S25.MCV"

# for SAMPLE in $MAU29
# do
#     INTERVALS=$DIR/mau29/${SAMPLE}.intervals
#     SAM=$DIR/mau29/${SAMPLE}_rg.bam

#     echo "creating intervals file"
#     echo $INTERVALS
#     java -Xmx1g -jar $GATK \
#          -T RealignerTargetCreator \
#          -R $REF \
#          -I $SAM \
#          --known $KNOWN \
#          -dt NONE \
#          -o $INTERVALS &

#     # echo "realigning"
#     # BAMOUT=$DIR/500/S${SAMPLE}_realigned.bam
#     # java -jar $GATK \
#     #      -T IndelRealigner \
#     #      -R $REF \
#     #      -I $SAM \
#     #      -dt NONE \
#     #      -targetIntervals $INTERVALS \
#     #      -o $BAMOUT
# done



EXM_ILLIMINA="DLA
GEL
GMCA
JLRL
JLRM
LMG
PTL
YRN"

for SAMPLE in $EXM_ILLIMINA
do
    INTERVALS=$DIR/exm_illumina/${SAMPLE}.intervals
    SAM=$DIR/exm_illumina/${SAMPLE}_rg_dedup.bam

    # echo "creating intervals file"
    # echo $INTERVALS
    # java -Xmx1g -jar $GATK \
    #      -T RealignerTargetCreator \
    #      -R $REF \
    #      -I $SAM \
    #      --known $KNOWN \
    #      -dt NONE \
    #      -o $INTERVALS &

    echo "realigning"
    BAMOUT=$DIR/exm_illumina/${SAMPLE}_realigned.bam
    java -jar $GATK \
         -T IndelRealigner \
         -R $REF \
         -I $SAM \
         -dt NONE \
         -targetIntervals $INTERVALS \
         -o $BAMOUT &
done
