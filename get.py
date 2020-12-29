# Get data

import pymongo
import core

# get project, returns None if not found

def get_project (name, client=None):
    # get a client if needed
    if client == None:
        client = core.mongo_client()
    # check if exists, return False if not
    db = client[core.MONGO_DB]
	# see if the project exists
    count = db.projects.count_documents({'name': name})
    if count != 1:
        print ("Wrong number of projects with name=" + name + ": " + count)
        return None
    # delete project
    return db.projects.find_one({'name': name})
    
