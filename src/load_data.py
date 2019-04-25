# loading data

import pandas as pd
import glob
from os import path 

def make_arr(fname):
	"""
	The purpose of this function is to create an array from the data in a file in flat ascii format

	ONLY WORKS FOR CLU AND RES FILES
	"""
	arr = []
	with open(fname, "rt") as fp:
		arr.append(np.fromstring(line, sep = "\n") for line in fp

def make_arr_pos(pos_file):
	"""
	The purpose of this function is to create an array from the data in the .pos files
	"""
	arr = []
	with open(fname, "rt") as fp:
		for line in fp:
			arr.append([line[0, 2], line[2, ]])

def flatten_data():
	"""
	The purpose of this function is to flatten the data that is inside the .pos, .res, .clu

	This function requires iterating through all of the .pos, .res, and .clu files and creating a nested format of all of the data

	For reference, the .pos files contain x and y positions of the rat in terms of the video, .res is the samples, and .clu is the clusters and tetrodes 

	return: an array of the flattened data
	"""
	data = {}
	for train in glob.glob("data/trains/*"):
	    train_name = path.basename(train)
	    for cluster in glob.glob("data/trains/train/*"):
			tetrode_name = path.basename(cluster)[0]
			cluster_arr = []
			for line in fp:
		    data = make_array(cluster)
			ndata = {"cluster": cluster_name, "data": data}
			data[train_name] = ndata