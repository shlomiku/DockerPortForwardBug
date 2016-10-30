#!/bin/bash
set -e
python manage.py runserver 0.0.0.0:5000
exec "$@"
