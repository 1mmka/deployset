import os
from pathlib import Path

# путь к родительской директории
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '@dvave(p21z_#)r%a2jsxte%xa4okv($j!8_+k6)&s+^#wv*bn'
    # может использоваться при создании токенов JWT

# false в разработке, иначе true
DEBUG = False

# разрешенные ip
ALLOWED_HOSTS = ['*']


SECURE_HSTS_SECONDS = 60 * 60 * 24 * 365 # защищенное подключение к сайту в течении года

SECURE_HSTS_INCLUDE_SUBDOMAINS = True # разрешено использовать поддомены(разделенный контент на сайте)

SECURE_HSTS_PRELOAD = True # разрешено заранее подгружать информацию о сайте

SECURE_SSL_REDIRECT = True # разрешаем изменение HTTP запросов на HTTPS

SESSION_COOKIE_SECURE = True # отправление куки сессии только если подключение защищенное

CSRF_COOKIE_SECURE = True # отправление данных только при csrf то есть защищенное

# приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'easy_thumbnails',
    'captcha',
    'app'
]

# посредники / доп.проверка
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lesson_56.urls'

# шаблоны
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

# путь к wsgi
WSGI_APPLICATION = 'lesson_56.wsgi.application'


# если в разработке - postgresql, если готовый - sqlite3 
if DEBUG == True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

# отправка email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

# кэш
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': '',
    }
}

# валидаторы пароля
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


# язык / timezone
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Asia/Almaty'
USE_I18N = True
USE_TZ = True

# статические файлы
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR / 'static-root')

# медиа файлы
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'