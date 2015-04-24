from sh import ls, uniq, glob
import os


plots   = set()
samples = set()
for img in ls(glob("qc/html/*/images_qualimapReport/*png")):
    plots.add(os.path.basename(img.strip()))
    samples.add(os.path.dirname(img).split('/')[2])


print """
<html>
<body>
<table>
<thead>
<tr>
<th>sample</th>
"""

for plot in plots:
    print "<th> %s </th>" % " ".join(plot.replace('.png','').split('_'))
print """
</tr></thead>
<tbody>
"""


width = "200px"
    
for sample in samples:
    print "<tr><th>%s</th>" % sample
    for plot in plots:
        print "<td><img src='html/%s/images_qualimapReport/%s' width='%s'></td>" % ( sample, plot.strip(), width )
    print "</tr>"

print """
</tbody>
</table>
</body>
</html>
"""
