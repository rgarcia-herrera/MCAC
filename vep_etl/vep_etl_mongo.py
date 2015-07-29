import argparse
import json
import pymongo
from bson.objectid import ObjectId
from pprint import pprint
from os import path


parser = argparse.ArgumentParser(description='Load Variant Effect Prediction JSON file to MongoDB.')
parser.add_argument('--url', default='mongodb://localhost:27017/', help="MongoDB URL, default: mongodb://localhost:27017/")
parser.add_argument('--veps', type=argparse.FileType('r'), nargs="+", required=True, help='one or more VEP JSON files')
args = parser.parse_args()


client = pymongo.MongoClient(args.url)
mcac   = client.mcac
veps   = mcac.veps


for f in args.veps:
    predictions = []
    for l in f.readlines():
        p = json.loads(l)
        del(p['input'])
        p['vep_json'] = path.abspath(f.name)
        predictions.append(p)
    result = veps.insert_many(predictions)
