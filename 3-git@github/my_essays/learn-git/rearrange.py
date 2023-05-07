#!/usr/bin/env python3

import re

def rearrange_name(name):
	# here we search for the pattern 
	# then we return the input string if there is no result found
	result=re.search(r"^([\w.]*), ([\w.]*)$", name)
	if result is None:
		return name
	return "{} {}".format(result[2],result[1])