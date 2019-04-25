# tidy data

# sampling rates of acquisition and video -- both found in the .xml files
fs_spikes - 32552.083 # samples/second
fs_video = 39.0625 # frames/second

# to find the spike times and correct positions:

# 1. with the data in the res file mutliplt by (1/fs_spikes) AS A FLOAT

# above is spike times!!!

# 2. multiply by fs_video and then cast as an integer using int()
# 3. resulting int corresponds to a line number in the .pos files which will give you the x and y positions


