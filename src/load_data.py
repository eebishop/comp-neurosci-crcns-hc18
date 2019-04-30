# loading data

import glob
from os import path
import numpy as np
import pandas as pd

def make_dict():
"""
This function creates a nested dict with all of the trains and their asosciated files (including res, clu, pos, and cat.evt)
First level is trains and second level is all of the files (in the form of arrays)
The function calls other functions

Parameter: There are no parameters

Return: Returns the nested dictionary
"""
    d = {} # First level dictionary
    for t in glob.glob("/Users/Embo/comp-neurosci-crcns-hc18/data/trains/*"):
        train_name = t[-3:]
        train = {} # Second level dictionary
        train["positions"] = load_pos(t + "Train-" + train_name + ".pos")
        train["phases"] = load_phases(t + "Train-" + train_name + ".cat.evt")
        for file in glob.glob(t + "/*"): # More complicated code for the individual clu and res files
            file_type = path.basename(file)[19:22]
            if file_type in ["res", "clu"]:
                tetrode_num = path.basename(file)[23:]
                train[file_type+tetrode_num] = load_clu_res(t + "Train-" + train_name + "." file_type + "." + tetrode_num)
        d[train_name] = train
    return d

def load_pos(fname):
"""
This function iterates through the pos file of a specific train and return a nested list with positions for each line in the file

Parameter: Accepts a file name that is the pos file for a specific train

Return: A nested list
"""
    positions = []
    with open(fname, "rt") as fp:
        for line in fp:
            line = int(line.strip().split("\t"))
            positions.append(line)
    return positions


def load_phases(fname):
"""
This function iterates through the cat.evt file of a specific train and returns a nested list with positions for each line in the file

Parameter: Accepts a file name that is the cat.evt file for a specific train

Return: A nested list
"""
    phases = []
    with open(fname, "rt") as fp:
        for line in fp:
            line = float(line.strip().split()[0])
            phases.append(line)
    return phases


def load_clu_res(fname):
"""
This function iterates through a clu or res file for a specific train and returns a nested list with the data for each line of the file

Parameter: Accepts a file name that is ta clu or res file for a specific train

Return: A list
"""
   data_arr = []
        with open(fname, "rt") as fp:
            for line in fp:
                line = int(line.strip())
                data_arr.append(line) 
    return data_arr

# Testing




