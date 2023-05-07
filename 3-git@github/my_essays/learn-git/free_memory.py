#!/usr/bin/env python3

import sys
import psutil

def check_free_space():
        try:
                disc=psutil.disk_usage("/")
                if disc.free/1073741824 >= 10737418240:
                        sys.exit(0)
                else:
                        sys.exit(1)
        except Exception as e:
                raise e

def main():
        """ you need to check disc space """
        if check_free_space():
                print("Everything is Going Good after checking in!")
        else:
                print("There is not enough space!")
main()