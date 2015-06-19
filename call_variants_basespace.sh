FREEBAYES=/export/home/rgarcia/software/freebayes/bin/freebayes
REF=/export/home/rgarcia/reference/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFASTA/genome.fa
BED=/export/home/rgarcia/canalopatias/targets/Miocardiopatias_y_canalopatias_Amplicons.bed
SAMDIR=/export/home/rgarcia/canalopatias/sam_basespace
VCFDIR=/export/home/rgarcia/canalopatias/vcf_basespace

$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S00_dedup.bam -v $VCFDIR/S00.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S01_dedup.bam -v $VCFDIR/S01.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S02_dedup.bam -v $VCFDIR/S02.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S03_dedup.bam -v $VCFDIR/S03.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S04_dedup.bam -v $VCFDIR/S04.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S05_dedup.bam -v $VCFDIR/S05.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S06_dedup.bam -v $VCFDIR/S06.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S07_dedup.bam -v $VCFDIR/S07.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S08_dedup.bam -v $VCFDIR/S08.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S09_dedup.bam -v $VCFDIR/S09.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S10_dedup.bam -v $VCFDIR/S10.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S11_dedup.bam -v $VCFDIR/S11.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S12_dedup.bam -v $VCFDIR/S12.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S13_dedup.bam -v $VCFDIR/S13.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S14_dedup.bam -v $VCFDIR/S14.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S15_dedup.bam -v $VCFDIR/S15.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S16_dedup.bam -v $VCFDIR/S16.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S17_dedup.bam -v $VCFDIR/S17.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S18_dedup.bam -v $VCFDIR/S18.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S19_dedup.bam -v $VCFDIR/S19.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S20_dedup.bam -v $VCFDIR/S20.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S21_dedup.bam -v $VCFDIR/S21.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S22_dedup.bam -v $VCFDIR/S22.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S23_dedup.bam -v $VCFDIR/S23.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S24_dedup.bam -v $VCFDIR/S24.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S25_dedup.bam -v $VCFDIR/S25.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S26_dedup.bam -v $VCFDIR/S26.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S27_dedup.bam -v $VCFDIR/S27.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S28_dedup.bam -v $VCFDIR/S28.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S29_dedup.bam -v $VCFDIR/S29.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S30_dedup.bam -v $VCFDIR/S30.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S31_dedup.bam -v $VCFDIR/S31.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S32_dedup.bam -v $VCFDIR/S32.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S33_dedup.bam -v $VCFDIR/S33.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S34_dedup.bam -v $VCFDIR/S34.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S35_dedup.bam -v $VCFDIR/S35.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S36_dedup.bam -v $VCFDIR/S36.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S37_dedup.bam -v $VCFDIR/S37.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S38_dedup.bam -v $VCFDIR/S38.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S39_dedup.bam -v $VCFDIR/S39.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S40_dedup.bam -v $VCFDIR/S40.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S41_dedup.bam -v $VCFDIR/S41.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S42_dedup.bam -v $VCFDIR/S42.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S43_dedup.bam -v $VCFDIR/S43.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S44_dedup.bam -v $VCFDIR/S44.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S45_dedup.bam -v $VCFDIR/S45.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S46_dedup.bam -v $VCFDIR/S46.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S47_dedup.bam -v $VCFDIR/S47.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S48_dedup.bam -v $VCFDIR/S48.vcf

