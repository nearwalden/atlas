# atlas parameters

import pymongo

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

# return a new client
def mongo_client ():
    return pymongo.MongoClient(MONGO_HOST)
    
# return the atlas DB
def atlas_db ():
    client = mongo_client()
    return client[MONGO_DB]
    
# check number of items
def check_count (coll, name, count, db):
    real_count = db[coll].count_documents({'name': name})
    if real_count != count:
        print ("Wrong number of items in " + coll + " with name=" + name + ": expected " + count + ", got " + real_count)
        error()
    return True




