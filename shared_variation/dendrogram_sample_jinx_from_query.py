import argparse
from pymongo import MongoClient
from varnorm.varcharkey import VarCharKey
from jinx import jaccard_index
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import linkage
import numpy as np
import matplotlib
matplotlib.use('svg')
import matplotlib.pyplot as plt
import json

from pprint import pprint

parser = argparse.ArgumentParser(description='Query RVS annotations, create dendrograms of shared variation.')
parser.add_argument('--url', default="mongodb://localhost:27017", help='mongo db url')
parser.add_argument('--database', default="rvs_annotations", help='database')
parser.add_argument('--collection', default="default", help='database')
parser.add_argument('--query', required=True, help='mongo query')
parser.add_argument('--algorythm', required=True,choices = [ 'average','complete','ward','centroid','single','weighted'], help='choose algorythm to display')
parser.add_argument('--outfile', type=argparse.FileType('w'), required=True, help='file path and name')
#parser.add_argument('--plot', type=argparse.FileType('w'), required=True, help='SVG output')
args    = parser.parse_args()
 
# create mongo client
client  = MongoClient(args.url)
db      = client[args.database]
rvs_collection = db[args.collection]




 
sets = {}
for v in rvs_collection.find(json.loads(args.query)):
    for sample in v['samples']:
        if sample in sets:
            sets[sample].add(v['vkey'])
        else:
            sets[sample] = set([v['vkey'],])

# pprint(sets)    
# exit(0)
# sets = {}
# for sample in vcf_paths:
#     variants = vcf.Reader( open( vcf_paths[sample], 'r' ))
#     sets[sample] = set()
#     for v in variants:
#         if v.is_snp and len(v.FILTER) == 0:
#             for allele in v.ALT:
#                 sets[sample].add((v.CHROM, 
#                                   v.POS,
#                                   str(allele),
#                                   str(allele)))






                
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



# plot dendrograms
fig = plt.figure(figsize=(15,15))

fig.add_subplot()
linkage_matrix = linkage(rows,args.algorythm)

a = dendrogram(linkage_matrix,
color_threshold=1,
labels=keys,
show_leaf_counts=False,
leaf_font_size=5,
leaf_rotation=0.0,
orientation='left',
)
plt.savefig(args.outfile)
plt.close()
