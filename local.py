import config
from board.settings import *

SECRET_KEY    = config.SECRET_KEY
ALLOWED_HOSTS = config.get("ALLOWED_HOSTS", ["*"])
DEBUG         = True

INSTALLED_APPS += [
    'django_extensions',
]

DATABASES = {
    'default' : {
        'ENGINE'   : 'django.db.backends.mysql',
        'NAME'     : config.DB_NAME,
        'USER'     : config.DB_USER,
        'PASSWORD' : config.DB_PASSWORD,
        'HOST'     : config.DB_HOST,
        'PORT'     : config.DB_PORT,
        'OPTIONS'  : {
            'charset' : 'utf8mb4'
        }
    }
}