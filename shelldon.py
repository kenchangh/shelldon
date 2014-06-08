#!/usr/bin/env python

import os
import subprocess

def call(cmd):
    cmd_list = cmd.split()
    subprocess.call(cmd_list)

