FREEBAYES=/usr/local/bin/freebayes
REF=/home/rgarcia/MCAC/reference/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFASTA/genome.fa
BED=/home/rgarcia/MCAC/targets_gea/CYTRON_CAD_Amplicons.bed


SAMDIR=/home/rgarcia/MCAC/sam/gea
VCFDIR=/home/rgarcia/MCAC/vcf/gea

mkdir -p $VCFDIR



for SAMPLE in $(seq -f "%02g" 1 49)
do
    $FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S${SAMPLE}_realigned.bam -v $VCFDIR/S${SAMPLE}.vcf 
done

