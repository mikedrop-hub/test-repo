#!/bin/bash

# 1. Create the virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# 2. Activate the environment
source .venv/bin/activate

# 3. Upgrade pip and install requirements
echo "Installing dependencies and updating core build tools..."

pip install --upgrade pip setuptools wheel

if [ -f "hidden_stuff/requirements.txt" ]; then
    echo "Requirements found!"
    pip install -r hidden_stuff/requirements.txt
else
    echo "hidden_stuff/requirements.txt not found!"
fi


echo "Setup complete. You are now in the virtual environment."
echo ""
echo "To activate virtual environment (to run the file correctly):
'source .venv/bin/activate' or 'actvenv'
then 'python3 app.py'
"
