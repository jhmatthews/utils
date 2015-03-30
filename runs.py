#!/usr/bin/python
'''
Script to create daddy script and individual script for iridis runs

'''
import os, sys

ls_filename = sys.argv[1]

ncores = sys.argv[2]

walltime = sys.argv[3]

vers = sys.argv[4]
vers_sep = False
if vers == "-v":
	print "running separate versions on separate files- two column ls file"
	vers_sep = True

dir = os.getcwd()

vlist = []
ls_file = open(ls_filename, "r")
pf_files = []
for line in ls_file:
	if vers_sep:
		data = line.split()[1]
		v = line.split()[0]
                vlist.append(v)	
	else:
		data = line.split()[0]
	pf_files.append(data)
	

restart = False
if len(sys.argv) > 5:
	if sys.argv[5] == "-r":
		restart = True

submit_name = "submit_%s" % ls_filename
daddy = open (submit_name, "w") 

for i in range(len(pf_files)):
	
	scriptname = "script%i_%s" % ( i, pf_files[i][:-3])
	script = open (scriptname, "w")

	script.write("module load openmpi/1.6.4/intel_of2\n\n")

	command = "cd %s\n" % dir

	script.write(command)
	
	if vers_sep:
		version = vlist[i]
	else:
		version = vers
	
	if restart:
		command = "mpirun -n %s /home/jm8g08/Python/bin/py%s -r %s > %s.out &\n" % (ncores, version, pf_files[i][:-3], pf_files[i][:-3])
	else:
		command = "mpirun -n %s /home/jm8g08/Python/bin/py%s %s > %s.out &\n" % (ncores, version, pf_files[i][:-3], pf_files[i][:-3])

	print command

	script.write(command)

	script.write("wait\n")
	nodes = int(ncores) / 8
	ppn = int( ncores) / nodes 


	daddy.write("qsub -l nodes=%i:ppn=%i -l walltime=%s %s\n" % (nodes, ppn, walltime, scriptname))
	print "qsub -l nodes=%i:ppn=%i -l walltime = %s\n" % (nodes, ppn, walltime)

	script.close()



daddy.close()


os.system ("chmod +x %s" % submit_name)
print "all done"
