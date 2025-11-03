#! /usr/bin/python3

import sys
import subprocess
import pathlib
import json

CURR_PATH = pathlib.Path(__file__).parent #NOTE remove when a glob solution is implemented for _create_set()
JSON_path = CURR_PATH.joinpath('dir_files.JSON')

class tool_manager:
    '''enable retrieval of python script file name using a user specfied abbreviation'''
    def __init__(self):
        try:
            with open(JSON_path, 'r') as f:
                self.file_dict = json.load(f)
        except:
            print('ERROR: dir_files.JSON not found')
            exit()

    def __getitem__(self, abbrev): #use angle brackets to retrieve filename from dictionary
        try:
            return self.file_dict[abbrev]
        except KeyError:
            raise KeyError #in case abbrev not in file_dict

    def update_dict(self):
        '''add any new files and file abbreviations to class dictionary'''

        # can't append new key-value pairs to json file.
        # must read data from json into dictionary, change the dictionary, then write data back to the json file

        dict_set = self._create_set('dict')
        dir_set = self._create_set('dir')

        diff_set = dir_set.difference(dict_set) #filenames that are present in directory but not in the class dictionary

        for filename in diff_set: 
            abbrev = input(f"{filename} - enter abbreviated name: ") 
            self.file_dict.update({abbrev:filename})

        with open(JSON_path, 'w') as file_json: 
            json.dump(self.file_dict,file_json)

    def list_files(self): 
        '''print a list of files with it's abbreviation'''
        print(f"FILENAME ALIASES\n{'-'*16}")
        for abbrev, filename in self.file_dict.items():
            print(f"{filename:15}{abbrev:>4}")

    def init_json(self):
        '''write empty brackets to json file'''
        with open(JSON_path, 'w') as json_file:
            json.dump({}, json_file)

    def list_options(self):
        "print all options and a description"

        option_list = [
            ("init", "Initialize JSON file with an empy JSON object"),
            ("update", "Add new .py files to JSON"),
            ("list", "print list of python scripts and their abbreviation"),
            ("help", "print a list of utility options"),
        ]

        print(f"OPTIONS\n{'-'*7}")
        for name, desc in option_list:
            print(f"{name:>6} - {desc}")

    def _create_set(self,mode): 
        '''returns a set created from either file dictionary or from files in directory'''

        new_set = set()

        if mode == 'dict':
            for _, value in self.file_dict.items(): #NOTE each character in value is being stored in different variable.
                new_set.add(value)

        elif mode == 'dir':
            for f in pathlib.Path.iterdir(CURR_PATH): #NOTE experiment with glob syntax
                if f.name[-3:] == '.py' and f.name != 'script_runner.py':
                    new_set.add(f.name)

        return new_set


def file_exec(filename):
    try:
        script_path = CURR_PATH.joinpath(filename)
        result = subprocess.run(['python3', script_path], capture_output=True, check=True)
        print(result.stdout.decode().strip())
    except subprocess.CalledProcessError:
        print("ERROR: file not found")


def file_case(file_arg, pytool):  # TODO try using get .get dictionary method
    try:
        filename = pytool[file_arg]
    except KeyError:
        filename = file_arg
        if ".py" not in file_arg:
            filename = file_arg + ".py"

    file_exec(filename)


def run_options(option, pytool):
    option_choices = {'list': pytool.list_files, 'update': pytool.update_dict, 'init': pytool.init_json, 'help': pytool.list_options}
    run_option = option_choices.get(option, 'is-file')

    if run_option == 'is-file':
        file_case(option, pytool)
    else:
        run_option() 


def main():
    if len(sys.argv) < 2: #may remove in final version
        print('Usage: python3 script_runner.py <filename.py>')
        exit()

    option = sys.argv[1]
    pytool = tool_manager() 

    run_options(option, pytool)

main()
