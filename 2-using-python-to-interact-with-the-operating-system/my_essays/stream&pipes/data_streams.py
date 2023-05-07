#!/usr/bin/env python3

import os
import sys

print(os.env.get('PATH',"path unavailable in env"))
#export FRUIT=var_content

print(sys.argv)

filename=sys.argv[1]

if not os.path.exists(filename):
	with open(filename,'w') as fp:
		f.write('new file created \n')
else:
	print(f'error file:{filename} already exists')
	sys.exit(1)


