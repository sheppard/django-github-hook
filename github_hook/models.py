from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django import dispatch
import subprocess


@python_2_unicode_compatible
class Hook(models.Model):
    name = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    repo = models.CharField(max_length=255)
    path = models.CharField(max_length=255)

    def execute(self):
        subprocess.call([self.path])

    def __str__(self):
        return "%s (%s/%s)" % (self.name, self.user, self.repo)

    class Meta:
        db_table = 'github_hook'


class HookSignal(dispatch.Signal):
    pass

hook_signal = HookSignal()
