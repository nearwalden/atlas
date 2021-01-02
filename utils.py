# imports an atlas project



import core

#######################################################################
### Projects
#######################################################################

# import a project from the provided path

# path should have "/" at end, add check for this later
def create_project (path, db=None, path_is_dir=False):
	if db == None:
		db = core.atlas_db()
	# create the path to the file, only look for YAML now
	if path_is_dir:
		project_file_path = path + core.ATLAS_DIR + core.PROJECT_FILE_YAML
	else:
		project_file_path = path
	project_data = core.load_yaml (project_file_path)
	if ds_data['type'] != 'project':
		print ("Wrong type of data, expected 'datastore', got '" + ds_data['type'] + "'")
		return None
	core.check_count('projects', project_data['name'], 0, db)
	# write the project data
	db.projects.insert_one(project_data)
	return "created project"

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

# should be full path
def create_datastore (path, db=None):
	if db == None:
		db = core.atlas_db()
	ds_data = core.load_yaml(path)
	if ds_data['type'] != 'datastore':
		print ("Wrong type of data, expected 'datastore', got '" + ds_data['type'] + "'")
		return None
	# see if the project exists
	core.check_count ('datastores', ds_data['name'], 0, db)
	# write the project data
	db.datastores.insert_one(ds_data)
	return "created datastore"

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
	core.check_count ('datastores', name, 1, db)
	# delete project
	return db.datastores.find_one({'name': name})

#######################################################################
### Datasets
#######################################################################

# should be full path
def create_dataset (path, db=None):
	if db == None:
		db = core.atlas_db()
	ds_data = core.load_yaml(path)
	if ds_data['type'] != 'dataset':
		print ("Wrong type of data, expected 'dataset', got '" + ds_data['type'] + "'")
		return None
	# see if the project exists
	core.check_count ('datasets', ds_data['name'], 0, db)
	# write the project data
	db.datasets.insert_one(ds_data)
	return "created dataset"

# delete dataset, deletes everything to do within a dataset
# (right now only deletes the dataset)

def delete_dataset (name, db=None):
	# get a client if needed
	if db == None:
		db = core.atlas_db()
	# see if the project exists
	core.check_count ('datasets', name, 1, db)
	# delete project
	db.datasets.delete_one({'name': name})
	return True
	
# get dataset, returns None if not found

def get_dataset (name, db=None):
	# get a client if needed
	if db == None:
		db = core.atlas_db()
	# see if the project exists
	core.check_count ('datasets', name, 1, db)
	# delete project
	return db.datasets.find_one({'name': name})

#######################################################################
### Data
#######################################################################

# should be full path
def create_data (path, db=None):
	if db == None:
		db = core.atlas_db()
	data = core.load_yaml(path)
	if data['type'] != 'data':
		print ("Wrong type of data, expected 'data', got '" + data['type'] + "'")
		return None
	# see if the project exists
	unique_name = core.make_unique_name(data['name'], data['dataset'])
	core.check_count ('datasets', unique_name, 0, db, data=True)
	data['unique_name'] = unique_name
	# write the project data
	db.data.insert_one(data)
	return "created data record"

# delete dataset, deletes everything to do within a dataset
# (right now only deletes the dataset)

def delete_data (name, dataset, db=None):
	unique_name = core.make_unique_name (name, dataset)
	return delete_data_unique (unique_name, db)

def delete_data_unique  (unique_name, db=None):
	# get a client if needed
	if db == None:
		db = core.atlas_db()
	# see if the project exists
	core.check_count ('data', unique_name, 1, db, data=True)
	# delete project
	db.data.delete_one({'unique_name': unique_name})
	return True
	
# get dataset, returns None if not found

def get_data (name, dataset, db=None):
	unique_name = core.make_unique_name (name, dataset)
	return get_data_unique (unique_name, db)	
	
def get_data_unique (unique_name, db=None):
	# get a client if needed
	if db == None:
		db = core.atlas_db()
	# see if the project exists
	core.check_count ('data', unique_name, 1, db, data=True)
	# delete project
	return db.data.find_one({'unique_name': unique_name})
	

	

