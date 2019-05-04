# loading data

import glob
from os import path
import os
import numpy as np
import pandas as pd

def change_name(file):
    """ 
    This function ensures that all files are in the correct format. If they are not, the function alters 
    the file name so that it is. 

    Parameter: The file name of the file to be checked/changed

    Returns: Nothing, changes the file names
    """
    date = file[69:72]
    if date == "201":
        path_name = file[0:59]
        file_name_o  = path.basename(file)
        file_name_m = file_name_o[0:9] + file_name_o[18:]
        os.rename(file, path_name + file_name_m)

# Changing all of the file names (use this once after you have downloaded all the files


def change_name_train(train_name):
    """ 
    This function ensures that all files are in the correct format in a specified train. 
    If they are not, the function alters the file name so that it is. 

    Parameter: The train name of the train with files to be checked/changed

    Returns: Nothing, changes the file names
    """
    for file in glob.glob("/Users/Embo/comp-neurosci-crcns-hc18/data/trains/" + train_name + "/*"):
        change_name(file)


def make_dict():
    """
    This function creates a nested dictionary of all of the files in the dataset. Top layer of dictionary is of the indivdual
    trains. Second level dictionary is the all of the files within each train (e.g. clu, res, pos, etc.). This function 
    calls other functions in this script in order to make the dictionary

    Parameter: None

    Return: The nested dictionary
    """
    t = "/Users/Embo/comp-neurosci-crcns-hc18/data/train.242"
    train = {}
    for clufile in glob.glob(t + "/*clu*"):
        tetrode_num = int(clufile.split(".")[-1])
        train[tetrode_num] = load_spikes(clufile)
    return train


def load_spikes(clufile):
    """
    This function loads the spike times from a given clu file. It references the res file with same tetrode num 
    to get both clu data and spike time data. It creates a data frame using these two set of data

    Parameter: a clu file

    Return: a data frame with clu and res data from a specific tetrode
    """
    sampling_rate = 32552.083 
    resfile = clufile.replace("clu", "res")
    cludata = np.loadtxt(clufile)[1:]
    resdata = (np.loadtxt(resfile) / sampling_rate)
    # data_dict = {"cludata": cludata, "resdata": resdata}
    df = pd.DataFrame({"cluster": cludata, "time (ms)": resdata})
    df = df_idx = df.set_index(["cluster"])
    return df
