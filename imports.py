# imports an atlas project

import pymongo
import yaml
import os
import params

client = pymongo.MongoClient(params.MONGO_HOST)

# import a project from the provided path

# path should have "/" at end, add check for this later
def import_proj (path):
	# check if path exists
	if not os.path.exists(path):
		return "Path doesn't exist"
	# create the path to the file, only look for YAML now
	project_file_path = path + params.PROJECT_FILE_YAML
	if os.path.exists(project_file_path):
		with open(project_file_path) as project_file:
			project_data = yaml.load(project_file, Loader=yaml.FullLoader)
	else:
		return "No project file in " + path
	# see if the project exists
	dbs = client.list_databases()
	if project_data['name'] in dbs:
		if new:
			return "Project already exists:  " + project_data.shortname
	db = client[project_data['name']]
	# write the project data
	proj = db.project
	proj.insert_one(project_data)
	return "loaded project"
	

