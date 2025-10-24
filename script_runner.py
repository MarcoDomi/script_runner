#! /usr/bin/python3

import sys
import subprocess
import pathlib
from glob import glob



if len(sys.argv) < 2: #may remove in final version
    print('Usage: python3 script_runner.py <filename.py>')
    exit()

curr_path = pathlib.Path(__file__).parent #use .parent attr to remove script_runner.py from path
filename = sys.argv[1]
filename_set = glob(f'{filename}.py', root_dir=curr_path) #retrieve all files that end in '.py'
target_script = curr_path.joinpath(sys.argv[1])
result = subprocess.run(['python3', target_script], capture_output=True, check=True)
print(result.stdout.decode())
print(result.stderr)
