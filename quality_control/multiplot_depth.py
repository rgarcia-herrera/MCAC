genes = [
    'ABCC8', 'ABCC9', 'ACTC1', 'ACTN2', 'AKAP9', 'ANK2', 'ANKRD1', 'BAG3', 'CACNA1C', 'CACNA2D1', 'CACNB2',
    'CALM1', 'CALR3', 'CAMK2A', 'CASQ2', 'CAV3', 'CSRP3', 'DES', 'DLG1', 'DPP6', 'DSC2', 'DSG2', 'DTNA',
    'FGF12', 'GJA5', 'GJD4', 'GLA', 'GPD1L', 'HCN4', 'HEY2', 'JUP', 'KCNA5', 'KCND3', 'KCNE1', 'KCNE1L',
    'KCNE2', 'KCNE3', 'KCNH2', 'KCNJ2', 'KCNJ5', 'KCNJ8', 'KCNQ1', 'LAMP2', 'LDB3', 'LMNA', 'MYBPC3', 'MYH6',
    'MYH7', 'MYL2', 'MYL3', 'MYLK2', 'MYOZ2', 'MYPN', 'NEXN', 'NOS1AP', 'PKP2', 'PLN', 'PRKAG2', 'RANGRF',
    'RYR2', 'SCN10A', 'SCN1B', 'SCN2B', 'SCN3B', 'SCN4B', 'SCN5A', 'SLMAP', 'SNTA1', 'TAZ', 'TCAP', 'TGFB3',
    'TMEM43', 'TNNC1', 'TNNI3', 'TNNT2', 'TPM1', 'TRDN', 'TRPM4', 'TTN', 'TTR', 'VCL',
    ]

dirp = "/home/rgarcia/MCAC"
depth_files = ["%s/qc/depths/300/S%02d_realigned.bam.genes_depth.tsv" % (dirp, n) for n in [23,]]

depths = {}
for gene in genes:
    depths[gene] = {}
    
bins = []
for path in depth_files:
    with open(path, 'r') as f:
        for l in f.readlines():
            (gene, depth) = l.split()
            if path in depths[gene]:
                depths[gene][path].append(depth)
            else:
                depths[gene][path] = [depth,]

                
import matplotlib
matplotlib.use('agg')
import pylab as pl
import matplotlib.pyplot as plt

for gene in genes:
    plt.cla()
    for sample in depths[gene]:
        plt.plot(range(0,len(depths[gene][sample])),depths[gene][sample], '-')
    plt.savefig("%s.png" % gene)

