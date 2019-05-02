# tidy data

# sampling rates of acquisition and video -- both found in the .xml files
fs_spikes - 32552.083 # samples/second
fs_video = 39.0625 # frames/second

# to find the spike times and correct positions:

# 1. with the data in the res file mutliply by (1/fs_spikes) AS A FLOAT

def make_spikes_all():
	"""
	This function iterates through all of the trains to changes all of the raw res data into spike times
	Calls the component function

	Parameter: None

	Return: None, changes data in the dictionary
	"""
	for t in glob.glob("/Users/Embo/comp-neurosci-crcns-hc18/data/trains/*"):
            for file in glob.glob(t + "/*"):
            	if "res" in file:
            		make_spikes_component(file)



def make_spikes_component(fname):
	"""
	This function changes raw res data into spike times. Does this for idnividual res files
	"""
	with open(fname, "rt") as fp:
        for line in fp:
			line = float(line)
		    line  = line * 1/(fs_spikes)


# above is spike times!!!

# 2. multiply by fs_video and then cast as an integer using int()
# 3. resulting int corresponds to a line number in the .pos files which will give you the x and y positions


