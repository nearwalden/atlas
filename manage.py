# imports an atlas project

import pymongo
import yaml
import os
import core

#######################################################################
### Projects
#######################################################################

# import a project from the provided path

# path should have "/" at end, add check for this later
def create_project (path, db=None):
	if db == None:
		db = core.atlas_db()
	# check if path exists
	if not os.path.exists(path):
		return "Path doesn't exist"
	# create the path to the file, only look for YAML now
	project_file_path = path + core.ATLAS_DIR + core.PROJECT_FILE_YAML
	if os.path.exists(project_file_path):
		with open(project_file_path) as project_file:
			project_data = yaml.load(project_file, Loader=yaml.FullLoader)
	else:
		return "No project file in " + path
	core.check_count('projects', project_data['name'], 0, db)
	# write the project data
	db.projects.insert_one(project_data)
	return "imported project"

# delete project, deletes everything to do with a project
# (right now only deletes the project)

def delete_project (name, db=None):
	# get a client if needed
	if db == None:
		db = core.atlas_db()
	core.check_count('projects', name, 1, db)
	# delete project
	db.projects.delete_one({'name': name})
	return True
	
# get project, returns None if not found

def get_project (name, db=None):
	# get a client if needed
	if db == None:
		db = core.atlas_db()
	core.check_count('projects', name, 1, db)
	# delete project
	return db.projects.find_one({'name': name})
	
#######################################################################
### Datastores
#######################################################################

# path should have "/" at end, add check for this later
def create_datastore (path, db=None):
	if db == None:
		db = core.atlas_db()
	# check if path exists
	if not os.path.exists(path):
		return "Path doesn't exist"
	else:
		with open(path) as ds_file:
			ds_data = yaml.load(ds_file, Loader=yaml.FullLoader)
	# see if the project exists
	core.check_count ('datastores', ds_data['name'], 0, db)
	# write the project data
	db.datastores.insert_one(ds_data)
	return "imported project"

# delete project, deletes everything to do with a project
# (right now only deletes the project)

def delete_datastore (name, db=None):
	# get a client if needed
	if db == None:
		db = core.atlas_db()
	# see if the project exists
	core.check_count ('datastores', name, 1, db)
	# delete project
	db.datastores.delete_one({'name': name})
	return True
	
# get project, returns None if not found

def get_datastore (name, db=None):
	# get a client if needed
	if db == None:
		db = core.atlas_db()
	# see if the project exists
	check_count ('datastores', name, 1, db)
	# delete project
	return db.datastore.find_one({'name': name})

#######################################################################
### Datasets
#######################################################################


#######################################################################
### Data
#######################################################################


	

	

