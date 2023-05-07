#!/usr/bin/env python3



def char_count(filename):

	try:
		fp=open(filename)
	except OSError:
		return None
	chars={}
	for line in fp:
		for c in line:
			chars[c]=chars.get(c,0)+1
	fp.close()
	return chars