import os

from .base import *

SECRET_KEY    = os.environ["SECRET_KEY"]
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", ["*"])
DEBUG         = True

INSTALLED_APPS += [
    'django_extensions',
]

DATABASES = {
    'default' : {
        'ENGINE'   : 'django.db.backends.mysql',
        'NAME'     : os.environ.get('DB_NAME'),
        'USER'     : os.environ.get('DB_USER'),
        'PASSWORD' : os.environ.get('DB_PASSWORD'),
        'HOST'     : os.environ.get('DB_HOST'),
        'PORT'     : os.environ.get('DB_PORT'),
        'OPTIONS'  : {
            'charset' : 'utf8mb4'
        }
    }
}
