#!/usr/bin/env python3



import os

def filereader(filename):
	if os.path.exists(filename):
		with open(filename,'r') as f:
			for line in f:
				print(line)
	else:
		print(f'{filename} does not exist')

filepointer=open('file.txt','w')
filepointer.write('this is just few words to write ')
filepointer.close()

filepointer=open('file.txt','r+')
filepointer.write('apending other content to the file')
#print(f'{filepointer}')
filepointer.close()

#or this way
with open('nextf.txt','w') as fp:
	fp.write('this file content was generated by the script')

deletedfile=input('enter file name you want to delete file.txt or nextf.txt')

if len(deletedfile) and os.path.exists(deletedfile):
	os.remove(deletedfile)	


filereader('file.txt')
filereader('nextf.txt')

#directories
print(os.getcwd())
newdir=input('enter new directory name:')
if len(newdir):
	print(f'creating {newdir}')
	os.mkdir(newdir)
	print(f'cd dir to {newdir}')
	os.chdir(newdir)
	print(os.getcwd())
	print(f'creating {newdir+"next"}')
	os.mkdir(newdir+"next")
	print(f'deleting the : {newdir+"next"}')
	os.rmdir(newdir+"next")

print("list of files in the current directory")
print(os.listdir)

dir='./'
for name in os.listdir(dir):
	fullpath=os.path.join(dir,name)
	if isdir(fullpath):
		print(f'{fullpath} is a directory')
	else:
		print(f'{fullpath} is a file')
		










