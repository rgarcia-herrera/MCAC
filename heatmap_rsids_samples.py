import csv
import numpy as np
import matplotlib
matplotlib.use('svg')
import matplotlib.pyplot as plt
import existing_variation_make_uniq as IDs

from pprint import pprint

bwa_mask  = "S%02d.bwa_ir_fb.norepeats.intersected.vep.filtered.csv"
directory = "/export/home/rgarcia/MCAC/vcf/intersections/filtered/"


score_threshold = 5

varcount = {}

for ID in IDs.all_ids:
    varcount[ID] = {}                
    for sample in range(1, 49):
        archivo = directory + bwa_mask % sample
        with open(archivo, 'rb') as csvfile:
            vepreader = csv.reader(csvfile, delimiter='\t')
            header = vepreader.next()
            for row in vepreader:
                if int(row[0]) >= score_threshold:
                    existing = row[7].split(',')
                    if ID in existing:
                        if sample in varcount[ID]:
                            varcount[ID][sample] += 1
                        else:
                            varcount[ID][sample] = 1
    

pprint(varcount)
                                            
# rows = []
# for sample in range(1, 49):
#     cols = []
#     for gene in genes:
#         if gene in varcount[sample]:
#             heat = len(varcount[sample][gene])
#         else:
#             heat = 0
#         cols.append(heat)
#     rows.append(cols)


# with open('var_count_per_sample_score_gt5.csv', 'wb') as csvfile:
#     varwriter = csv.writer(csvfile, delimiter=',')
#     varwriter.writerow(['S'] + genes )
#     for row in range(len(rows)):
#         varwriter.writerow([row+1] + rows[row] )
    

