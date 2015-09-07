FREEBAYES=/usr/local/bin/freebayes
REF=/home/rgarcia/MCAC/reference/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFASTA/genome.fa
BED=/home/rgarcia/MCAC/targets/Miocardiopatias_y_canalopatias_AllTracks.bed

# SAMDIR=/home/rgarcia/MCAC/sam/300
# VCFDIR=/home/rgarcia/MCAC/vcf/300

# mkdir -p $VCFDIR

# for SAMPLE in $(seq -f "%02g" 1 48)
# do
#     $FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S${SAMPLE}_realigned.bam -v $VCFDIR/S${SAMPLE}.vcf &
# done






# SAMDIR=/home/rgarcia/MCAC/sam/500
# VCFDIR=/home/rgarcia/MCAC/vcf/500

# mkdir -p $VCFDIR

# for SAMPLE in $(seq -f "%02g" 1 48)
# do
#     $FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S${SAMPLE}_realigned.bam -v $VCFDIR/S${SAMPLE}.vcf &
# done




SAMDIR=/home/rgarcia/MCAC/sam
VCFDIR=/home/rgarcia/MCAC/vcf/300et500

mkdir -p $VCFDIR

for SAMPLE in $(seq -f "%02g" 1 48)
do
    $FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/300/S${SAMPLE}_realigned.bam $SAMDIR/500/S${SAMPLE}_realigned.bam -v $VCFDIR/S${SAMPLE}.vcf &
done
