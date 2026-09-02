#!/usr/bin/python3

from pathlib import Path
import os
import subprocess

folder_path = os.path.dirname(os.path.abspath(__file__))
alias_path = os.path.join(folder_path, ".bash_aliases")

user_path = os.path.expanduser('~')
cmd = f'cp {alias_path} {user_path}'
print("Bash Aliases Copied")
subprocess.run(cmd.split(' '))