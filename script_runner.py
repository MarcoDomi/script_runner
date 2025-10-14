#! /usr/bin/python3

import sys
import os
import pathlib

script_run_path = pathlib.Path(__file__).parent
script_run_path = script_run_path / 'utility_scripts'

for _, _, filenames in os.walk(script_run_path):
    print(filenames)

