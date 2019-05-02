# loading data

import glob
from os import path
import os
import numpy as np
# import pandas as pd

# Note: Must change file name of all files to exclude date for make_dict() to work properly

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
    for file in glob.glob("/Users/Embo/comp-neurosci-crcns-hc18/data/trains/" + train_name + "/*"):
        print("hi")
        change_name(file)

def make_dict():
    """
    This function creates anested dictionary of all of the files in the dataset. Top layer of dictionary is of the indivdual
    trains. Second level dictionary is the all of the files within each train (e.g. clu, res, pos, etc.). This function 
    calls other functions in this script in order to make the dictionary

    Parameter: None

    Return: The nested dictionary
    """
    d = {} # First level dictionary
    for t in glob.glob("/Users/Embo/comp-neurosci-crcns-hc18/data/trains/*"):
        train_name = t[-3:]
        train = {} # Second level dictionary
        train["positions"] = load_pos(t + "/Train-" + train_name + ".pos")
        train["phases"] = load_phases(t + "/Train-" + train_name + ".cat.evt")
        for file in glob.glob(t + "/*"): # More complicated code for the individual clu and res files
            file_type = path.basename(file)[10:13]
            if file_type in ["res", "clu"]:
                tetrode_num = path.basename(file)[14:]
                train[file_type+tetrode_num] = load_clu_res(t + "/Train-" + train_name + "." + file_type + "." + tetrode_num)
        d[train_name] = train
    return d

def load_pos(fname):
    """
    This function opens a specific pos file and reads the data into an array format. It will
    be a nested list where each item in the top layer list is an array of two positions. For example:
    [[3, 4], [1,2]]

    Parameter: the path of the file to open and read

    Return: Nested list with position data
    """
    positions = []
    with open(fname, "rt") as fp:
        for line in fp:
            line = line.strip().split("\t")
            line = map(int, line)
            positions.append(line)
    return positions


def load_phases(fname):
    """
    This function opens a specific cat.evt file and reads the data into an array format. It will
    be a nested list where each item in the top layer list is an array of three items: the time value,
    whether it denotes a beginning or end, and the phase it represents. For example:
    [[0, 'beginnning', 'SleepBaseline']]

    Parameter: the path of the file to open and read

    Return: Nested list with phase data
    """
    phases = []
    with open(fname, "rt") as fp:
        for line in fp:
            line = line.strip().split()
            ret = []
            ret.append(line[0])
            ret.append(line[1])
            ret.append(line[3][22,])
            phases.append(ret)
    return phases


def load_clu_res(fname):
    """
    This function opens a specific clu or res file and reads the data into an array format. The first value 
    in the array represents SOMETHING IMPORTANT 

    Parameter: the path of the file to open and read

    Return: List with data
    """
    data_arr = []
    with open(fname, "rt") as fp:
        for line in fp:
            data_arr.append(int(line)) 
    return data_arr


# Testing

testing_mode = False

if testing_mode:

    # Test load_pos

    pos_test = load_pos("/Users/Embo/comp-neurosci-crcns-hc18/data/trains/train.242/Train-242.pos")
    print(pos_test[:10])

    # Test load_clu_res

    clu_test = load_clu_res("/Users/Embo/comp-neurosci-crcns-hc18/data/trains/train.242/Train-242.clu.2") 
    print(clu_test[:10])

    res_test = load_clu_res("/Users/Embo/comp-neurosci-crcns-hc18/data/trains/train.242/Train-242.res.2") 
    print(res_test[:10])

    # Test load_phases

    phase_test = load_phases("/Users/Embo/comp-neurosci-crcns-hc18/data/trains/train.242/Train-242.cat.evt")
    print(phase_test[:10])

    #  Test make_dict

    dict_test = make_dict()
    print(dict_test.keys())
    print(dict_test["242"].keys())
    print(dict_test["242"]["phases"])
    df = pd.DataFrame(make_dict())
    print(df)



change_name_train("train.292")