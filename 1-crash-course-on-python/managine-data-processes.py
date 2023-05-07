#!/usr/bin/env python3
import os

name=input("please enter your name:")
print("hello ,"+name)

shell=os.environ.get('SHELL','not defined')
path=os.environ.get('PATH','unavailable')

print(f'env variables :\n\n path={path} \n\n shell={shell}')