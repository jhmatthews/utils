#!/local/software/python/2.7.5/bin/python
'''
modes
cf 			copy and replace in name 
f 			just replace in name 
cr 			copy and replace in file 
r 			just replace in file 
'''

import os, sys
import numpy as np 


mode = sys.argv[1]

old_string = sys.argv[2]
new_string = sys.argv[3]

files = sys.argv[4]


if files[0:3] == "all":
	os.system("ls *%s > _temp" % files[3:])

old_fnames = np.loadtxt("_temp", dtype="string")


os.system("sed -i 's/%s/%s/g' _temp" % (old_string, new_string))
new_fnames = np.loadtxt("_temp", dtype="string")

nfiles = len(old_fnames)

print "processing %i files" % nfiles

for i in range(nfiles):

	if mode == "c":
		command = "cp %s %s" % (old_fnames[i], new_fnames[i])

	elif mode == "r":
		command = "mv %s %s" % (old_fnames[i], new_fnames[i])

	os.system(command)


os.system("rm -f _temp")
