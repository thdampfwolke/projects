# ../core/forats/de/formats.py

# ----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/topics/i18n/formatting/#creating-custom-format-files
# https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date
# https://docs.djangoproject.com/en/3.2/topics/i18n/timezones/
# https://blog.mounirmesselmeni.de/2014/11/06/date-format-in-django-admin/

# ----------------------------------------------------------------------------
DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d_H-i-s'

# ----------------------------------------------------------------------------
# MONTH_DAY_FORMAT = 'j. F'

# DATE_FORMAT
# DATETIME_FORMAT
# SHORT_DATE_FORMAT
# SHORT_DATETIME_FORMAT

# THOUSAND_SEPARATOR = '\xa0'   # -> ,

# ----------------------------------------------------------------------------
# from django.conf.locale.en import formats as en_formats
# de_formats.DATE_FORMAT = "%Y-%m-%d"
# en_formats.DATE_FORMAT = "%Y-%m-%d"
#
# and for inputs (to accept 30/12/2017 or 30-12-2017)
# 
# de_formats.DATE_INPUT_FORMATS = ['%Y-%m-%d', '%Y-%m-%d']
# en_formats.DATE_INPUT_FORMATS = ['%Y-%m-%d', '%Y-%m-%d']
