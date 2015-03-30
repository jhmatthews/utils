#!/local/software/python/2.7.5/bin/python
import numpy as np 
import os, sys

mode = sys.argv[1]

os.system("qstat > _temp_qstat")

f = open("_temp_qstat", "r")

for line in f:
	
	data = line.split()

	if data[0] != "Job" and data[0][0] != "-":
		job_id = data[0]

		if mode == "start":
			os.system("showstart %s" % job_id)

		elif mode == "check":
			os.system("checkjob %s >  _check" % job_id)
			
			g = open("_check", "r")

			for line in g:
				gdata = line.split()
				if len(gdata) > 1:
					if gdata[0] == "AName:":
						name = gdata[1]	
					if gdata[0] == "State:":
						state = gdata[1]
					if gdata[0] == "WallTime:":
                                                wall = gdata[1]
			
			print job_id, state, wall, name

			os.system("rm -f _check")

os.system("rm -f _temp_qstat")
