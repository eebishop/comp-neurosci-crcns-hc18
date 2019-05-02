To retrieve data set go to CRCNS website and find the hc-18 data set. From there:

		1. Download each .tar.gz from the hc-18 data from the CRCNS website
		2. Move relevant files into the data folder
			a. These files are: .clu#, .pos#, .res#, .cat.evt and .xml
		3. Organize the data into a folder for each session(i.e. train)
		4. Change the file names to exclude the date. For example:
			Before: Train-242-20140617.pos
			After: Train-242.pos
			This is important as the functions made to read data is looking for file names
			in this format.
			We have written function that will do this for you, please 
			use it.
		5. We will not be using the following files: .fet#, .lfp, .spk#
