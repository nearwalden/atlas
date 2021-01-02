# Looks at all of the files in a directory and decides what to do

# Only looks at things are there - does not make any judgements if things are not there

import glob
import core

# import everything, report anything that wasn't imported

def import_dir (path, db=None):
	# get a database if needed
	if db == None:
		db = core.atlas_db()
	total = 0
	imports = 0
	# grab list of files
	for yamlfile in glob.glob(path + "*.yaml"):
		print ("Processing " + yamlfile)
		total += 1
		# read file, punt if not there
		data = core.load_yaml(yamlfile)
		# if found
		if data == None:
			print ("Could not find valid yaml data at : " + yamlfile)
			return None
		# check if exists already
		coll = core.TYPE_DICT[data['type']]
		if data['type'] == 'data':
			unique_name = core.make_unique_name (data['name'], data['dataset'])
			count = db[coll].count_documents({'unique_name': unique_name})
			data['unique_name'] = unique_name
		else:
			count = db[coll].count_documents({'name': data['name']})			
		if count == 0:
			db[coll].insert_one(data)
			imports += 1
		else:
			print ("Name '" + data['name'] + "' in file " + yamlfile + " already exists, ignoring.")
	print ("Total files = " + str(total) + ", imported = " + str(imports))
	return True
