BED=/home/rgarcia/MCAC/targets/Miocardiopatias_y_canalopatias_AllTracks.bed
DIR=/home/rgarcia/MCAC/vcf/complete

vcftools --vcf $DIR/A01.JATE.vcf --bed $BED --recode --stdout > $DIR/A01.JATE.haloplex.vcf &
vcftools --vcf $DIR/B01.PTL.vcf --bed $BED --recode --stdout > $DIR/B01.PTL.haloplex.vcf &
vcftools --vcf $DIR/C01.JPAM.vcf --bed $BED --recode --stdout > $DIR/C01.JPAM.halople.vcf &
vcftools --vcf $DIR/D01.LACA.vcf --bed $BED --recode --stdout > $DIR/D01.LACA.halople.vcf &
vcftools --vcf $DIR/E01.JIAT.vcf --bed $BED --recode --stdout > $DIR/E01.JIAT.halople.vcf &
