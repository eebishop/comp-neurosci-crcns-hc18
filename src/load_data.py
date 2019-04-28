# loading data

import glob
from os import path
import numpy as np

x = {}

for t in glob.glob("/Users/Embo/comp-neurosci-crcns-hc18/data/trains/*"):
    train_name = t[-3:]
    for file in glob.glob(t + "/*"):
        train = []
        file_type = path.basename(file)[19:22]
        if file_type in ["clu", "res"]:
            tetrode_num = path.basename(file)[23:]
            file_name = file_type + tetrode_num
            data_arr = []
            with open(file, "rt") as fp:
                for line in fp:
                    line = line.strip()
                    data_arr.append(line)
            spike_data = {"file_name": file_name, "tetrode_num": tetrode_num, "data": data_arr}
            train.append(spike_data)
        elif file_type == "pos":
            positions = []
            with open(file, "rt") as fp:
                for line in fp:
                    line = line.strip().split("\t")
                    positions.append(line)
            pos_data = {"positions": positions}
            train.append(pos_data)
        elif file_type == "cat":
            file_type = "cat.evt"
            phases = []
            with open(file, "rt") as fp:
                for line in fp:
                    line = line.strip()
                    phases.append(line)
            phase_data = {"phases": phases}
            train.append(phase_data)
    x[train_name] = train
        
print(x)




