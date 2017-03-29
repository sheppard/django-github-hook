import os
from django.test.utils import setup_test_environment
import django
from django.core.management import call_command


os.environ['DJANGO_SETTINGS_MODULE'] = "tests.settings"
setup_test_environment()
django.setup()
call_command('makemigrations')
call_command('migrate')
