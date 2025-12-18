# script_runner
I wanted a tool similar to the Windows Run dialog where I could conveniently execute a specified Python script from any working directory while avoiding having to navigate to that scripts' directory. 

### How to use 
script_runner.py is intended to be used through pyrun.sh on the command line followed by a script name, script abbreviation or an option. 

>pyrun exampleScript.py    
>pyrun exampleScript   
>pyrun ex

A list of supported options 
- init - Initialize JSON file with an empy JSON object
- update - Add new .py files to JSON
- list - print list of python scripts and their abbreviation
- help - print a list of utility options

> [!NOTE]  
> You do not need to update dir_files.JSON in order to run a script. you only update the JSON file if you want to run a script using an abbreviation.