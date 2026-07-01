#!/bin/bash
pip install --break-system-packages -r requirements.txt
python manage.py collectstatic --noinput