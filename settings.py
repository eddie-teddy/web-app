# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Media files (User uploaded files)
# https://docs.djangoproject.com/en/3.2/ref/settings/#media-root

MEDIA_ROOT = BASE_DIR / 'media/'

# Media URL
# https://docs.djangoproject.com/en/3.2/ref/settings/#media-url

MEDIA_URL = '/media/'