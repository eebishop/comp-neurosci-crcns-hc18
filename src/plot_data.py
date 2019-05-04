from src import load_data
import numpy as np
import matplotlib.pyplot as plt
import math


def prep_data(clufile):
	"""
	This function prepares the data to be plotted for both the combined and all functions
	Its major purpose is complile a list of all of the clusters found in the given clu file

	Parameter: a clu file

	Return: a list of unique clusters
	"""
	t = load_data.load_spikes(clufile)
	clu_list = []
	for i in t.index.values[:5000]:
	    if i not in clu_list:
	        clu_list.append(int(i))
	return clu_list

def plot_tetrode_combined(clufile):
	"""
	This function creates a figure with multiple histograms within it, each graph representing a cluster in the given 
	tetrode.

	Parameter: a clu file

	Return: Nothing, plots a figure
	"""
	clu_list = prep_data(clufile)

	num = len(clu_list) # prepping the fig with correct rows/cols
	sq = np.sqrt(num)
	row = math.floor(sq) 
	col = math.ceil(sq) + 1
	if(row*col >= num + row):
	    col -= 1
	fig, axes = plt.subplots(nrows = row, ncols = col, figsize = (10,6), sharex = True)
	tetrode_num = clufile.split(".")[-1]
	fig.suptitle("Tetrode" + str(tetrode_num))
	row_counter = 0
	col_counter = 0

	for i in clu_list: # plotting each cluster in same figure
	    plot = load_data.load_spikes(clufile)
	    plot = plot.loc[i]
	    plot = plot.values
	    p = []
	    for k in plot:
	        for j in k:
	            p.append(j)
	    axes[row_counter][col_counter].hist(p, bins = 250)
	    axes[row_counter][col_counter].set_title("Cluster " + str(i))
	    if col_counter >= col - 1:
	        col_counter = 0
	        row_counter += 1
	    else:
	        col_counter += 1


