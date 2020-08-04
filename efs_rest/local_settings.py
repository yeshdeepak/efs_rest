import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
#EMAIL_HOST_PASSWORD = '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'
EMAIL_HOST_PASSWORD='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'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'yesh080690@gmail.com'

SECRET_KEY = '8a!=96l(@^p2d$6=p6tzaat+dm8ems2aqm%^o^g555+b)q7e75'

