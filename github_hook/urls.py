from django.conf.urls import patterns, url, include
from rest_framework import routers

from .views import HookView

router = routers.DefaultRouter()
router.register(r'', HookView(),'hook')

urlpatterns = patterns('',
	url(r'^', HookView.as_view()),
)
