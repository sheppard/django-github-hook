SECRET_KEY = '1234'
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'github_hook',
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
ROOT_URLCONF = 'github_hook.urls'
