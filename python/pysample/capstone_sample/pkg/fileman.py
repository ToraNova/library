#!/usr/bin/python3
import os, sys

target_path = "data/base"

def checkFiles(filename,pathdir):
	return os.path.isfile(os.path.join(pathdir,filename))

def checkExist(pathdir):
	#check if pathdir exist, create it if not
	if( os.path.isdir(pathdir) and os.path.exists(pathdir)):
		#do not create dir, just files
		pass #do nothing
	else:
		#create directory and files
		os.makedirs(pathdir, 0o777 ) #create the directory

def createFiles(filenames,pathdir):
	#write "test name" onto a list of filenames
	for name in filenames:
		with open(os.path.join(pathdir,name), 'w') as tfile:  # Use file to refer to the file object
	    		#tfile.write('test '+f) #sample operation
			pass

def listDir(pathdir):
	x = [x[2] for x in os.walk(pathdir)][0]
	return x

def clearDir(pathdir):
	x = [x[2] for x in os.walk(pathdir)][0]
	for f in x:
		os.remove(os.path.join(pathdir,f))	

if __name__ == "__main__":

	filelist = ["a","b","c","d"]

	checkExist(target_path)			#check and create path
	#createFiles(filelist,target_path) 	#create a list of files

	x = listDir(target_path)
	print(x)
	if("a" in x):
		print("yes")

	#clearDir(target_path)


	

