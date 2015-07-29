template = """#!/bin/bash

DIR=%(DIR)s
INTERVALS=$DIR/`basename %(SAM)s .bam`.intervals

echo "creating intervals file"
echo $INTERVALS
java -Xmx1g -jar %(GATK)s \\
    -T RealignerTargetCreator \\
    -R %(REF)s \\
    -I %(SAM)s \\
    --known %(KNOWN)s \\
    -dt NONE \\
    -o $INTERVALS

echo "realigning"
BAMOUT=$DIR/`basename $SAM .bam`_realigned.bam
java -jar %(GATK)s \\
     -T IndelRealigner \\
     -R %(REF)s \\
     -I %(SAM)s \\
     -dt NONE \\
     -targetIntervals $INTERVALS \\
     -o $BAMOUT
"""

sampath    = "/export/home/rgarcia/MCAC/sam_miseq_hg19/S%02i_rg.bam"
scriptpath = "/export/home/rgarcia/MCAC/jobs/indel_realign_S%02i.sh"

for n in range(1,49):
    sam = sampath % n
    script = open(scriptpath % n, 'w')

    script.write( template % {
        'SAM'   : sam,
        'DIR'   : '/export/home/rgarcia/MCAC/sam_miseq_hg19',
        'GATK'  : '/export/home/rgarcia/software/GenomeAnalysisTK.jar',
        'REF'   : '/export/home/rgarcia/MCAC/reference/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFASTA/genome.fa',
        'KNOWN' : '/export/home/rgarcia/MCAC/reference/1000G_phase1.indels.b37.vcf.gz'
    })
    script.close()
