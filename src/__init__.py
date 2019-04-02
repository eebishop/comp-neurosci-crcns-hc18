# The general idea of our hypothesis

## The goal of this project is to reproduce the figures and
## findings of the experimenters. We anticipate we
## will be able to do this

# The natural unit of analysis for our study

## We have determined that the UoA for this project 
## will be cluster

# How the relevant data with our UoA is organized 
# in the files of the data repository

## The way the data is organized is by rat (train), then
## in each Train file there are eight .clu files 
## which have different numbers identifying the session
## that is recorded
## Within these files is the data that can be analyzed
## Each data point is one line in the file


def make_array(fname):
	"""
	The purpose of this function is to iterate through an ascii file
	and return an array with all of the values in the file
	fname: denotes which file to iterate through
	return: an array with values stored in file
	"""
	with open(fname, "rt") as fp:
		return [np.fromstring(line, sep="\n") for line in fp]


def load_data():
	"""
	The purpose of this function is to create an array of the data in each
	individual session
	return: an array of the data in the file that we have just read through
	"""
	spike_data = {}
	for train in glob.glob("data/*"):
	    train_name = path.basename(train)
	    for cluster in glob.glob("data/train/*"):
			cluster_name = path.basename(cluster)[0]
	    	data = make_array(cluster)
			ndata = {"cluster": cluster_name, "data": data}
		    spike_data[train_name] = ndata



