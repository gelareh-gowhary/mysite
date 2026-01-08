from mysite.settings import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)r^3tlj=9n(^8i&y(b^mqiwdo21h)f8)r%u&s@-ocnkfv^080p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# sites framework
SITE_ID=2


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT=BASE_DIR/'static'
MEDIA_ROOT=BASE_DIR/'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
   
]
X_FRAME_OPTIONS='SAMEORIGIN'
