github\_hook
============

Simple continuous integration for Django developers, taking the form of
a Django app for managing GitHub (or BitBucket) post receive hooks.

.. image:: https://travis-ci.org/sheppard/django-github-hook.svg?branch=master
    :target: https://travis-ci.org/sheppard/django-github-hook

Usage
-----

-  ``pip install django-github-hook``
-  Add ``github_hook`` to ``INSTALLED_APPS`` in your settings.py
-  ``./manage.py migrate`` (or ``./manage.py syncdb``)
-  Add e.g. ``url(r'^hook/', include('github_hook.urls'))`` to your
   urls.py ``urlpatterns``
-  Log into the Django admin console
-  Configure your hook with the folowing fields:

   -  *Name*: Hook identifier
   -  *User*: Repo username
   -  *Repo*: Repo name
   -  *Path*: Absolute path to script to execute

-  Go to your repo's "Service Hooks" settings on GitHub (or BitBucket) and add a
   WebHook/POST URL:

   -  http[s]://[yourwebsite]/hook
   -  The repo information will be read from the JSON payload

-  Alternatively, you can specify a specific hook by name:

   -  http[s]://[yourwebsite]/hook/name


