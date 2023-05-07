#!/usr/bin/env python3

import os
import subprocess

print("first")

print("second")

result=subprocess.run(["host","8.8.8.8"],capture_output=True)
print(result.stdout)
print(result.returncode)

rs=subprocess.run(["rm","not_exist"],capture_output=True)
print(rs.stdout)
print(rs.stderr)

print("third")

my_env=os.environ.copy()
my_env["PATH"]=os.environ.pathsep.join(["/opt/wpapp/",my_env["PATH"]])

rs2=subprocess.run(["wpapp"],env=my_env)
print(rs2)