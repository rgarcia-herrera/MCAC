import vcf

from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import linkage
import numpy as np
import matplotlib
matplotlib.use('svg')
import matplotlib.pyplot as plt

from samples import vcf_paths

# computes jacard index for two or mor sets
def jaccard_index(first, *others):
    return float( len( first.intersection(*others))) / float(len(first.union(*others)))


sets = {}

for sample in vcf_paths:
    variants = vcf.Reader( open( vcf_paths[sample], 'r' ))

    sets[sample] = set()
    for v in variants:
        if v.is_snp and len(v.FILTER) == 0:
            for allele in v.ALT:
                sets[sample].add((v.CHROM, 
                                  v.POS,
                                  str(allele),
                                  str(allele)))


# count intersections, place them in a table (rows are lists of cols)
keys = sorted(sets.keys())
rows = []
for i in keys:
    col = []
    for j in keys:
        if i==j:
            inter = 1
        else:
            inter = jaccard_index(sets[i], sets[j])
        col.append(inter)
    rows.append(col)


rows = np.array( rows )


algorythms = [ 'average',
               'complete',
               'ward',
               'centroid',
               'single',
               'weighted',]


for algorythm in algorythms:
        # plot dendrograms
        fig = plt.figure(figsize=(15,15))


        fig.add_subplot()
        linkage_matrix = linkage(rows, algorythm)

        a = dendrogram(linkage_matrix,
                       color_threshold=1,
                       labels=keys,
                       show_leaf_counts=False,
                       leaf_font_size=5,
                       leaf_rotation=0.0,
                       orientation='left',
               )
        plt.savefig('dendrogram_%s.svg' % algorythm)
        plt.close()
