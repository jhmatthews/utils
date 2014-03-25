'''
setup file 
'''

dependencies = ["util.py", \
				"edfile.py", \
                "runs.py"]

import sys, os

py_ex = "#!"+sys.executable

cdir = os.getcwd()

path_string = '''
export PATH=$PATH:%s 
''' % cdir


home = os.environ["HOME"]



def script_prepender():

	for filename in dependencies:
	    with open(filename,'r+') as f:
	        content = f.read()
	        f.seek(0,0)
	        f.write(py_ex + '\n' + content)

		os.system("chmod +x %s" % filename)

	return 0

def path_appender():

    with open(home+"/.bash_profile",'a') as f:
        f.write(path_string)

	os.system("source " + home + "/.bash_profile")

	return 0


def script_clean():

	for filename in dependencies:
		f = open(filename,'r+')

		temp = []
		for line in f:
			temp.append(line)

		f.seek(0,0)

		for line in temp:
			if "#!" not in line:
				print line
				f.write(line)

	return 0

def path_clean():


	f = open(home + "/.bash_profile",'r+')
	f.seek(0,0)

	temp = []
	for line in f:
		temp.append(line)
	f.seek(0,0)

	for line in temp:
	    if cdir not in path_string:
	        	f.write(line)

	return 0






if len(sys.argv) < 2:
	script_prepender()
	path_appender()

else:
	if sys.argv[1] == "install":
		script_prepender()
		path_appender()

	elif sys.argv[1] == "clean":
		"print Can't clean, won't clean"
		#script_clean()
		#path_clean()