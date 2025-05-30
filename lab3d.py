#!/usr/bin/env python3
'''Lab 3 Inv 3: get free disk space'''
# Author ID: nkaur526

import subprocess

def free_space():
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", 
                            shell=True, 
                            capture_output=True, 
                            text=True)
    return result.stdout.strip()

if __name__ == '__main__':
    print(free_space())
