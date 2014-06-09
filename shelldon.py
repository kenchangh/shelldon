#!/usr/bin/env python

import os
import shlex
import subprocess

home = os.path.expanduser('~')
os.chdir(home)

def call(cmd):
    cmd_lines = split_cmd(cmd)
    for line in cmd_lines:
        call_list = shlex.split(line)
        try:
            subprocess.call(call_list)
        
        except OSError:
            if call_list[0] == 'cd':
                os.chdir(call_list[1])

def split_cmd(cmd):
    cmd_lines = cmd.splitlines()

    for index, line in enumerate(cmd_lines):
        line = line.strip()
        cmd_lines[index] = line

    cmd_lines = filter(lambda x: x != '', cmd_lines)
    return cmd_lines

