#! /usr/bin/python3

import sys
import subprocess
import pathlib


def get_scriptPath():
    curr_path = pathlib.Path(__file__).parent #use .parent attr to remove script_runner.py from path
    filename = sys.argv[1]

    if ".py" not in filename:
        filename = filename + ".py"

    return curr_path.joinpath(filename)



if len(sys.argv) < 2: #may remove in final version
    print('Usage: python3 script_runner.py <filename.py>')
    exit()

script_path = get_scriptPath()

result = subprocess.run(['python3', script_path], capture_output=True, check=True)
print(result.stdout.decode().strip())
