#!/bin/bash
# Run script_runner.py


# Get the directory where this script is located
SCRIPT_DIR="$HOME/.local/my_python_tools/script_runner.py"

# Check if the Python file exists
if [ ! -f "$SCRIPT_DIR" ]; then
    echo "Error: $SCRIPT_DIR not found."
fi

# Run the Python file
python3 "$SCRIPT_DIR" $1