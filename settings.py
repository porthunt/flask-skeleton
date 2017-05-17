from decouple import config
from unipath import Path
import os


PROJECT_DIR = Path(__file__).parent

SECRET_KEY = config('SECRET_KEY')
WTF_CSRF_ENABLED = config('WTF_CSRF_ENABLED', default=True, cast=bool)

DEBUG = config('DEBUG', default=False, cast=bool)
SERVER_HOST = config('SERVER_URL', default='0.0.0.0')
SERVER_PORT = config('SERVER_PORT', default=os.getenv('PORT'), cast=int)

DATABASE = {
    'nosql': {
        'user': config('DATABASE_USER'),
        'password': config('DATABASE_PASSWORD'),
        'database': config('DATABASE_NAME')
    }
}

ADMINS = (
    ('Joao Pedro Portela', 'porthunt@gmail.com')
)
MANAGERS = ADMINS

MEDIA_ROOT = PROJECT_DIR.parent.parent.child('media')
MEDIA_URL = '/media/'
FILE_UPLOAD_TEMP_DIR = '/tmp/'

LOGIN_URL = '/signin/'
LOGOUT_URL = '/signout/'

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
