FASTQC=/home/rgarcia/downloads/FastQC/fastqc

FASTQDIR=/home/rgarcia/MCAC/fastq/exm_illumina
FASTQCDIR=/home/rgarcia/MCAC/qc/fastqc/exm_illumina

mkdir -p $FASTQCDIR


EXM_ILLUMINA="DLA
GEL
GMCA
JLRL
JLRM
LMG
PTL
YRN"

for SAMPLE in $EXM_ILLUMINA
do
    OUTDIR=$FASTQCDIR/S${SAMPLE}
    mkdir -p $OUTDIR
    $FASTQC -t 30 `find $FASTQDIR/$SAMPLE -iname *.fastq.gz` -o $OUTDIR
done
