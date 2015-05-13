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

	print out_files[i], c


sig_files = [f for f in os.listdir(path) if f.endswith('.sig')]

for i in range(len(sig_files)):

	f = open(sig_files[i], "r")

	last = "0"
	for line in f:
		data = line.split()
		if len(data) > 11:
			if data[11] == "ionization":
				last = data[8]	
	f.close()

	print sig_files[i], last
