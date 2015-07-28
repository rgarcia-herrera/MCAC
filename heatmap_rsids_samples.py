import csv
import numpy as np
import matplotlib
matplotlib.use('svg')
import matplotlib.pyplot as plt
import existing_variation_make_uniq as IDs
from get_clinical_significances import get_clinical_significance

from pprint import pprint

bwa_mask  = "S%02d.bwa_ir_fb.norepeats.intersected.vep.filtered.csv"
directory = "/export/home/rgarcia/MCAC/vcf/intersections/filtered/"



varcount = {}
genes    = {}

for ID in IDs.all_ids:
    varcount[ID] = {}
    for sample in range(1, 49):
        archivo = directory + bwa_mask % sample
        with open(archivo, 'rb') as csvfile:
            vepreader = csv.reader(csvfile, delimiter='\t')
            header = vepreader.next()
            for row in vepreader:
                existing = row[7].split(',')
                if ID in existing:
                    genes[ID] = row[13]
                    if sample in varcount[ID]:
                        varcount[ID][sample] += 1
                    else:
                        varcount[ID][sample] = 1
    



rows = []
for ID in IDs.all_ids:
    cols = []
    for sample in range(1, 49):
        if sample in varcount[ID]:
            cols.append(1)
        else:
            cols.append(0)
    rows.append(cols)

with open('var_count_per_existing_variation_gt5.csv', 'wb') as csvfile:
    varwriter = csv.writer(csvfile, delimiter=',')
    varwriter.writerow(['ID', 'symbol', 'clinical_significance'] + range(1,49) )
    row = 0
    for ID in IDs.all_ids:
        clinical_significance = '-'
        if ID.startswith('rs'):
            clinical_significance = get_clinical_significance(ID)
            
        varwriter.writerow([ID, genes[ID], clinical_significance] + rows[row] )
        row += 1

