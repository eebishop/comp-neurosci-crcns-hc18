#!/usr/bin/env python
# coding: utf-8

# In[5]:


from src import load_data
import numpy as np
import matplotlib.pyplot as plt
import glob
from os import path
import os
import math


clufile = "/Users/Embo/comp-neurosci-crcns-hc18/data/train.242/Train-242.clu.10"


def plot_tetrode(clufile):
    spikes = load_data.load_spikes(clufile)
    clu_list = []
    for i in spikes.index.values[:5000]:
        if i not in clu_list:
            clu_list.append(int(i))
    num = len(clu_list)
    sq = np.sqrt(num)
    row = math.floor(sq) 
    col = math.ceil(sq) + 1
    if(row*col >= num + row):
        col -= 1
    fig, axes = plt.subplots(nrows = row, ncols = col, figsize = (10,6), sharex = True)
    tetrode_num = clufile.split(".")[-1]
    fig.suptitle("Tetrode " + str(tetrode_num))
    row_counter = 0
    col_counter = 0

    for i in clu_list:
        plot = spikes
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
            

plot_data(clufile)


# In[2]:


# clu_list = []

# for i in spikes.index.values[:5000]:
#     if i not in clu_list:
#         clu_list.append(int(i))


# In[3]:


# num = len(clu_list)
# sq = np.sqrt(num)
# row = math.floor(sq) 
# col = math.ceil(sq) + 1
# if(row*col >= num + row):
#     col -= 1


# In[4]:


# fig, axes = plt.subplots(nrows = row, ncols = col, figsize = (10,6), sharex = True)
# tetrode_num = clufile.split(".")[-1]
# fig.suptitle("Tetrode " + str(tetrode_num))
# row_counter = 0
# col_counter = 0

# for i in clu_list:
#     plot = spikes
#     plot = plot.loc[i]
#     plot = plot.values
#     p = []
#     for k in plot:
#         for j in k:
#             p.append(j)
#     axes[row_counter][col_counter].hist(p, bins = 250)
#     axes[row_counter][col_counter].set_title("Cluster " + str(i))
#     if col_counter >= col - 1:
#         col_counter = 0
#         row_counter += 1
#     else:
#         col_counter += 1

