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
        repo = info.get('name', None)
        user = info.get('owner', {}).get('name', None)

        # Find and execute registered hook for the given repo, fail silently
        # if none exist
        if repo and user:
            try:
                hook = Hook.objects.get(user=user, repo=repo)
                hook.execute()
            except Hook.DoesNotExist:
                pass
        return Response({})
