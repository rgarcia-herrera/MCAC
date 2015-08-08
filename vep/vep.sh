VEP=~/software/ensembl-tools-release-79/scripts/variant_effect_predictor/variant_effect_predictor.pl

$VEP -i vcf/bwa_fb/S24.norepeats.vcf -o S01.json --json --everything --fork 24 --offline --assembly GRCh37


