FASTQC=/home/rgarcia/downloads/FastQC/fastqc

FASTQDIR=/home/rgarcia/MCAC/fastq
FASTQCDIR=/home/rgarcia/MCAC/qc/fastqc

mkdir -p $FASTQCDIR

for SAMPLE in $(seq -f "%02g" 1 48)
do
    for SIZE in {300,500}
    do
        OUTDIR=$FASTQCDIR/$SIZE/S${SAMPLE}
        mkdir -p $OUTDIR
        $FASTQC -t 30 $FASTQDIR/$SIZE/S${SAMPLE}_R1.fastq.gz $FASTQDIR/$SIZE/S${SAMPLE}_R2.fastq.gz -o $OUTDIR
    done
done

