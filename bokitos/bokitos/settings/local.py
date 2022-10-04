from .base import *
from pathlib import Path

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('db.sqlite3'),
        }
}

STATIC_URL = 'static/'
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
    ]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'