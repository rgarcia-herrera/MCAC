FREEBAYES=/export/home/rgarcia/software/freebayes/bin/freebayes
REF=/export/home/rgarcia/reference/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFASTA/genome.fa
BED=/export/home/rgarcia/MCAC/targets/Miocardiopatias_y_canalopatias_AllTracks.bed

SAMDIR=/export/home/rgarcia/MCAC/sam_miseq_hg19
VCFDIR=/export/home/rgarcia/MCAC/vcf/bwa_fb

$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S01.bam -v $VCFDIR/S01.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S02.bam -v $VCFDIR/S02.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S03.bam -v $VCFDIR/S03.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S04.bam -v $VCFDIR/S04.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S05.bam -v $VCFDIR/S05.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S06.bam -v $VCFDIR/S06.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S07.bam -v $VCFDIR/S07.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S08.bam -v $VCFDIR/S08.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S09.bam -v $VCFDIR/S09.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S10.bam -v $VCFDIR/S10.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S11.bam -v $VCFDIR/S11.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S12.bam -v $VCFDIR/S12.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S13.bam -v $VCFDIR/S13.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S14.bam -v $VCFDIR/S14.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S15.bam -v $VCFDIR/S15.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S16.bam -v $VCFDIR/S16.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S17.bam -v $VCFDIR/S17.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S18.bam -v $VCFDIR/S18.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S19.bam -v $VCFDIR/S19.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S20.bam -v $VCFDIR/S20.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S21.bam -v $VCFDIR/S21.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S22.bam -v $VCFDIR/S22.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S23.bam -v $VCFDIR/S23.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S24.bam -v $VCFDIR/S24.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S25.bam -v $VCFDIR/S25.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S26.bam -v $VCFDIR/S26.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S27.bam -v $VCFDIR/S27.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S28.bam -v $VCFDIR/S28.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S29.bam -v $VCFDIR/S29.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S30.bam -v $VCFDIR/S30.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S31.bam -v $VCFDIR/S31.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S32.bam -v $VCFDIR/S32.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S33.bam -v $VCFDIR/S33.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S34.bam -v $VCFDIR/S34.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S35.bam -v $VCFDIR/S35.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S36.bam -v $VCFDIR/S36.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S37.bam -v $VCFDIR/S37.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S38.bam -v $VCFDIR/S38.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S39.bam -v $VCFDIR/S39.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S40.bam -v $VCFDIR/S40.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S41.bam -v $VCFDIR/S41.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S42.bam -v $VCFDIR/S42.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S43.bam -v $VCFDIR/S43.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S44.bam -v $VCFDIR/S44.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S45.bam -v $VCFDIR/S45.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S46.bam -v $VCFDIR/S46.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S47.bam -v $VCFDIR/S47.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S48.bam -v $VCFDIR/S48.vcf &



SAMDIR=/export/home/rgarcia/MCAC/sam_basespace
VCFDIR=/export/home/rgarcia/MCAC/vcf/mistery_fb


$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S01.bam -v $VCFDIR/S01.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S02.bam -v $VCFDIR/S02.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S03.bam -v $VCFDIR/S03.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S04.bam -v $VCFDIR/S04.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S05.bam -v $VCFDIR/S05.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S06.bam -v $VCFDIR/S06.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S07.bam -v $VCFDIR/S07.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S08.bam -v $VCFDIR/S08.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S09.bam -v $VCFDIR/S09.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S10.bam -v $VCFDIR/S10.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S11.bam -v $VCFDIR/S11.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S12.bam -v $VCFDIR/S12.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S13.bam -v $VCFDIR/S13.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S14.bam -v $VCFDIR/S14.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S15.bam -v $VCFDIR/S15.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S16.bam -v $VCFDIR/S16.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S17.bam -v $VCFDIR/S17.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S18.bam -v $VCFDIR/S18.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S19.bam -v $VCFDIR/S19.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S20.bam -v $VCFDIR/S20.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S21.bam -v $VCFDIR/S21.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S22.bam -v $VCFDIR/S22.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S23.bam -v $VCFDIR/S23.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S24.bam -v $VCFDIR/S24.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S25.bam -v $VCFDIR/S25.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S26.bam -v $VCFDIR/S26.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S27.bam -v $VCFDIR/S27.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S28.bam -v $VCFDIR/S28.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S29.bam -v $VCFDIR/S29.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S30.bam -v $VCFDIR/S30.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S31.bam -v $VCFDIR/S31.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S32.bam -v $VCFDIR/S32.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S33.bam -v $VCFDIR/S33.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S34.bam -v $VCFDIR/S34.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S35.bam -v $VCFDIR/S35.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S36.bam -v $VCFDIR/S36.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S37.bam -v $VCFDIR/S37.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S38.bam -v $VCFDIR/S38.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S39.bam -v $VCFDIR/S39.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S40.bam -v $VCFDIR/S40.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S41.bam -v $VCFDIR/S41.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S42.bam -v $VCFDIR/S42.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S43.bam -v $VCFDIR/S43.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S44.bam -v $VCFDIR/S44.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S45.bam -v $VCFDIR/S45.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S46.bam -v $VCFDIR/S46.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S47.bam -v $VCFDIR/S47.vcf &
$FREEBAYES --standard-filters -t $BED -f $REF $SAMDIR/S48.bam -v $VCFDIR/S48.vcf &

