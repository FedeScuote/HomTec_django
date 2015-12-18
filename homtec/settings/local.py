from .base import *

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'homtec_django',
        'USER': 'homtec',
        'PASSWORD': 'homtec',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
