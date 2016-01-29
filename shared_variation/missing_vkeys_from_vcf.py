import argparse
from pymongo import MongoClient
import vcf
from varnorm.varcharkey import VarCharKey
import pickle
from pprint import pprint



parser = argparse.ArgumentParser(description='Create pickle with RVS annotations missing in mongo from variants in VCF.')
parser.add_argument('--vcf', type=argparse.FileType('r'), required=True, help='vcf file to annotate')
parser.add_argument('--url', default="mongodb://localhost:27017", help='mongo db url')
parser.add_argument('--database', default="rvs_annotations", help='database')
parser.add_argument('--collection', default="default", help='database')
parser.add_argument('--outpickle', type=argparse.FileType('w'), required=True, help='will create a pickle with missing vkeys')
args    = parser.parse_args()

# create mongo client
client  = MongoClient(args.url)
db      = client[args.database]
rvs_collection = db[args.collection]

# init output dict
resources = [u'frequency', u'disease', u'prediction', u'impact']
missing_vkeys={resource: set() for resource in resources}

# query for annotated variants from vcf
vcfr = vcf.Reader( args.vcf )
for v in vcfr:
    if len(v.FILTER)==0:
        for alt in v.ALT:
            chrom = v.CHROM.replace('chr','')
            start = v.POS
            alt = str(alt)
            
            if v.is_snp or (not v.is_deletion and v.is_indel):
                # snps or insertions
                end = v.POS
            elif v.is_deletion:
                end = v.POS + (len(v.REF) - len(alt))

            vkey = VarCharKey.v2k(chrom, start, end, alt)
            
            for resource in resources:
                # for n in  rvs_collection.find({'chr'      : str(chrom),
                #                                'start'    : str(start),
                #                                'end'      : str(end),
                #                                'alt'      : alt,}):
                #                                #'vkey'     : vkey,
                #                                # 'samples'  : {'$in': vcfr.samples},
                #                                #'resource' : resource}):
                #     pprint(n)
                if rvs_collection.count({ 'vkey'     : vkey,
                                          'samples'  : {'$in': vcfr.samples},
                                          'resource' : resource}) == 0:
                    missing_vkeys[resource].add(vkey)

missing_vkeys[u'samples'] = vcfr.samples
pickle.dump(missing_vkeys, args.outpickle)

