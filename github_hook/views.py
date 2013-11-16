from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer

from django.views.decorators.csrf import csrf_exempt
import json
from .models import Hook

class HookView(GenericAPIView):
    renderer_classes = [JSONRenderer]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        # Git repo information from Github post-receive payload
        payload = json.loads(request.DATA.get('payload', "{}"))
        info = payload.get('repository', {})
        try:
            repo = info.get('name', None)
            user = info.get('owner', {}).get('name', None)
        except:
            try:
                name = kwargs['name']
            except:
                raise Exception("No JSON data or URL argument : cannot identify hook")


        # Find and execute registered hook for the given repo, fail silently
        # if none exist
        try:
            hook = None
            if name:
                hook = Hook.objects.get(name=name)
            elif repo and user:
                hook = Hook.objects.get(user=user, repo=repo)
            if hook:
                hook.execute()
        except Hook.DoesNotExist:
            pass
        return Response({})
