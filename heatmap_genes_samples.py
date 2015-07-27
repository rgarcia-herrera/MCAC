import csv
import numpy as np
import matplotlib
matplotlib.use('svg')
import matplotlib.pyplot as plt

from pprint import pprint

genes = ['ABCC8', 'ABCC9', 'ACTC1', 'AKAP9', 'ANK2', 'BAG3', 'CACNA1C', 'CACNA2D1', 'CACNB2', 'CALR3', 'CAMK2A', 'CASQ2',
         'CAV3', 'CTD-3222D19.2', 'DES', 'DLG1', 'DPP6', 'DSC3', 'DSG2', 'DTNA', 'GLA', 'HCN4', 'JUP', 'KCNA5', 'KCNH2',
         'KCNQ1', 'LDB3', 'LMNA', 'MADD', 'MYBPC3', 'MYH6', 'MYH7', 'MYLK2', 'MYOZ2', 'MYPN', 'NEXN', 'NOS1AP', 'PKP2',
         'PRKAG2', 'RANGRF', 'RP11-729I10.2', 'RYR2', 'SCN10A', 'SCN1B', 'SCN5A', 'SLMAP', 'SSUH2', 'TAZ', 'TCAP', 'TNNI3',
         'TPM1', 'TRDN', 'TRPM4', 'TTN', 'TTN-AS1', 'VCL', 'WWTR1',]

bwa_mask  = "S%02d.bwa_ir_fb.norepeats.intersected.vep.filtered.csv"
directory = "/export/home/rgarcia/MCAC/vcf/intersections/filtered/"


score_threshold = 5

varcount = {}

for sample in range(1, 49):
    archivo = directory + bwa_mask % sample

    varcount[sample] = {}                

    with open(archivo, 'rb') as csvfile:
        vepreader = csv.reader(csvfile, delimiter='\t')
        header = vepreader.next()
        for row in vepreader:
            if int(row[0]) >= score_threshold:
                for gene in genes:
                    if row[13] == gene:
                        if gene in varcount[sample]:
                            varcount[sample][gene].add((row[5], row[15]))
                        else:
                            varcount[sample][gene] = set([(row[5], row[15]),])



                                            
rows = []
for sample in range(1, 49):
    cols = []
    for gene in genes:
        if gene in varcount[sample]:
            heat = len(varcount[sample][gene])
        else:
            heat = 0
        cols.append(heat)
    rows.append(cols)


with open('var_count_per_sample_score_gt5.csv', 'wb') as csvfile:
    varwriter = csv.writer(csvfile, delimiter=',')
    varwriter.writerow(['S'] + genes )
    for row in range(len(rows)):
        varwriter.writerow([row+1] + rows[row] )
    



    
# rows          = np.array( rows )

# column_labels = range(1,49)
# row_labels    = genes

# data = np.array( rows )

# fig, ax = plt.subplots()
# heatmap = ax.pcolor(data, cmap='summer', picker=True)

# # Format
# fig = plt.gcf()
# fig.set_size_inches(16, 13)
# # put the major ticks at the middle of each cell
# ax.set_xticks(np.arange(data.shape[0])+0.5, minor=False)
# ax.set_yticks(np.arange(data.shape[1])+0.5, minor=False)

# # want a more natural, table-like display
# ax.invert_yaxis()
# ax.xaxis.tick_top()
# ax.set_xticklabels(row_labels, minor=False, fontsize=8)
# ax.set_yticklabels(column_labels, minor=False, fontsize=8)

# # plt.show()
# plt.xticks(rotation=90)
# plt.colorbar(heatmap, orientation="vertical")
# plt.savefig('heatmap.png')
