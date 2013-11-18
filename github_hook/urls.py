from django.conf.urls import patterns, url, include

from .views import HookView

urlpatterns = patterns('',
    url(r'^(?P<name>[\w-]+)$', HookView.as_view()),
    url(r'^$', HookView.as_view()),
)
