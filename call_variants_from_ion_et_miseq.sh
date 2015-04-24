FREEBAYES=/export/home/rgarcia/software/freebayes/bin/freebayes
REF=/export/home/rgarcia/reference/GRCh38/GCA_000001405.15_GRCh38_no_alt_analysis_set.fna
BED=/export/home/rgarcia/canalopatias/targets/Miocardiopatias_y_canalopatias_AllTracks.bed
SAMDIR_ION=/export/home/rgarcia/canalopatias/sam_ion
SAMDIR_MISEQ=/export/home/rgarcia/canalopatias/sam_miseq
VCFDIR=/export/home/rgarcia/canalopatias/vcf_ion_miseq

$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S01_dedup.bam $SAMDIR_ION/S01_dedup.bam -v $VCFDIR/S01.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S02_dedup.bam $SAMDIR_ION/S02_dedup.bam -v $VCFDIR/S02.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S03_dedup.bam $SAMDIR_ION/S03_dedup.bam -v $VCFDIR/S03.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S04_dedup.bam $SAMDIR_ION/S04_dedup.bam -v $VCFDIR/S04.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S05_dedup.bam $SAMDIR_ION/S05_dedup.bam -v $VCFDIR/S05.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S06_dedup.bam $SAMDIR_ION/S06_dedup.bam -v $VCFDIR/S06.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S07_dedup.bam $SAMDIR_ION/S07_dedup.bam -v $VCFDIR/S07.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S08_dedup.bam $SAMDIR_ION/S08_dedup.bam -v $VCFDIR/S08.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S09_dedup.bam $SAMDIR_ION/S09_dedup.bam -v $VCFDIR/S09.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S10_dedup.bam $SAMDIR_ION/S10_dedup.bam -v $VCFDIR/S10.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S11_dedup.bam $SAMDIR_ION/S11_dedup.bam -v $VCFDIR/S11.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S12_dedup.bam $SAMDIR_ION/S12_dedup.bam -v $VCFDIR/S12.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S13_dedup.bam $SAMDIR_ION/S13_dedup.bam -v $VCFDIR/S13.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S14_dedup.bam $SAMDIR_ION/S14_dedup.bam -v $VCFDIR/S14.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S15_dedup.bam $SAMDIR_ION/S15_dedup.bam -v $VCFDIR/S15.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S16_dedup.bam $SAMDIR_ION/S16_dedup.bam -v $VCFDIR/S16.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S17_dedup.bam $SAMDIR_ION/S17_dedup.bam -v $VCFDIR/S17.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S18_dedup.bam $SAMDIR_ION/S18_dedup.bam -v $VCFDIR/S18.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S19_dedup.bam $SAMDIR_ION/S19_dedup.bam -v $VCFDIR/S19.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S20_dedup.bam $SAMDIR_ION/S20_dedup.bam -v $VCFDIR/S20.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S21_dedup.bam $SAMDIR_ION/S21_dedup.bam -v $VCFDIR/S21.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S22_dedup.bam $SAMDIR_ION/S22_dedup.bam -v $VCFDIR/S22.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S23_dedup.bam $SAMDIR_ION/S23_dedup.bam -v $VCFDIR/S23.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S24_dedup.bam $SAMDIR_ION/S24_dedup.bam -v $VCFDIR/S24.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S25_dedup.bam $SAMDIR_ION/S25_dedup.bam -v $VCFDIR/S25.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S26_dedup.bam $SAMDIR_ION/S26_dedup.bam -v $VCFDIR/S26.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S27_dedup.bam $SAMDIR_ION/S27_dedup.bam -v $VCFDIR/S27.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S28_dedup.bam $SAMDIR_ION/S28_dedup.bam -v $VCFDIR/S28.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S29_dedup.bam $SAMDIR_ION/S29_dedup.bam -v $VCFDIR/S29.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S30_dedup.bam $SAMDIR_ION/S30_dedup.bam -v $VCFDIR/S30.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S31_dedup.bam $SAMDIR_ION/S31_dedup.bam -v $VCFDIR/S31.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S32_dedup.bam $SAMDIR_ION/S32_dedup.bam -v $VCFDIR/S32.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S33_dedup.bam $SAMDIR_ION/S33_dedup.bam -v $VCFDIR/S33.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S34_dedup.bam $SAMDIR_ION/S34_dedup.bam -v $VCFDIR/S34.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S35_dedup.bam $SAMDIR_ION/S35_dedup.bam -v $VCFDIR/S35.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S36_dedup.bam $SAMDIR_ION/S36_dedup.bam -v $VCFDIR/S36.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S37_dedup.bam $SAMDIR_ION/S37_dedup.bam -v $VCFDIR/S37.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S38_dedup.bam $SAMDIR_ION/S38_dedup.bam -v $VCFDIR/S38.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S39_dedup.bam $SAMDIR_ION/S39_dedup.bam -v $VCFDIR/S39.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S40_dedup.bam $SAMDIR_ION/S40_dedup.bam -v $VCFDIR/S40.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S41_dedup.bam $SAMDIR_ION/S41_dedup.bam -v $VCFDIR/S41.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S42_dedup.bam $SAMDIR_ION/S42_dedup.bam -v $VCFDIR/S42.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S43_dedup.bam $SAMDIR_ION/S43_dedup.bam -v $VCFDIR/S43.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S44_dedup.bam $SAMDIR_ION/S44_dedup.bam -v $VCFDIR/S44.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S45_dedup.bam $SAMDIR_ION/S45_dedup.bam -v $VCFDIR/S45.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S46_dedup.bam $SAMDIR_ION/S46_dedup.bam -v $VCFDIR/S46.vcf
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR_MISEQ/S47_dedup.bam $SAMDIR_ION/S47_dedup.bam -v $VCFDIR/S47.vcf

