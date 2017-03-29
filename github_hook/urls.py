from django.conf.urls import url

from .views import HookView

app_name = 'github_hook'
urlpatterns = [
    url(r'^(?P<name>[\w-]+)$',
        HookView.as_view()),
    url(r'^$',
        HookView.as_view()),
]
