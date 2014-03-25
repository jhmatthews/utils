'''
Script to create daddy script and individual script for iridis runs

'''
import os, sys

ls_filename = sys.argv[1]

ncores = sys.argv[2]

walltime = sys.argv[3]

vers = sys.argv[4]

dir = os.getcwd()

ls_file = open(ls_filename, "r")
pf_files = []
for line in ls_file:
	data = line.split()[0]
	pf_files.append(data)


daddy = open ("daddy_script", "w") 

for i in range(len(pf_files)):
	
	scriptname = "script%i_%s" % ( i, pf_files[i][:-3])
	script = open (scriptname, "w")

	script.write("module load mpirun/1.6.4/intel_of2\n\n")

	command = "cd %s\n" % dir

	script.write(command)

	command = "mpirun -n %s /home/jm8g08/Python/bin/py%s %s > %s.out &\n" % (ncores, vers, pf_files[i][:-3], pf_files[i][:-3])

	print command

	script.write(command)

	script.write("wait\n")
	nodes = int(ncores) / 8
	ppn = int( ncores) / nodes 


	daddy.write("qsub -l nodes=%i:ppn=%i -l walltime=%s %s\n" % (nodes, ppn, walltime, scriptname))
	print "qsub -l nodes=%i:ppn=%i -l walltime = %s\n" % (nodes, ppn, walltime)

	script.close()



daddy.close()


os.system ("chmod +x daddy_script")
print "all done"
