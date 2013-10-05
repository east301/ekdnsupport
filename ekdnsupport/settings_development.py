# Django settings for development environment.

import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3')
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('SECRET_KEY') or '@8t2z6y=-n&-+cbtdgztr449icx!%t7(w_x_+xemjf189pglq9'

ADDITIONAL_INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
)

# Path to a directory to be used to store GPX/KML data
GPX_ROOT = os.path.join(BASE_DIR, 'gpx')
