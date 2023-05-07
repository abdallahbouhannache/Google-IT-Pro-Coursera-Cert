#!/usr/bin/env python3


import re
import sys

name=sys.argv[1]


def rearrange(name):
    result=re.search(r"^([\w .]*), ([\w .]*)$",name)
    if result is None:
        return name
    return "{} {}".format(result[2],result[1])

if name:
    print(rearrange(name))