import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(1, os.path.join(BASE_DIR, 'extra_apps'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6(mgvj8w#6#ik5omx_ub4hjr0_u9mb9@v53m-v9e32jfh(ync9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MY_APPS = [
    'books',
    'user_center',
    'message',
    'drf_apis',
    'statistic',
    'commerce',
    'corsheaders',
    'djcelery',
    'xadmin',
    'crispy_forms',
    'DjangoUeditor',
    'rest_framework',

]

INSTALLED_APPS += MY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DjangoBooks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'DjangoBooks.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_table',
        'USER': 'jsf',
        'PASSWORD': 'jj123456',
        'HOST': '47.96.109.219',
        'PORT': '3306',

    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

from django.contrib.messages import constants as message_constants

MESSAGE_LEVEL = message_constants.INFO

# 将存入session的对象序列化
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh_hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, "static")

USER_CHOICES = [
    (0, '普通会员'),
    (1, 'VIP会员'),
    (2, '黄金会员'),
]

DB_FIELD_VALID_CHOICES = [
    (0, '未删除'),
    (1, '已删除'),
]
PAY_CHOICES = [
    (0, '货到付款'),
    (1, '微信支付'),
    (2, '支付宝支付'),
]

DINNER_CHOICES = [
    (0, '待下单'),
    (1, '已下单')
]

REDIS_DEPLOY_FLAG = 'test'
REDIS_SERVICE = {
    # 测试时用
    'test': ('127.0.0.1', '6379'),
    # 上线后用
    'online': ('47.96.109.219', '6379')
}
# -------------------eamil settions end---------------
CELERY_BROKER_URL = 'redis://%s:%s/5' % (  # 配置celery存储地址
    REDIS_SERVICE[REDIS_DEPLOY_FLAG][0],
    REDIS_SERVICE[REDIS_DEPLOY_FLAG][1]
)
CELERY_ACCEPT_CONTENT = ['json']

CELERY_TASK_SERIALIZER = 'json'

CELERY_RESULT_BACKEND = 'django-db'

import redis

R = redis.Redis(host='127.0.0.1', port=6379, db=0)

CACHES = {
    'default': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://%s:%s/1" % (REDIS_SERVICE[REDIS_DEPLOY_FLAG][0],
                                         REDIS_SERVICE[REDIS_DEPLOY_FLAG][1]),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
# 部署的django服务的IP和端口
DJANGO_SERVICE = ('127.0.0.1', 8888)
# ################ email settings begin #################
EMAIL_HOST = 'smtp.163.com'

EMAIL_PORT = 465

# 163邮箱
EMAIL_HOST_USER = "18162358456@163.com"

# 邮箱的客户端授权密码
EMAIL_HOST_PASSWORD = "Jsf950218"

EMAIL_USE_SSL = True

# ################ email settings end ###################
# 允许所有站点跨域请求
CORS_ORIGIN_ALLOW_ALL = True
