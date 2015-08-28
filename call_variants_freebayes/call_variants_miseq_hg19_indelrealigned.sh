FREEBAYES=/usr/local/bin/freebayes
REF=/home/rgarcia/MCAC/reference/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFASTA/genome.fa
BED=/home/rgarcia/MCAC/targets/Miocardiopatias_y_canalopatias_AllTracks.bed

SAMDIR=/home/rgarcia/MCAC/sam/sam_miseq_hg19
VCFDIR=/home/rgarcia/MCAC/vcf/bwa_indelrealigned_fb

mkdir -p $VCFDIR

$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S01_rg_realigned.bam -v $VCFDIR/S01.vcf --failed-alleles $VCFDIR/S01_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S02_rg_realigned.bam -v $VCFDIR/S02.vcf --failed-alleles $VCFDIR/S02_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S03_rg_realigned.bam -v $VCFDIR/S03.vcf --failed-alleles $VCFDIR/S03_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S04_rg_realigned.bam -v $VCFDIR/S04.vcf --failed-alleles $VCFDIR/S04_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S05_rg_realigned.bam -v $VCFDIR/S05.vcf --failed-alleles $VCFDIR/S05_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S06_rg_realigned.bam -v $VCFDIR/S06.vcf --failed-alleles $VCFDIR/S06_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S07_rg_realigned.bam -v $VCFDIR/S07.vcf --failed-alleles $VCFDIR/S07_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S08_rg_realigned.bam -v $VCFDIR/S08.vcf --failed-alleles $VCFDIR/S08_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S09_rg_realigned.bam -v $VCFDIR/S09.vcf --failed-alleles $VCFDIR/S09_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S10_rg_realigned.bam -v $VCFDIR/S10.vcf --failed-alleles $VCFDIR/S10_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S11_rg_realigned.bam -v $VCFDIR/S11.vcf --failed-alleles $VCFDIR/S11_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S12_rg_realigned.bam -v $VCFDIR/S12.vcf --failed-alleles $VCFDIR/S12_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S13_rg_realigned.bam -v $VCFDIR/S13.vcf --failed-alleles $VCFDIR/S13_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S14_rg_realigned.bam -v $VCFDIR/S14.vcf --failed-alleles $VCFDIR/S14_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S15_rg_realigned.bam -v $VCFDIR/S15.vcf --failed-alleles $VCFDIR/S15_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S16_rg_realigned.bam -v $VCFDIR/S16.vcf --failed-alleles $VCFDIR/S16_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S17_rg_realigned.bam -v $VCFDIR/S17.vcf --failed-alleles $VCFDIR/S17_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S18_rg_realigned.bam -v $VCFDIR/S18.vcf --failed-alleles $VCFDIR/S18_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S19_rg_realigned.bam -v $VCFDIR/S19.vcf --failed-alleles $VCFDIR/S19_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S20_rg_realigned.bam -v $VCFDIR/S20.vcf --failed-alleles $VCFDIR/S20_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S21_rg_realigned.bam -v $VCFDIR/S21.vcf --failed-alleles $VCFDIR/S21_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S22_rg_realigned.bam -v $VCFDIR/S22.vcf --failed-alleles $VCFDIR/S22_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S23_rg_realigned.bam -v $VCFDIR/S23.vcf --failed-alleles $VCFDIR/S23_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S24_rg_realigned.bam -v $VCFDIR/S24.vcf --failed-alleles $VCFDIR/S24_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S25_rg_realigned.bam -v $VCFDIR/S25.vcf --failed-alleles $VCFDIR/S25_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S26_rg_realigned.bam -v $VCFDIR/S26.vcf --failed-alleles $VCFDIR/S26_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S27_rg_realigned.bam -v $VCFDIR/S27.vcf --failed-alleles $VCFDIR/S27_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S28_rg_realigned.bam -v $VCFDIR/S28.vcf --failed-alleles $VCFDIR/S28_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S29_rg_realigned.bam -v $VCFDIR/S29.vcf --failed-alleles $VCFDIR/S29_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S30_rg_realigned.bam -v $VCFDIR/S30.vcf --failed-alleles $VCFDIR/S30_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S31_rg_realigned.bam -v $VCFDIR/S31.vcf --failed-alleles $VCFDIR/S31_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S32_rg_realigned.bam -v $VCFDIR/S32.vcf --failed-alleles $VCFDIR/S32_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S33_rg_realigned.bam -v $VCFDIR/S33.vcf --failed-alleles $VCFDIR/S33_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S34_rg_realigned.bam -v $VCFDIR/S34.vcf --failed-alleles $VCFDIR/S34_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S35_rg_realigned.bam -v $VCFDIR/S35.vcf --failed-alleles $VCFDIR/S35_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S36_rg_realigned.bam -v $VCFDIR/S36.vcf --failed-alleles $VCFDIR/S36_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S37_rg_realigned.bam -v $VCFDIR/S37.vcf --failed-alleles $VCFDIR/S37_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S38_rg_realigned.bam -v $VCFDIR/S38.vcf --failed-alleles $VCFDIR/S38_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S39_rg_realigned.bam -v $VCFDIR/S39.vcf --failed-alleles $VCFDIR/S39_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S40_rg_realigned.bam -v $VCFDIR/S40.vcf --failed-alleles $VCFDIR/S40_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S41_rg_realigned.bam -v $VCFDIR/S41.vcf --failed-alleles $VCFDIR/S41_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S42_rg_realigned.bam -v $VCFDIR/S42.vcf --failed-alleles $VCFDIR/S42_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S43_rg_realigned.bam -v $VCFDIR/S43.vcf --failed-alleles $VCFDIR/S43_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S44_rg_realigned.bam -v $VCFDIR/S44.vcf --failed-alleles $VCFDIR/S44_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S45_rg_realigned.bam -v $VCFDIR/S45.vcf --failed-alleles $VCFDIR/S45_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S46_rg_realigned.bam -v $VCFDIR/S46.vcf --failed-alleles $VCFDIR/S46_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S47_rg_realigned.bam -v $VCFDIR/S47.vcf --failed-alleles $VCFDIR/S47_failed.bed &
$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S48_rg_realigned.bam -v $VCFDIR/S48.vcf --failed-alleles $VCFDIR/S48_failed.bed &
