# atlas parameters

import pymongo
import os
import yaml

# where is the mongo instance
# frost.local
MONGO_HOST = '192.168.20.10'
# MONGO_PORT = default

# mongo database
MONGO_DB = 'atlas'

# name of the yaml version of project info
PROJECT_FILE_YAML = 'project.yaml'

# directory to look for atlas stuff
ATLAS_DIR = "atlas/"

# maps type in file to right collection
TYPE_DICT = {'project': 'projects',
            'data': 'data',
            'datastore': 'datastores',
            'dataset': 'datasets'}

# return a new client
def mongo_client ():
    return pymongo.MongoClient(MONGO_HOST)
    
# return the atlas DB
def atlas_db ():
    client = mongo_client()
    return client[MONGO_DB]
    
def load_yaml (path):
    if os.path.exists(path):
        with open(path) as atlas_file:
            data = yaml.load(atlas_file, Loader=yaml.FullLoader)
            return data
    else:
        print ("No file in " + path)
        return None

    
# check number of items
def check_count (coll, name, count, db, data=False):
    if data:
        key = 'unique_name'
    else:
        key = 'name'
    real_count = db[coll].count_documents({key: name})
    if real_count != count:
        print ("Wrong number of items in " + coll + " with name=" + name + ": expected " + count + ", got " + real_count)
        error()
    return True
    
def make_unique_name (data, dataset):
    return dataset + ":" + data
    




