import os
#import cloudinary  # cloudinary
#import cloudinary.uploader  # cloudinary
from functools import partial

import cloudinary.api  # cloudinary
from decouple import config
import dj_database_url


cloudinary.config(
    cloud_name="dr-time",
    api_key="318177226937779",
    api_secret="yL1bD-dSRo8ZJzV0iE6VUmfx2Bk"
)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['*']


# Application definition

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LIB_APPS = [
    'cloudinary',
    'rest_framework',
    'django_filters',
]

LEGGACY_APPS = [
    'agenda',
    'cliente',
    'clinica',
    'horario',
    'marcacao',
    'profissional',
    'especialidade',
    'clinica_profissional',
]

INSTALLED_APPS = (
    DEFAULT_APPS + LIB_APPS + LEGGACY_APPS
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'drtimeapis.urls'

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

WSGI_APPLICATION = 'drtimeapis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

parse_database =partial(dj_database_url.parse, conn_max_age=600)

DATABASES = {'default': config('DATABASE_URL', default=default_dburl, cast=parse_database), }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
ESTADOS_CHOICES = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins')
)

SEXO_CHOICES = (
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino'),
    ('Outros', 'Outros'),
)

DIAS_CHOICES =(
    ('Segunda', 'Segunda'),
    ('Terca', 'Terca'),
    ('Terca', 'Terca'),
    ('Quarta', 'Quarta'),
    ('Quinta', 'Quinta'),
    ('Sexta', 'Sexta'),
    ('Sabado', 'Sabado'),
    ('Domingo', 'Domingo'),
)

ST_AGENDA_CHOICES = (
    ('Marcado', 'Marcado'),
    ('Confirmado', 'Confiramdo'),
    ('Cancelado Cliente', 'Cancelado Cliente'),
    ('Cancelado Profissional', 'Cancelado Profissional'),
    ('Cancelado Clinica', 'Cancelado Clinica'),
    ('Em atendimento', 'Em atendimento'),
    ('Atendido', 'Atendido'),
    ('Remarcado', 'Remarcado'),

)
