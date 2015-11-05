DIR=/mnt/f/rgarcia/MCAC/sam/exm_caem_fvi_rigo

for SAM in `find $DIR -iname '*.sam'`
do
    SAMPLE=`basename $SAM .sam`
    echo "samtools sort -o $DIR/${SAMPLE}.bam -O bam -T $DIR -@ 30 -m 8G $SAM &"
done
