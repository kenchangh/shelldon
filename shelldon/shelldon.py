#!/usr/bin/env python

import os
import sys
import shlex
import subprocess

class CommandError(Exception):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        Exception.__init__(self, message)

def call(cmd):
    cmd_lines = split_cmd(cmd)
    for line in cmd_lines:
        call_list = shlex.split(line)
        try:
            subprocess.call(call_list)
        
        except OSError:
            if call_list[0] == 'cd':
                try: 
                    os.chdir(call_list[1])
                except:
                    raise CommandError(
                    '{cmd} is not a valid command!'.format(
                    cmd = cmd))

def split_cmd(cmd):
    cmd_lines = cmd.splitlines()
    cmd_lines = map(lambda x: x.strip(), cmd_lines)
    cmd_lines = filter(lambda x: x != '', cmd_lines)
    return cmd_lines

def terminal():
    home = os.path.expanduser('~')
    os.chdir(home)

    print ("\nShelldon's interactive terminal.\n" + 
           "Enter 'quit' to exit and 'help' for documentation.")

    while True:
        cwd = os.getcwd()
        cwd = cwd.replace(home, '~')
        cmd = raw_input('\n' + cwd + '$ ')

        if cmd == 'quit':
            break

        elif cmd == 'help':
            help_dir = os.path.join(os.path.dirname(__file__), 'help', 'help.txt')
            with open(help_dir, 'r') as f:
                help_page = f.read()
            print help_page

        else:
            try:
                call(cmd)
            except EOFError:
                break
            if not cmd:
                break

