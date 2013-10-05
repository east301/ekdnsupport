# Django settings for development environment.

import dj_database_url

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3')
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Make this unique, and don't share it with anybody.
SECRET_KEY = '@8t2z6y=-n&-+cbtdgztr449icx!%t7(w_x_+xemjf189pglq9'

ADDITIONAL_INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
)
