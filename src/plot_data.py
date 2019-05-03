import load_data
import numpy as np
import matplotlib.pyplot as plt

test = load_data.load_spikes("/Users/Embo/comp-neurosci-crcns-hc18/data/train.242/Train-242.clu.10")

clu_list = []

for i in test.index.values[:5000]:
    if i not in clu_list:
        clu_list.append(int(i))

for i in clu_list:
    plot = test
    plot = plot.loc[i]
    plot = plot.values
    p = []
    for i in plot:
        for j in i:
            p.append(j)
    fig, axes = plt.subplots(nrows = 1, ncols = 1, figsize = (10,6), sharex = True)
    plt.hist(p, bins = 250)
