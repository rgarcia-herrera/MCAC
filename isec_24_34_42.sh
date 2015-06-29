python vep_intersect.py --files vcf_basespace/vep/S24_vep.csv vcf_basespace/vep/S34_vep.csv --intersection isec_24_34.csv
python vep_intersect.py --files vcf_basespace/vep/S24_vep.csv vcf_basespace/vep/S42_vep.csv --intersection isec_24_42.csv
python vep_intersect.py --files vcf_basespace/vep/S34_vep.csv vcf_basespace/vep/S42_vep.csv --intersection isec_34_42.csv
python vep_intersect.py --files vcf_basespace/vep/S24_vep.csv vcf_basespace/vep/S34_vep.csv vcf_basespace/vep/S42_vep.csv --intersection isec_24_34_42.csv

