#!/bin/bash

echo "BUILD START"
source mrbaten/env/bin/activate
# Install dependencies
python3 -m pip install -r requirements.txt

# Run Django management commands
python3 manage.py collectstatic --noinput --clear

echo "BUILD END"