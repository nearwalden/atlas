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




