FREEBAYES=/usr/local/bin/freebayes
REF=/home/rgarcia/MCAC/reference/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFASTA/genome.fa
BED=/home/rgarcia/MCAC/targets/Miocardiopatias_y_canalopatias_AllTracks.bed

SAMDIR=/home/rgarcia/MCAC/sam/mau29
VCFDIR=/home/rgarcia/MCAC/vcf/mau29

mkdir -p $VCFDIR

for SAMPLE in $(seq -f "%02g" 17 26)
do
    $FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S${SAMPLE}_realigned.bam -v $VCFDIR/S${SAMPLE}.vcf &
done





