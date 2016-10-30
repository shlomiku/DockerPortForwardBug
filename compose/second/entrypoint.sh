#!/bin/bash
set -e
python manage.py runserver 0.0.0.0:6000
exec "$@"
