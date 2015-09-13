FREEBAYES=/usr/local/bin/freebayes
REF=/home/rgarcia/MCAC/reference/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFASTA/genome.fa

EXM_ILLIMINA="DLA
GEL
GMCA
JLRL
JLRM
LMG
PTL
YRN"

SAMDIR=/home/rgarcia/MCAC/sam/exm_illumina
VCFDIR=/home/rgarcia/MCAC/vcf/exm_illumina

mkdir -p $VCFDIR

for SAMPLE in $EXM_ILLIMINA
do
    $FREEBAYES --standard-filters -X -u -f $REF $SAMDIR/${SAMPLE}_realigned.bam -v $VCFDIR/${SAMPLE}.vcf 
done

