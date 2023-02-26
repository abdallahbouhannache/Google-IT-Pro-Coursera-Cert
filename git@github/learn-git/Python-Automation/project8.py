#!/usr/bin/env python3
import os
import zipfile 
import re

# Backup of folder into a zip file

# Copies the whole contents of any folder into a zip file whose filename increaments

# File format should be like this filename_number.zip (number should be increamented)

def backup(folder):
	# Backup the content of folder into a zip file

	folder = os.path.abspath(folder)
	number = 1

	while True:
		zip_name = os.path.basename(folder) + '_' + str(number) + '.zip'
		print("while")

		if os.path.exists(zip_name):
			print(f"{zip_name} -- file already exist quitting ..")
			break
		number = number + 1

		print ("Creating file %s" %(zip_name))

		backupzip = zipfile.ZipFile(zip_name,'w')

		# Walking through the whole directory
		for foldername, subfolders, filenames in os.walk(folder):
			if  len(foldername) and  not re.search(r'\.',foldername):
				print(foldername, subfolders, filenames)
				for filename in filenames:
					backupzip.write(filename)

		backupzip.close()

		print ('Succeeded')
		break

# def main():
# 	backup()

backup("./")