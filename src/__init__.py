# The general idea of our hypothesis

## The goal of this project is to reproduce the figures and
## findings of the experimenters. We anticipate we
## will be able to do this

# The natural unit of analysis for our study spike time

# The relevant data with our UoA is organized 
# in the files of the data repository across many different files, 
# Specifically the .res .pos and .clu files. 

## The way the data is organized is by rat (train), then
## in each Train file there are multiple different types of files 
## That contain different information. For example, the .res files 
## Store the the spike times and .clu contains the specific which cluster 
## Is associated with an event 
## There are other files with more descriptive information such as .xml
## Most of the files are formatted such that each line represents a single
## Data point


def load_positions(fname):
	"""
	The purpose of this function is to iterate through an ASCII file
	and return an array with all of the positions in the file

	Parameter fname: denotes the .pos file to be used to load positions

	Data in the .pos file is organized such that each line has two 
	Three digit numbers separated by space. 

	fname: denotes which file to iterate through
	return: a two dimensional array with positions stored in file
	"""


def load_spikes(fname):
	"""
	The purpose of this function is to create an array of spike times 
	from a certain tetrode and cluster

	Parameter fname: denotes the cluster file to be used to load spikes

	This function requires iterating or referencing the .clu files. We believe
	The data within the .clu files denotes specific clusters where an event occurred
	Whereas the number at the end of the file denotes the tetrode

	return: an array of the data in the file that we have just read through
	"""
	# Code below is a reference we will use to write this function and others
	# The main role of this function is to ge tthe tetrode by reading the path
	# Basename and then to iterate through the file to return an array with cluster info
	# spike_data = {}
	# for train in glob.glob("data/*"):
	#     train_name = path.basename(train)
	#     for cluster in glob.glob("data/train/*"):
	# 		cluster_name = path.basename(cluster)[0]
	#     	data = make_array(cluster)
	# 		ndata = {"cluster": cluster_name, "data": data}
	# 	    spike_data[train_name] = ndata

def load_events(event_type):
	"""
	The purpose of this function is to return all events from a specific
	Type of session whether that passive or active travel, or sleep. 

	Parameter event_type: this string parameter denotes which type of events the
	user wants returns

	Return: Loads all events of the type of session, in array format
	"""

	# This function will reference the .cat.evt file to find out the beginning 
	# and end times for each type of session
	# It will then use these times to iterate through other files to find all of the events
	# That correspond to these times
	# It will then save this data to an array (probably multidimensional) and once
	# It finishes iterating it will return this array 

