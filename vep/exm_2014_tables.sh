#!/bin/bash

HALOPLEX="python /home/rgarcia/MCAC/vep/vep2csv_filter_haloplex_genes.py"

FRAMESHIFT="python /home/rgarcia/MCAC/vep/vep2csv_frameshift.py"
IMPACT="python /home/rgarcia/MCAC/vep/vep2csv_impact.py"
PATHOGENIC="python /home/rgarcia/MCAC/vep/vep2csv_pathogenic.py"
PROBPOS="python /home/rgarcia/MCAC/vep/vep2csv_prob_poss_del.py"

FRAMESHIFT_H="python /home/rgarcia/MCAC/vep/vep2csv_frameshift_et_haloplex.py"
IMPACT_H="python /home/rgarcia/MCAC/vep/vep2csv_impact_et_haloplex.py"
PATHOGENIC_H="python /home/rgarcia/MCAC/vep/vep2csv_pathogenic_et_haloplex.py"
PROBPOS_H="python /home/rgarcia/MCAC/vep/vep2csv_prob_poss_del_et_haloplex.py"



for CSV in `find /home/rgarcia/MCAC/vcf/exm_illumina -iname '*csv' | sort`
do
    DIROUT=`dirname $CSV`
    OUT=`basename $CSV .csv`
    
    $HALOPLEX $CSV | awk '{print $16,$5,$10,$11,$27,$26,$13,$43,$52,$7,$14,$1,$2}' > $DIROUT/${OUT}.HALOPLEX.tsv &

    $FRAMESHIFT $CSV | awk '{print $16,$5,$10,$11,$27,$26,$13,$43,$52,$7,$14,$1,$2}' > $DIROUT/${OUT}.FRAMESHIFT.tsv &
    $IMPACT $CSV | awk '{print $16,$5,$10,$11,$27,$26,$13,$43,$52,$7,$14,$1,$2}' > $DIROUT/${OUT}.IMPACT.tsv &
    $PATHOGENIC $CSV | awk '{print $16,$5,$10,$11,$27,$26,$13,$43,$52,$7,$14,$1,$2}' > $DIROUT/${OUT}.PATHOGENIC.tsv &
    $PROBPOS $CSV | awk '{print $16,$5,$10,$11,$27,$26,$13,$43,$52,$7,$14,$1,$2}' >  $DIROUT/${OUT}.PROBPOS.tsv &

    $FRAMESHIFT_H $CSV | awk '{print $16,$5,$10,$11,$27,$26,$13,$43,$52,$7,$14,$1,$2}' > $DIROUT/${OUT}.FRAMESHIFT.HLPLX.tsv &
    $IMPACT_H $CSV | awk '{print $16,$5,$10,$11,$27,$26,$13,$43,$52,$7,$14,$1,$2}' > $DIROUT/${OUT}.IMPACT.HLPLX.tsv &
    $PATHOGENIC_H $CSV | awk '{print $16,$5,$10,$11,$27,$26,$13,$43,$52,$7,$14,$1,$2}' > $DIROUT/${OUT}.PATHOGENIC.HLPLX.tsv &
    $PROBPOS_H $CSV | awk '{print $16,$5,$10,$11,$27,$26,$13,$43,$52,$7,$14,$1,$2}' >  $DIROUT/${OUT}.PROBPOS.HLPLX.tsv &

    
done
