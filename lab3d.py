#!/usr/bin/env python3

# Author ID: jshopkins

import os
import subprocess

def free_space():
    p = subprocess.Popen(['df -h | grep \'/$\' | awk \'{print $4}\''], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    asdf = p.communicate()
    return asdf[0].decode('utf-8').strip()