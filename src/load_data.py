# loading data

import glob
from os import path
import numpy as np
import pandas as pd

# Note: Must change file name of all files to exclude date for make_dict() to work properly
# Having an issue with pandas
# Add documentation for each function

def make_dict():
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
    positions = []
    with open(fname, "rt") as fp:
        for line in fp:
            line = line.strip().split("\t")
            line = map(int, line)
            positions.append(line)
    return positions


def load_phases(fname):
    phases = []
    with open(fname, "rt") as fp:
        for line in fp:
            line = line.strip().split()
            ret = []
            ret.append(line[0])
            ret.append(line[1])
            ret.append(line[3][22:])
            phases.append(ret)
    return phases


def load_clu_res(fname):
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

