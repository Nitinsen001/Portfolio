#!/bin/bash
pip install --upgrade pip
pip install -r requirements.txt --target /tmp/packages
export PYTHONPATH=/tmp/packages:$PYTHONPATH
python manage.py collectstatic --noinput