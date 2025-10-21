#! /usr/bin/python3

import sys
import subprocess
import pathlib
from glob import glob


script_run_path = pathlib.Path(__file__).parent / "utility_scripts"  # use .parent attr to remove script_runner.py from path
filename_set = set(glob('*.py', root_dir=script_run_path)) #retrieve all files that start with 'sc_' and end in '.py'

if len(sys.argv) < 2: # may remove in final version
    print('Usage: python3 script_runner.py <filename.py>')
    exit()

if sys.argv[1] in filename_set:
    target_script = script_run_path.joinpath(sys.argv[1])
    result = subprocess.run(['python3', target_script], capture_output=True, check=True)
    print(result.stdout.decode())
    print(result.stderr)
