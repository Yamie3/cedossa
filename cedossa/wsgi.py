import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cedossa.settings')  # Make sure 'cedossa' is your project name

application = get_wsgi_application()
