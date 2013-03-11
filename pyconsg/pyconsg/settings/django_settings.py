"""Django settings for pyconsg project."""
import os

from pyconsg.settings.base_settings import PROJECT_ROOT


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Singapore'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en', 'English'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

ROOT_URLCONF = 'pyconsg.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'pyconsg.wsgi.application'

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, 'pyconsg/fixtures'),
)
