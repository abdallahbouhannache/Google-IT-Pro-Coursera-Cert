#!/usr/bin/env python3

# CRON JOBS ARE USED TO SCHEDULE SCRIPTS ON UNIX BASE SYSTEMS
# syslog

import sys
import re

usernames={}

logfile=sys.argv[1]

with open(logfile) as fp:
	for line in fp:
		if "CRON" not in line:
			continue
		print(fp.strip())
		pattern=r'USER \((\w+)\)$'
		result=re.search(pattern,line)
		user=result[1]
		usernames[user]=usernames.get(user,0)+1

print(usernames)

