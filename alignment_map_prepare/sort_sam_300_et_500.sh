DIR=/home/rgarcia/MCAC/sam

for SAMPLE in $(seq -f "%02g" 1 48)
do
    samtools sort -o $DIR/300/S${SAMPLE}.bam \
	     -O bam -T $DIR -@ 30 -m 8G $DIR/300/S${SAMPLE}.sam
done


for SAMPLE in $(seq -f "%02g" 1 48)
do
    samtools sort -o $DIR/500/S${SAMPLE}.bam \
	     -O bam -T $DIR -@ 30 -m 8G $DIR/500/S${SAMPLE}.sam
done

