def jaccard_index(first, *others):
    """
    computes jacard index for two or mor sets
    """
    return float( len( first.intersection(*others))) / float(len(first.union(*others)))
