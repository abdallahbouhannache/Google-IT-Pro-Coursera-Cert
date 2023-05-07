#!/usr/bin/env python3

import re
import sys


logfile=sys.argv[1]

usernames={}



with open(logfile) as f:
	for line in f:
		if "CRON" not in line:
			continue
		pattern=r"USER \((\w+)\)$"
		res=re.search(pattern,line)
		if res is None:
			continue
		name=res[1]

		usernames[name]=usernames.get(name,0)+1
		print(line.strip())	
		print(res[1])
