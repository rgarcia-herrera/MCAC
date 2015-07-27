


for n in range(1,49):
    print "python vep_filter.py --input vcf/intersections/S%02d.bwa_ir_fb.norepeats.intersected.vep.csv --output vcf/intersections/S%02d.bwa_ir_fb.norepeats.intersected.vep.filtered.csv" % (n, n)
    print "python vep_filter.py --input vcf/intersections/S%02d.mistery.intersected.vep.csv --output vcf/intersections/S%02d.mistery.intersected.vep.filtered.csv" % (n, n)
