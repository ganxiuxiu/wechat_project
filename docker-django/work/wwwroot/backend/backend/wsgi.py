"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
#
# application = get_wsgi_application()
import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append("/usr/src/app/backend/")

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "book.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "backend.settings"

application = get_wsgi_application()
