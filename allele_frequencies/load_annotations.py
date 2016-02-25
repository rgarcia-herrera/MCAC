"""
This script will load frequency annotations from json files into a mongodb cache.
"""

import argparse
import json
from pymongo import MongoClient
from pprint import pprint


parser = argparse.ArgumentParser(description='Read JSON files, load them to mongo.')
parser.add_argument('--url', default="mongodb://localhost:27017", help='mongo db url')
parser.add_argument('--database', default="rvs_annotations", help='database')
parser.add_argument('--collection', default="cache", help='collection')
parser.add_argument('jsons', type=argparse.FileType('r'), nargs="+", help='json file(s) with annotations to load')
args    = parser.parse_args()



# create mongo client
client  = MongoClient(args.url)
db      = client[args.database]
rvs_collection = db[args.collection]

for j in args.jsons:
    annotations = json.load(j)
    rvs_collection.insert_many(annotations)
