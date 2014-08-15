from __future__ import absolute_import

from .base import *

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ('127.0.0.1',)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

try:
    import rosetta
    INSTALLED_APPS += ('rosetta',)
except ImportError:
    print 'rosetta is not installed'

try:
    import django_extensions
    INSTALLED_APPS +=('django_extensions',)
except ImportError:
    print 'django_extensions is not installed'

try:
    import debug_toolbar
    # INSTALLED_APPS.append('debug_toolbar')
except ImportError:
    # print 'debug_toolbar is not installed'
    pass

TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.debug',)

WSGI_AUTO_RELOAD = True
