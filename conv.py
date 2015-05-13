#!/usr/bin/env python
#import pylab as p 
import pylab as p
import py_read_output as r 
import numpy as np 
import os, sys
import py_plot_util as util

path = os.getcwd()

out_files = [f for f in os.listdir(path) if f.endswith('.out')]

for i in range(len(out_files)):
	
	c = r.read_convergence(out_files[i])

	sig_file = out_files[i][:-3] + ".sig"

	f = open(sig_file, "r")

	last = "0"
	for line in f:
		data = line.split()
		if len(data) > 11:
			if data[11] == "ionization":
				last = data[8]	
	f.close()

	print "%s\t%s\t%s" % (sig_file[:-3], c,last)




