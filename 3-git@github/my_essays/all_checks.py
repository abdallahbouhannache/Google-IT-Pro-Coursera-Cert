#!/usr/bin/env python3

import os
import shutil
import socket
import sys


def check_reboot():
    """return true if the computer has a pending reboot"""
    return os.path.exists("/run/reboot-required")


def check_disc_full(disk, min_gig, min_percent):
    """Return True if there is no space left on the disk ,False otherwise"""
    du = shutil.disk_usage(disk)
    free_percentage = 100 * du.free / du.total
    gigabyte_free = du.free / 2**30
    if gigabyte_free < min_gig or free_percentage < min_percent:
        return True
    return False


# def check_root_full():
#     """Return True if the root partition is Full ,False otherwise"""
#     return check_disc_full("/", min_gig=2, min_percent=10)


# def check_no_network():
#     """Return True if the internet is unavailable."""
#     try:
#         socket.gethostbyname("www.google.com")
#         return True
#     except:
#         return False


def main():
    checks = [
        (check_reboot, "Pending Reboot"),
        # (check_root_full, "Root Partition is FUll"),
        # (check_no_network, "No internet Connection"),
    ]
    Everything_is_Ok = True
    for check, msg in checks:
        check()
        print(msg)
        Everything_is_Ok = False

    if not Everything_is_Ok:
        sys.exist(1)
