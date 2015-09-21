select variants.sample,
       variants.chrom,
       variants.start,
       missense_variant.gene_symbol,
       missense_variant.polyphen_prediction,
       missense_variant.sift_prediction
  from variants 
  join missense_variant
       on missense_variant.variant_id = variants.id
  where variants.chrom="X"
  order by variants.start,variants.sample; 
