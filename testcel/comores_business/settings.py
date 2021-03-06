"""
Django settings for comores_business project.
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import environ
from decouple import config
from decimal import Decimal as D

from oscar.defaults import *
from oscar import get_core_apps
from oscar import OSCAR_MAIN_TEMPLATE_DIR
from django.utils.translation import ugettext_lazy as _
from oscar_accounts import TEMPLATE_DIR as ACCOUNTS_TEMPLATE_DIR

####################### Environment variables 1  ###################

location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), x)

env = environ.Env()

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = config('SECRET_KEY')

ROOT_URLCONF = 'comores_business.urls'
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
           
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = ['178.128.199.234','.comores-en-ligne.com',
                 'localhost',]

PHONENUMBER_DEFAULT_REGION = "FR"

WSGI_APPLICATION = 'comores_business.wsgi.application'


############## Applications inslatés ##############################

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'compressor',
    'widget_tweaks',
    'debug_toolbar',
    'paypal',
    'oscar_accounts',
    'localflavor',
    'contact',
    'mathfilters'
 
]

INSTALLED_APPS = INSTALLED_APPS + get_core_apps(
    ['promotions', 'customer','address','catalogue','shipping',
     'partner','basket','checkout','payment','order','search',
     'dashboard','offer',])


SITE_ID = 1

############### Middlewere config et templates ######################

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware'
   # 'middleware.virtuel.IPMiddleware',
]




TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates'),
                  OSCAR_MAIN_TEMPLATE_DIR, ACCOUNTS_TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
            'debug': DEBUG,
        },
    },
]


############## Database et caches  configuration #################


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'naoufad_production',#saandi_prod',
        'USER': 'naoufad_user',#saandi',
        'PASSWORD': 'Youstina@@2015',
        'HOST': 'localhost',
        'PORT': '',
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'yousti-naoufad',
    }
}


################# Password validation ##############################

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


###################### add dashboard Shipping, PayPal, Account ########################


OSCAR_DASHBOARD_NAVIGATION += [
    {
        'label': _('Shipping'),
        'children': [
            {
                'label': 'Shipping',
                'url_name': 'dashboard:shipping-method-list',
            },
        ]
    },
]




OSCAR_DASHBOARD_NAVIGATION.append(
    {
        'label': _('PayPal'),
        'icon': 'icon-globe',
        'children': [
            {
                'label': _('PayFlow transactions'),
                'url_name': 'paypal-payflow-list',
            },
            {
                'label': _('Express transactions'),
                'url_name': 'paypal-express-list',
            },
        ]
})


OSCAR_DASHBOARD_NAVIGATION.append(
    {
        'label': 'Comptes',
        'icon': 'icon-globe',
        'children': [
            {
                'label': 'Comptes',
                'url_name': 'accounts-list',
            },
            {
                'label': 'Transfers',
                'url_name': 'transfers-list',
            },
            {
                'label': 'Rapport de revenu différés',
                'url_name': 'report-deferred-income',
            },
            {
                'label': 'Rapport Bénéfice/Perte',
                'url_name': 'report-profit-loss',
            },
        ]
    })

ACCOUNTS_UNIT_NAME = 'Compte MpessaOnLine'
ACCOUNTS_UNIT_NAME_PLURAL ='Comptes MpessaOnLine'
ACCOUNTS_MIN_LOAD_VALUE = D('1.02')
ACCOUNTS_MAX_ACCOUNT_VALUE = D('1000.00')


########################## PayPal settings ########################

PAYPAL_CURRENCY='EUR'

PAYPAL_SANDBOX_MODE = False 
PAYPAL_CALLBACK_HTTPS = True
PAYPAL_API_VERSION = '119 '

PAYPAL_ALLOW_NOTE=False
PAYPAL_BRAND_NAME='Comores En Ligne'
PAYPAL_CUSTOMER_SERVICES_NUMBER='0651933748'

PAYPAL_CURRENCY = PAYPAL_PAYFLOW_CURRENCY = 'EUR' 
PAYPAL_PAYFLOW_DASHBOARD_FORMS = True 

PAYPAL_API_USERNAME = config('PAYPAL_API_USERNAME')
PAYPAL_API_PASSWORD = config('PAYPAL_API_PASSWORD')
PAYPAL_API_SIGNATURE = config('PAYPAL_API_SIGNATURE')


#################### Internationalization ##########################

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


################## Configurations des staticfiles ###################


STATIC_ROOT = os.path.join(PROJECT_ROOT, '../static')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


MEDIA_ROOT=os.path.join(BASE_DIR, 'MEDIA')
MEDIA_URL='/media/'


################# django-toolbar config ############################

INTERNAL_IPS = ['10.188.112.191','127.0.0.1']



#################### Paramettre oscar ##############################

from django.core.urlresolvers import reverse_lazy

OSCAR_SHOP_NAME = 'Comores En Ligne'
OSCAR_SHOP_TAGLINE = ''
OSCAR_HOMEPAGE = reverse_lazy('promotions:home')

OSCAR_REQUIRED_ADDRESS_FIELDS = ('first_name', 'last_name', 'line1',
                                 'line4', 'postcode', 'country')

OSCAR_USE_LESS = False

OSCAR_DEFAULT_CURRENCY = 'EUR'

OSCAR_PRODUCTS_PER_PAGE=124
OSCAR_RECENTLY_VIEWED_PRODUCTS=40

OSCAR_OFFERS_PER_PAGE=120
OSCAR_REVIEWS_PER_PAGE=30
OSCAR_NOTIFICATIONS_PER_PAGE=30
OSCAR_EMAILS_PER_PAGE=50
OSCAR_ORDERS_PER_PAGE=50
OSCAR_ADDRESSES_PER_PAGE=30
OSCAR_STOCK_ALERTS_PER_PAGE=30
OSCAR_DASHBOARD_ITEMS_PER_PAGE=150

OSCAR_ALLOW_ANON_CHECKOUT = False

OSCAR_INITIAL_ORDER_STATUS = 'En attente'
OSCAR_INITIAL_LINE_STATUS = 'En attente'

OSCAR_PROMOTIONS_ENABLED = True
OSCAR_PRODUCT_SEARCH_HANDLER = None

OSCAR_ORDER_STATUS_PIPELINE = {
    'En attente': ('En cours de traitement', 'Annulé',),
    'En cours de traitement': ('Traité', 'Annulé',),
    'Annulé': (),
    'Traité':(),
}

OSCAR_LINE_STATUS_PIPELINE={
    'En attente': ('En cours de traitement', 'Annulé',),
    'En cours de traitement': ('Traité', 'Annulé',),
    'Annulé': (),
    'Traité':(),
}


OSCAR_ORDER_STATUS_CASCADE = {
    'En cours de traitement': 'En cours de traitement',
    'Annulé': 'Annulé',
    'Traité': 'Traité',
}



#####################  Haystack - solr - Backend ####################

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr',
        'INCLUDE_SPELLING': True,
    },
}



################## Envoi d'email Backend #########################

EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST ='localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD =''
EMAIL_PORT = 25
EMAIL_USE_TLS = False

OSCAR_SEND_REGISTRATION_EMAIL = True
OSCAR_FROM_EMAIL= 'no-replay@mail.comores-en-ligne.com'
SEND_BROKEN_LINK_EMAILS = True


SERVER_EMAIL='danger@mail.comores-en-ligne.com'

ADMINS = (
    ('Naoufad Saandi', 'sidiyoustina@gmail.com'),
)

EMAIL_SUBJECT_PREFIX = '[Comores En Ligne Error]'

MANAGERS = ADMINS


from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
    
}



#################   Journalisation du système de fichier   #########


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s',
        },
        'simple': {
            'format': '[%(asctime)s] %(message)s'
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'oscar': {
            'level': 'DEBUG',
            'propagate': True,
        },
        'oscar.catalogue.import': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'oscar.alerts': {
            'handlers': ['null'],
            'level': 'INFO',
            'propagate': False,
        },

        # Django loggers
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'level': 'WARNING',
            'propagate': True,
        },
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },

        # Third party
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sorl.thumbnail': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
    }
}

