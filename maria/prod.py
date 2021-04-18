import os
import maria.settings

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'library',
        'HOST': 'lang-dictionary-postgres.postgres.database.azure.com',
        'PORT': '5432',
        'USER': os.environ['DB_USERNAME'],
        'PASSWORD': os.environ['DB_PASSWORD']
    }
}
