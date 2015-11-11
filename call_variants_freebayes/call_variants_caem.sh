FREEBAYES=/usr/local/bin/freebayes
REF=/home/rgarcia/MCAC/reference/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFASTA/genome.fa
BED=/home/rgarcia/MCAC/targets/exm/all_tracks_freebayes.bed

SAMDIR=/mnt/f/rgarcia/MCAC/sam/exm_caem_fvi_rigo
VCFDIR=/home/rgarcia/MCAC/vcf/caem_fvi_rigo

mkdir -p $VCFDIR

for SAMPLE in $(seq -f "%02g" 1 17)
do
    $FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S${SAMPLE}_realigned.bam -v $VCFDIR/S${SAMPLE}.vcf & 
done
