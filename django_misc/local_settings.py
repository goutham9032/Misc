import os

INSTALLED_APPS = [
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # user defined apps
    'app',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE =  'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = '/'

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


