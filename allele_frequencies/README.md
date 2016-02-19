# samples.py

This file has a list with the VCFs to consider while using the following tables.



## variants vs samples table
This script is run thusly:

    python variants_samples.py


It will print to stdout all variants as rows, all samples as columns.

Cells contain 0 if a sample doesn't have a variant, 1 if it is heterozygous and 2 if it is homozygous.


## Allele frequencies table

This script is run like this:

    python groupAF_vs_gmaf.py


It will output to stdout a semicolon separated list. Rows are
variants, there are columns for homozygous and heterozygous variants
found in samples.