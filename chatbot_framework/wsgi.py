"""
WSGI config for chatbot_framework project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os,sys

sys.path.append('home/ubuntu/base')
sys.path.append('home/ubuntu/base/venv/lib/python3.12/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot_framework.settings')

application = get_wsgi_application()
