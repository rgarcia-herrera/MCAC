
python vep2csv_alpha_filter.py ../vcf/complete/A01.JATE.vep.csv | cut -f 16 | sort -u > ../vcf/complete/gene_lists/JATE_alpha_genes.txt &
python vep2csv_alpha_filter.py ../vcf/complete/B01.PTL.vep.csv  | cut -f 16 | sort -u > ../vcf/complete/gene_lists/PTL_alpha_genes.txt &
python vep2csv_alpha_filter.py ../vcf/complete/C01.JPAM.vep.csv | cut -f 16 | sort -u > ../vcf/complete/gene_lists/JPAM_alpha_genes.txt &
python vep2csv_alpha_filter.py ../vcf/complete/D01.LACA.vep.csv | cut -f 16 | sort -u > ../vcf/complete/gene_lists/LACA_alpha_genes.txt &
python vep2csv_alpha_filter.py ../vcf/complete/E01.JIAT.vep.csv | cut -f 16 | sort -u > ../vcf/complete/gene_lists/JIAT_alpha_genes.txt &


python vep2csv_beta_filter.py ../vcf/complete/A01.JATE.vep.csv | cut -f 16 | sort -u > ../vcf/complete/gene_lists/JATE_beta_genes.txt &
python vep2csv_beta_filter.py ../vcf/complete/B01.PTL.vep.csv  | cut -f 16 | sort -u > ../vcf/complete/gene_lists/PTL_beta_genes.txt &
python vep2csv_beta_filter.py ../vcf/complete/C01.JPAM.vep.csv | cut -f 16 | sort -u > ../vcf/complete/gene_lists/JPAM_beta_genes.txt &
python vep2csv_beta_filter.py ../vcf/complete/D01.LACA.vep.csv | cut -f 16 | sort -u > ../vcf/complete/gene_lists/LACA_beta_genes.txt &
python vep2csv_beta_filter.py ../vcf/complete/E01.JIAT.vep.csv | cut -f 16 | sort -u > ../vcf/complete/gene_lists/JIAT_beta_genes.txt &
