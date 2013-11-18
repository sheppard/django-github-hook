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
        # Explicit hook name
        name = kwargs.get('name', None)

        # Git repo information from post-receive payload
        payload = json.loads(request.DATA.get('payload', "{}"))
        info = payload.get('repository', {})
        repo = info.get('name', None)

        # GitHub: repository['owner'] = {'name': name, 'email': email}
        # BitBucket: repository['owner'] = name
        user = info.get('owner', {})
        if isinstance(user, dict):
            user = user.get('name', None)

        if not name and not repo and not user:
            raise Exception(
                "No JSON data or URL argument : cannot identify hook"
            )

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
