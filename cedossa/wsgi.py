import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cedossa.settings')  # Make sure 'cedossa' is your project name

application = get_wsgi_application()

# Apply database migrations on startup. Render's default build command only runs
# `pip install`, so without this new tables (e.g. Flyer) never get created and
# their pages 500. `migrate` is idempotent, so running it on boot is safe.
if os.getenv('RUN_MIGRATIONS_ON_STARTUP', 'True') == 'True':
    try:
        from django.core.management import call_command
        call_command('migrate', interactive=False, verbosity=0)
    except Exception as exc:  # never let a migration hiccup take the whole site down
        print(f"[startup] migrate skipped/failed: {exc}", file=sys.stderr)
