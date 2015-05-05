#!/usr/bin/env python
import os, sys
import platform
import py_plot_util as util 
import py_read_output as r
import numpy as np
import itertools as it


template = r.read_pf(sys.argv[1])


tot = 0
var = []
values = []
short = []
nvar = 0

grid_file = open(sys.argv[2], "r")

for line in grid_file:
	data = line.split()

	if data[0] != "#" and len(data) > 1:

		nvar+=1

		for i in range(2,len(data)):
			values.append(data[i])
			var.append(data[0])
			short.append(data[1])
			tot += 1

print var
print values

#nvar = len(var)
var = np.array(var)
values= np.array(values)

indices = np.arange(tot)

print indices

count = 0


for i in it.combinations(indices, nvar):

	do = True

	temp = []

	# check there isn't a repitition- must be a pythonic way to do this
	for j in range(len(i)):
		for k in range(len(temp)):
			if temp[k] == str(var[i[j]]):
				do = False
		temp.append(str(var[i[j]]))

	if do:		# there isn't a repetition, so go ahead

		count +=1 
		temp = np.array(temp)
		dummy = template 

		file_string = "run%i" % count

		for j in range(len(i)):
			dummy[str(var[i[j]])] = values[i[j]]
			file_string += "_%s%s" % (short[i[j]],values[i[j]])

		r.write_pf(file_string, dummy)

		print file_string, temp





print count






