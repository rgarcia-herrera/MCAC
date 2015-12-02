#!/bin/bash

HALOPLEX="python /home/rgarcia/MCAC/vep/vep2csv_filter_haloplex_genes.py"
FRAMESHIFT="python /home/rgarcia/MCAC/vep/vep2csv_frameshift.py"
IMPACT="python /home/rgarcia/MCAC/vep/vep2csv_impact.py"
PATHOGENIC="python /home/rgarcia/MCAC/vep/vep2csv_pathogenic.py"
PROBPOS="python /home/rgarcia/MCAC/vep/vep2csv_prob_poss_del.py"


DIR=/home/rgarcia/MCAC/vcf/500

for SAMPLE in $(seq -f "%02g" 1 48)
do
    $HALOPLEX $DIR/S${SAMPLE}.vep.csv | awk '{print $16,$5,$10,$11,$27,$26,$13,$43,$52,$7,$14,$1,$2}' > $DIR/S${SAMPLE}.HALOPLEX.vep.tsv &
    $FRAMESHIFT $DIR/S${SAMPLE}.vep.csv | awk '{print $16,$5,$10,$11,$27,$26,$13,$43,$52,$7,$14,$1,$2}' > $DIR/S${SAMPLE}.FRAMESHIFT.vep.tsv &
    $IMPACT $DIR/S${SAMPLE}.vep.csv | awk '{print $16,$5,$10,$11,$27,$26,$13,$43,$52,$7,$14,$1,$2}' > $DIR/S${SAMPLE}.IMPACT.vep.tsv &
    $PATHOGENIC $DIR/S${SAMPLE}.vep.csv | awk '{print $16,$5,$10,$11,$27,$26,$13,$43,$52,$7,$14,$1,$2}' > $DIR/S${SAMPLE}.PATHOGENIC.vep.tsv &
    $PROBPOS $DIR/S${SAMPLE}.vep.csv | awk '{print $16,$5,$10,$11,$27,$26,$13,$43,$52,$7,$14,$1,$2}' > $DIR/S${SAMPLE}.PROBPOS.vep.tsv &
done
