"""
Create BAM files for the BED regions from the Complete Genomics evidence files.
"""

from sh import cgatools, samtools


evidence_files = {
    'JATE' : '/mnt/amerindios/b/GS000033657-DID/GS000033832-ASM/GS02379-DNA_A01/ASM/EVIDENCE/evidenceDnbs-%s-GS000033832-ASM.tsv.bz2',
    'PTL'  : '/mnt/amerindios/b/GS000033658-DID/GS000033833-ASM/GS02379-DNA_B01/ASM/EVIDENCE/evidenceDnbs-%s-GS000033833-ASM.tsv.bz2',
    'JPAM' : '/mnt/amerindios/a/GS000033659-DID/GS000033834-ASM/GS02379-DNA_C01/ASM/EVIDENCE/evidenceDnbs-%s-GS000033834-ASM.tsv.bz2',
    'LACA' : '/mnt/amerindios/a/GS000033660-DID/GS000033835-ASM/GS02379-DNA_D01/ASM/EVIDENCE/evidenceDnbs-%s-GS000033835-ASM.tsv.bz2',
    'JIAT' : '/mnt/amerindios/a/GS000033661-DID/GS000033836-ASM/GS02379-DNA_E01/ASM/EVIDENCE/evidenceDnbs-%s-GS000033836-ASM.tsv.bz2', 
}

output_mask = "/home/rgarcia/MCAC/sam/complete/%s_%s.bam"
reference   = '/mnt/f/rgarcia/MCAC/reference/ucsc.hg19.crr'



with open('/home/rgarcia/MCAC/targets/haloplex_genes_ensembl_GRCh37_no_patch_padded.bed') as f:
    for l in f.readlines():
        (chrom, start, end, symbol) = l.split()
        chrom = "chr%s" % chrom

        for sample in evidence_files:
            samtools.sort( cgatools.evidence2sam( beta          = True,
                                                  reference     = reference,
                                                  evidence_dnbs = evidence_files[sample] % chrom,
                                                  extract_genomic_region = "%s,%s,%s" % (chrom,start,end),
                                                  keep_duplicates        = True,
                                                  _piped                 = True ),
                           "-", O='bam', T='/scratch/tmp',
                           o=output_mask % (sample, symbol))
