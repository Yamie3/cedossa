#!/usr/bin/env bash
# Render build script for the CeDossa Django app.
# Exit immediately if any command fails so a broken build is reported clearly.
set -o errexit

pip install -r requirements.txt

# Collect static assets into STATIC_ROOT so WhiteNoise can serve them.
python manage.py collectstatic --no-input

# Apply database migrations.
python manage.py migrate
