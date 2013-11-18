github_hook
===========
Simple continuous integration for Django developers, taking the form of a Django app for managing Github post receive hooks.


Usage
-----

  - `pip install django-github-hook`
  - Add `github_hook` to `INSTALLED_APPS` in your settings.py
  - `./manage.py migrate` (or `./manage.py syncdb`)
  - Add e.g. `url('/hook', include('github_hook.urls'))` to your urls.py `urlpatterns`
  - Log into the Django admin console
  - Configure your hook with the folowing fields:
    - *Name*: Hook identifier
    - *User*: Github repo username
    - *Repo*: Github repo name
    - *Path*: Absolute path to script to execute
  - Go to your repo's "Service Hooks" settings on Github and add a WebHook URL:
    - http[s]://[yourwebsite]/hook
    - Github will post the repo information as part of the JSON payload
  - Alternatively, you can specify a specific hook by name:
    - http[s]://[yourwebsite]/hook/name
