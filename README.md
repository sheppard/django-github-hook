github_hook
===========
Simple continuous integration for Django developers, taking the form of a Django app for managing github post receive hooks.


Usage:
  - Place `github_hook` in your Django project's apps directory
  - Add `github_hook` to `INSTALLED_APPS`
  - `./manage.py migrate`
  - Add e.g. `url('/hook', include('github_hook.urls'))` to your `urlpatterns`
  - Log into the Django admin console
  - Configure your hook with the folowing fields:
    - *Name*: Hook description
    - *User*: Github repo username
    - *Repo*: Github repo name
    - *Path*: Absolute path to script to execute
  - Go to your repo's Service Hooks settings on Github and add a WebHook URL:
    - http[s]://[yourwebsite]/hook
    - It should work?
