"""
WSGI config for image project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image.settings')

# Get the WSGI application
application = get_wsgi_application()

# Alias the application for deployment platforms like Vercel
app = application  # Required for Vercel deployment
