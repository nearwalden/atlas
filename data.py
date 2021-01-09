# routines for reading and writing data using atlas

import utils
import core

## returns the path for data in a dataset
def path (data, dataset):
	db = core.atlas_db()
	data_info = utils.get_data (data, dataset)
	dataset_info = utils.get_dataset (dataset)
	# not sure how to decide which dataset to pick
	datastore_info = util.get_datastore (dataset_info['datastore'][0])
	return datastore_info['poth'] + dataset_info['path'] + data_info['path']
	
# Called before writing out a data structure.  This should do versioning, but 
#   for now just overwrites
# also should add date/time written
def writing (data, data_object):
	# for now just save the data_info
	db = core.atlas_db()
	# check current count, just warn
	unique_name = core.make_unique_name (data['name'], data['dataset'])
	count = db[coll].count_documents({'unique_name': unique_name})
	data['unique_name'] = unique_name
	db['data'].insert_one(data)
	# returns the path so you can use it
	return path (data, data['dataset'])
	