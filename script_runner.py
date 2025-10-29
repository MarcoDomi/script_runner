#! /usr/bin/python3

import sys
import subprocess
import pathlib

CURR_PATH = pathlib.Path(__file__).parent
class tool_manager:
    def __init__(self):
        self.file_dict = {}

    def __getitem__(self, abbrev):
        try:
            return self.file_dict.get(abbrev)
        except KeyError:
            return KeyError

    def update_dict(self):
        dict_set = self._create_set('dict')
        dir_set = self._create_set('dir')

        diff_set = dir_set.difference(dict_set) #filenames that are present in directory but not in file dictionary

        for filename in diff_set:
            abbrev = input(f"{filename} - enter abbreviated name: ")
            self.file_dict.update({abbrev:filename})

    def list_files(self):
        '''print a list of files and it's abbreviation'''
        print(f"Filename   short name\n{'-'*7}")
        for abbrev, filename in self.file_dict.items():
            print(f"{filename} - {abbrev}")

    def _create_set(self,mode): 
        '''returns a set created from either file dictionary or from files in directory'''

        new_set = set()

        if mode == 'dict':
            for _, value in self.file_dict:
                new_set.add(value)

        elif mode == 'dir':
            for f in pathlib.Path.iterdir(CURR_PATH):
                if f.name[-3:] == '.py' and f.name != 'script_runner.py':
                    new_set.add(f.name)

        return new_set



def get_scriptPath(filename):
    curr_path = pathlib.Path(__file__).parent #use .parent attr to remove script_runner.py from path

    return curr_path.joinpath(filename)


def main():
    if len(sys.argv) < 2: #may remove in final version
        print('Usage: python3 script_runner.py <filename.py>')
        exit()

    option = sys.argv[1]
    pytool = tool_manager()

    if option == 'list':
        pytool.list_files()

    elif option == 'update':
        pytool.update_dict()

    else: 
        try:
            filename = pytool[option]
        except KeyError:

            if ".py" not in filename:
                filename = filename + ".py"

        script_path = get_scriptPath(filename)
        result = subprocess.run(['python3', script_path], capture_output=True, check=True)
        print(result.stdout.decode().strip())



main()

