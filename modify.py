# Edit, modify, delete objects

import pymongo
import core

# delete project, deletes everything to do with a project
# (right now only deletes the project)

def delete_project (name, client=None):
    # get a client if needed
    if client == None:
        client = core.mongo_client()
    # check if exists, return False if not
    db = client[core.MONGO_DB]
	# see if the project exists
    count = db.projects.count_documents({'name': name})
    if count != 1:
        return "Wrong number of projects with name=" + name + ": " + count
    # delete project
    db.projects.delete_one({'name': name})
    return True


    
    
