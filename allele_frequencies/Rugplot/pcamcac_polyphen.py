import csv
import numpy as np
import svgwrite, random
from rugplot import CircleMarker, Scatter
from itertools import combinations

from pprint import pprint

lines = open("datos_filtrados.csv", "r").readlines()

cons = []
poly = []
gmaf = []
afr = []
amr = []
eas = []
eur = []
sas = []
f_al = []
poly_2 = []


for line in lines[1:]:
    sep = line.strip().split(",")
    cons.append(sep[0])
    poly.append(sep[1])
    gmaf.append(sep[2][2:])
    afr.append(sep[3][2:])
    amr.append(sep[4][2:])
    eas.append(sep[5][2:])
    eur.append(sep[6][2:])
    sas.append(sep[7][2:])
    f_al.append(sep[8])



for letra in poly:
    temp = letra.strip().split("(")
    poly_2.append(temp[0])


#colors = ['olivedrab', 'navajowhite',
          #'indigo', 'tan',
          #'slategrey', 'palegreen',
          #'maroon', 'brown',
          #'lightsteelblue', 'khaki', ]
   
polyphen_color = {
    'probably_damaging': 'red',
    'benign': 'green', 'possibly_damaging': 'brown', 'unknown': 'navajowhite'  
    }

color_poly = []
for a in poly_2:   
    color_poly.append(polyphen_color[a])


reader = csv.reader(open('datos_filtrados_final.csv'))
reader.next()
pca = [list() for n in range(7)]
markers = []
i=0
for l in reader:
    markers.append(CircleMarker(r=2.5, fill=color_poly[i]))
    i += 1
    for n in range(2,9):
        pca[n-2].append(float(l[n]))



npca = []
for c in pca:
    tmp = np.array(c)
    tmp *= 1.0/tmp.max()
    npca.append(tmp)

frame_size = 200
dash_size = 10
jump = frame_size + dash_size

rug = svgwrite.Drawing('pcamcac_polyphen.svg')
pairs = []
for i,j in combinations(range(7), 2):
    s = Scatter(npca[i], npca[j], markers, insert=(i*jump,j*jump), size=(frame_size, frame_size))
    s.drawBorder(stroke='grey', fill='white', stroke_width=0.8)
    s.drawMarkers()
    s.drawDotDash(['w','e','s','n'], dash_height=5, stroke="grey", stroke_width=0.2)
    rug.add(s.dwg)

rug.save()


