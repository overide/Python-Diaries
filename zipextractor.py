#Author: Atul Kumar
#Date created: 11/06/16
#This script will simply extract the zip files
#Note: Filenames are case sensitive! take care!

import zipfile,os,pprint,sys

#Function to list the files and folders in zip file
def ziplist(ziploc):
	ziph=zipfile.ZipFile(filelocation)
	return ziph.namelist()

#Take choice form user
def takeChoice():
	choice=input('For extracting specific file press 1\nFor extracting all press 2\n>>')
	return int(choice)

#Extra specific file
def extractSpecific(filename,filelocation,extractLocation):
	ziphandle=zipfile.ZipFile(filelocation)
	os.mkdir(extractLocation+'\\extract')
	flocation=extractLocation+'\\extract'
	ziphandle.extract(filename,flocation)
	ziphandle.close()

#Extract All
def extractAll(filelocation,extractLocation):
	ziphandle=zipfile.ZipFile(filelocation)
	os.mkdir(extractLocation+'\\extract')
	ziphandle.extractall(extractLocation+'\\extract')
	ziphandle.close()

#Taking zip file location
filelocation=input("Please, enter the zip file location: ")
print('*' * 50)
zipfname=os.path.basename(filelocation)
print("List of the files and folders insize the zip file "+zipfname)
#printing files and directories inside the zip file
pprint.pprint(ziplist(filelocation))
print('*' * 50)

while True:
	myChoice=takeChoice()
	#Extraction of specific file
	if myChoice==1:
		filename=input('please enter the name of the file to be extraxted: ')
		extractLocation=input('Please enter the location for extraction: ')
		extractSpecific(filename,filelocation,extractLocation)
		print('File '+filename+' is successfully extracted at location '+extractLocation+'\extract')
		sys.exit(0)
	#Extract full zip file
	elif myChoice==2:
		extractLocation=input("Please enter the location for extraction: ")
		extractAll(filelocation,extractLocation)
		print('Zip File '+zipfname+' is successfully extracted at location '+extractLocation+'\extract')
		sys.exit(1)
	else:
		print("Please enter valid options!")