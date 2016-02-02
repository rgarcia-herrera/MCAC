import argparse
from pymongo import MongoClient
from varnorm.varcharkey import VarCharKey
import pickle
from rvs_ann import rvs_annotate
from time import sleep
from pprint import pprint

parser = argparse.ArgumentParser(description='Get vkeys from pickle, get annotations from RVS, load them to mongo.')
parser.add_argument('--url', default="mongodb://localhost:27017", help='mongo db url')
parser.add_argument('--database', default="rvs_annotations", help='database')
parser.add_argument('--collection', default="default", help='database')
parser.add_argument('--pickle', type=argparse.FileType('r'), required=True, help='pickle with vkeys dict sorted by resource')
args    = parser.parse_args()

# create mongo client
client  = MongoClient(args.url)
db      = client[args.database]
rvs_collection = db[args.collection]


resources = [u'frequency', u'disease', u'prediction', u'impact']

vkeys=pickle.load(args.pickle)

for resource in resources:
    for n in range(0,len(vkeys[resource]),30):
        batch = list(vkeys[resource])[n:n+29]

        for ann in rvs_annotate( batch, resource ):
            ann[u'samples']  = vkeys['samples']
            ann[u'resource'] = resource
            key ={'chr'      : ann.get('chr', None),
                  'start'    : ann.get('start', None),
                  'end'      : ann.get('end', None),
                  'alt'      : ann.get('alt', None),
                  'vkey'     : ann['vkey'],
                  'samples'  : vkeys['samples'],
                  'resource' : resource}            
            rvs_collection.update(key,ann,upsert=True)

        print n
        sleep(10)
    
