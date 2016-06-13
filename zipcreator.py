#Author:Atul Kumar
#Date of creation: 11/06/2016
#This script create a zip file for specified folder

import os,sys,zipfile

targetFolderLocation = input('Enter the location of folder to be compressed: ')
zippedLocation = input('Enter the location where zip file is saved: ')
zipfilename = input('Enter the name of zip file to be created: ')
zfhandle = zipfile.ZipFile(zipfilename+'.zip','w')
filelist=os.listdir(targetFolderLocation)

#create zip file handle
for filename in filelist:
	zfhandle.write(targetFolderLocation+'\\'+filename,compress_type=zipfile.ZIP_DEFLATED)

while True:
	passChoice=input("do you want to lock zip file with password? Y or N :")
	#password protect zip file
	if passChoice=='Y':
		password=input('Enter the password: ')
		zfhandle.setpassword(password.encode('ascii'))#unicode point is being converted into bytes
		print('Zip file '+zipfilename+'.zip'+' is successfully created at '+zippedLocation)
		sys.exit(0)
	#No password protection
	elif passChoice=='N':
		print('Zip file '+zipfilename+'.zip'+' is successfully created at '+zippedLocation)
		sys.exit(1)
	else:
		print('Please make valid choice!')



