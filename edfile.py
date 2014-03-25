'''
edfile.py replaces 
'''

import os, sys
import util


mode = sys.argv[1]
ls_filename = sys.argv[2]
s1 = sys.argv[3]
s2 = sys.argv[4]

fnames = np.loadtxt(ls_filename, dtype="string")



if mode =="-r":
	# we are in replace mode

	util.edit_fname(fnames, s1, s2, mode = "replace")




elif mode == "-a":

	util.edit_fname(fnames, s1, s2, mode = "append")



ode = "replace")




elif mode == "-a":

	util.edit_fname(fnames, s1, s2, mode = "append")



ode = "replace")




elif mode == "-a":

	util.edit_fname(fnames, s1, s2, mode = "append")



ode = "replace")




elif mode == "-a":

	util.edit_fname(fnames, s1, s2, mode = "append")



ode = "replace")




elif mode == "-a":

	util.edit_fname(fnames, s1, s2, mode = "append")



