import numpy as np

home = '/home/rgarcia/MCAC/qc/depths/500'

depths = {}
for s in range(1,49):
    depths[s] = {}
    with open("%s/S%02d_realigned.bam.genes_depth.tsv" % (home,s)) as f:
        for l in f.readlines():
            (gene, depth) = l.split()
            if gene in depths[s]:
                depths[s][gene].append(int(depth))
            else:
                depths[s][gene] = [int(depth), ]


for s in depths:
    for gene in depths[s]:
        a = np.array(depths[s][gene])
        print s, gene, a.mean(), a.std(), a.max(), a.min()
