To retrieve data set go to CRCNS website and find the hc-18 data set. From there:

		1. Download the Train-242 tar.gz file 
		2. Move relevant files into the data folder
			a. These files are: .clu#, .res#, and .xml
		3. Change the file names to exclude the date. For example:
			Before: Train-242-20140617.clu.12
			After: Train-242.clu.12
			This is important as the functions made to read data is looking for file names
			in this format.
			We have made a function that does this for you, if that is more convenient.
		4. We will not be using the following files: .fet#, .lfp, .spk#, .pos, and .cat.evt
