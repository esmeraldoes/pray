"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)z9(n(yj8j&)&ke43^11ob91=b)ex$*fkk%*a)#b_g1a_bqliz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'bibleApp.apps.BibleappConfig',
    'bibleApp',
    'mygrpcapp',
    'communityapp',
    'prayertrack',
    'corsheaders',
    'django_extensions',

    'rest_auth',
    'social_django',
    'drf_spectacular',
    'django_filters',
    'django_elasticsearch_dsl',
    'rest_framework.authtoken',
    # 'django_grpc',
    'grpc_django',
    
    

    'rest_framework',
    'django.contrib.sites',  
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',  
    'allauth.socialaccount.providers.google',

]


GRPC_SETTINGS = {
    "DEFAULT": {
        "RCP_SERVER": "C:\\Users\\HP\\Desktop\\shadow\\mygrpcapp\\bible_service.py",  
    },
}


GRPC_MAX_WORKERS = 10
# GRPC_SERVER_ADDRESS = '127.0.0.1'
GRPC_SERVER_ADDRESS = '18.170.215.183'


GRPC_ENABLED = True
GRPCSERVER = {
    'servicers': ['mygrpcapp.bible_service.BibleServiceServicer'],
    'async': False,
}


MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'backend.urls'


CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS = [
    'http://18.170.215.183',
    'http://localhost:8000',
   
]





# CORS_ALLOWED_ORIGINS = [    
#     "https://prayerapp1.onrender.com",
#     "http://localhost:8000",
#     "http://127.0.0.1:8000",
#     "http://localhost:8000",
# ] + ALLOWED_HOSTS


AUTH_USER_MODEL = 'bibleApp.CustomUser'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



AUTHENTICATION_BACKENDS = [
    
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
]
SITE_ID = 3
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',  
        'rest_framework.authentication.SessionAuthentication', 
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 25,
    
}

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'
    },
}

# AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # 'mandatory' or 'optional'
# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_UNIQUE_USERNAME = False
# SOCIALACCOUNT_QUERY_EMAIL = True
# SOCIALACCOUNT_AUTO_SIGNUP = False  # Users must confirm their email after social signup

# # Email settings
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'your-smtp-host.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your-email@example.com'
# EMAIL_HOST_PASSWORD = 'your-email-password'
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# Configure Django Allauth settings
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'APP': {
            'client_id': '1450115019174104',
            'secret': '0ed8e65c4e050522b27e684b20653c4c',
            'key': '',
        }
    },
    # 'google': {
    #     'SCOPE': ['profile', 'email'],
    #     'APP': {
    #         'client_id': '942851459790-okvqvkft4cnmjode76k5e8ch8vbc20ln.apps.googleusercontent.com',
    #         'secret': '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',
    #         'key': '',
    #     }
    # },
    'google': {
        'SCOPE': ['profile', 'email'],
        'APP': {
            'client_id': '802944885729-5p6m0ku0hgmbirpgguai9s794lppqgui.apps.googleusercontent.com',
            'secret': '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',
            'key': '',
        }
    },
}

REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'bibleApp.serializers.CustomLoginSerializer',
}

# Set the authentication URLs
LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'

# LOGIN_REDIRECT_URL = '/'

# LOGIN_REDIRECT_URL = '18.170.215.183:8000/api/profile/'
# # LOGIN_REDIRECT_URL = 'http://127.0.0.1:8000/api/profile/'

# # LOGIN_REDIRECT_URL = 'http://127.0.0.1:8000/api/login'

# LOGOUT_REDIRECT_URL = 'http://127.0.0.1:8000/accounts/login'

LOGIN_REDIRECT_URL = 'https://18.170.215.183:8000/api/profile/'
LOGOUT_REDIRECT_URL = 'https://18.170.215.183:8000/accounts/login'


SPECTACULAR_SETTINGS = {
    'TITLE': 'REGIMEN ENDPOINT',
    'DESCRIPTION': 'Endpoints for the prayer app',
    'VERSION': '1.0.0',
}
#### ADMIN CREDENTIALS
#username: david
#password: balm
#mail: davidbalm@gmail.com


# Username: admin1
# mail: admin1@gmail.com
# Password: oneadmin90



SWAGGER_SETTINGS = {
    
    # 'DEFAULT_API_URL': 'http://127.0.0.1/api/swagger/',
    'DEFAULT_API_URL': 'http://18.170.215.183/api/swagger/',
    # 'DEFAULT_API_URL': 'https://prayerapp1.onrender.com/api/swagger/',
    'DEFAULT_VALIDATOR_CLASS': None,
   
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
