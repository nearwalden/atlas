# imports an atlas project

import pymongo
import yaml
import os
import core


# import a project from the provided path

# path should have "/" at end, add check for this later
def create_project (path, client=None):
	if client == None:
		client = core.mongo_client()
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
	db = client[core.MONGO_DB]
	# see if the project exists
	project = db.projects.find_one({'name': project_data['name']})
	if project != None:
		return "Project already exists:  " + project_data['name']
	# write the project data
	db.projects.insert_one(project_data)
	return "imported project"
	

	
