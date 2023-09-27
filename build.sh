		#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install	Lo comenté por que no se usa en esta instalacion
# pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
