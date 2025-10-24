#! /usr/bin/python3

import sys
import subprocess
import pathlib

curr_path = pathlib.Path(__file__).parent #use .parent attr to remove script_runner.py from path


if len(sys.argv) < 2: #may remove in final version
    print('Usage: python3 script_runner.py <filename.py>')
    exit()


filename = sys.argv[1]

if '.py' not in filename:
    filename = filename + '.py'

target_script = curr_path.joinpath(filename)

result = subprocess.run(['python3', target_script], capture_output=True, check=True)
print(result.stdout.decode())
print(result.stderr)
