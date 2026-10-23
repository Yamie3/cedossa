release: python manage.py migrate --no-input
web: python manage.py migrate --no-input && python manage.py collectstatic --no-input && waitress-serve --host=0.0.0.0 --port=$PORT cedossa.wsgi:application
