#! /usr/bin/python3

import sys
import subprocess
import pathlib

class tool_manager:
    def __init__(self):
        self.file_dict = {}

    def update_dict(self):
        pass

    def list_files(self):
        for k in self.file_dict:
            print(f'{self.file_dict[k]} - {k}')

def get_filename():
    filename = sys.argv[1]

    if ".py" not in filename:
        filename = filename + ".py"

    return filename


def get_scriptPath(filename):
    curr_path = pathlib.Path(__file__).parent #use .parent attr to remove script_runner.py from path

    return curr_path.joinpath(filename)


if len(sys.argv) < 2: #may remove in final version
    print('Usage: python3 script_runner.py <filename.py>')
    exit()


filename = get_filename()
script_path = get_scriptPath(filename)

result = subprocess.run(['python3', script_path], capture_output=True, check=True)
print(result.stdout.decode().strip())
