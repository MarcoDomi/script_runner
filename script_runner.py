#! /usr/bin/python3

import sys
import subprocess
import pathlib

CURR_PATH = pathlib.Path(__file__).parent
class tool_manager:
    def __init__(self):
        self.file_dict = {}

    def update_dict(self):
        dict_set = self._create_dict_set()
        dir_set = self._create_dir_set()

        diff_set = dir_set.difference(dict_set) #filenames that are present in directory but not in file dictionary

        for f in diff_set:
            pass

    def list_files(self):
        '''print a list of files and it's abbreviation'''
        for filename, abbrev in self.file_dict.items():
            print(f"{filename} - {abbrev}")

    def _create_dict_set(self): 
        '''returns a set created from file dictionary'''

        dict_set = set()
        for _, value in self.file_dict:
            dict_set.add(value)

        return dict_set

    def _create_dir_set(self):
        '''iterate thru all elements in dictionary to create a set'''
        dir_set = set()
        for f in pathlib.Path.iterdir(CURR_PATH):
            if f.name[-3:] == '.py' and f.name != 'script_runner.py':
                dir_set.add(f.name)

        return dir_set


def get_filename():
    filename = sys.argv[1]

    if ".py" not in filename:
        filename = filename + ".py"

    return filename


def get_scriptPath(filename):
    curr_path = pathlib.Path(__file__).parent #use .parent attr to remove script_runner.py from path

    return curr_path.joinpath(filename)


def main():
    if len(sys.argv) < 2: #may remove in final version
        print('Usage: python3 script_runner.py <filename.py>')
        exit()

    filename = get_filename()
    script_path = get_scriptPath(filename)

    result = subprocess.run(['python3', script_path], capture_output=True, check=True)
    print(result.stdout.decode().strip())

def class_tester(): #NOTE delete later
    foo = tool_manager()
    foo.update_dict()


# main()
class_tester()
