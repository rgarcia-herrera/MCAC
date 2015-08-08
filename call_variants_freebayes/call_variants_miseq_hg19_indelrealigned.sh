FREEBAYES=/export/home/rgarcia/software/freebayes/bin/freebayes
REF=/export/home/rgarcia/MCAC/reference/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFASTA/genome.fa
BED=/export/home/rgarcia/MCAC/targets/Miocardiopatias_y_canalopatias_AllTracks.bed

SAMDIR=/export/home/rgarcia/MCAC/sam_miseq_hg19
VCFDIR=/export/home/rgarcia/MCAC/vcf/bwa_indelrealigned_fb

mkdir -p $VCFDIR

condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S01_rg_realigned.bam -v $VCFDIR/S01.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S02_rg_realigned.bam -v $VCFDIR/S02.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S03_rg_realigned.bam -v $VCFDIR/S03.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S04_rg_realigned.bam -v $VCFDIR/S04.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S05_rg_realigned.bam -v $VCFDIR/S05.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S06_rg_realigned.bam -v $VCFDIR/S06.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S07_rg_realigned.bam -v $VCFDIR/S07.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S08_rg_realigned.bam -v $VCFDIR/S08.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S09_rg_realigned.bam -v $VCFDIR/S09.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S10_rg_realigned.bam -v $VCFDIR/S10.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S11_rg_realigned.bam -v $VCFDIR/S11.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S12_rg_realigned.bam -v $VCFDIR/S12.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S13_rg_realigned.bam -v $VCFDIR/S13.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S14_rg_realigned.bam -v $VCFDIR/S14.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S15_rg_realigned.bam -v $VCFDIR/S15.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S16_rg_realigned.bam -v $VCFDIR/S16.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S17_rg_realigned.bam -v $VCFDIR/S17.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S18_rg_realigned.bam -v $VCFDIR/S18.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S19_rg_realigned.bam -v $VCFDIR/S19.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S20_rg_realigned.bam -v $VCFDIR/S20.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S21_rg_realigned.bam -v $VCFDIR/S21.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S22_rg_realigned.bam -v $VCFDIR/S22.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S23_rg_realigned.bam -v $VCFDIR/S23.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S24_rg_realigned.bam -v $VCFDIR/S24.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S25_rg_realigned.bam -v $VCFDIR/S25.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S26_rg_realigned.bam -v $VCFDIR/S26.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S27_rg_realigned.bam -v $VCFDIR/S27.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S28_rg_realigned.bam -v $VCFDIR/S28.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S29_rg_realigned.bam -v $VCFDIR/S29.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S30_rg_realigned.bam -v $VCFDIR/S30.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S31_rg_realigned.bam -v $VCFDIR/S31.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S32_rg_realigned.bam -v $VCFDIR/S32.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S33_rg_realigned.bam -v $VCFDIR/S33.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S34_rg_realigned.bam -v $VCFDIR/S34.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S35_rg_realigned.bam -v $VCFDIR/S35.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S36_rg_realigned.bam -v $VCFDIR/S36.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S37_rg_realigned.bam -v $VCFDIR/S37.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S38_rg_realigned.bam -v $VCFDIR/S38.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S39_rg_realigned.bam -v $VCFDIR/S39.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S40_rg_realigned.bam -v $VCFDIR/S40.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S41_rg_realigned.bam -v $VCFDIR/S41.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S42_rg_realigned.bam -v $VCFDIR/S42.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S43_rg_realigned.bam -v $VCFDIR/S43.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S44_rg_realigned.bam -v $VCFDIR/S44.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S45_rg_realigned.bam -v $VCFDIR/S45.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S46_rg_realigned.bam -v $VCFDIR/S46.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S47_rg_realigned.bam -v $VCFDIR/S47.vcf" &
condor_run "$FREEBAYES --standard-filters -X -u  -t $BED -f $REF $SAMDIR/S48_rg_realigned.bam -v $VCFDIR/S48.vcf" &
