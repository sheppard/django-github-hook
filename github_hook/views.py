import logging

import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError

from django.views.decorators.csrf import csrf_exempt
from .models import Hook, hook_signal

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig()


class HookView(GenericAPIView):
    renderer_classes = [JSONRenderer]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        # Explicit hook name
        name = kwargs.get('name', None)

        # Git repo information from post-receive payload
        if request.content_type == "application/json":
            payload = request.data
        else:
            # Probably application/x-www-form-urlencoded
            payload = json.loads(request.data.get("payload", "{}"))

        info = payload.get('repository', {})
        repo = info.get('name', None)

        # GitHub: repository['owner'] = {'name': name, 'email': email}
        # BitBucket: repository['owner'] = name
        user = info.get('owner', {})
        if isinstance(user, dict):
            user = user.get('name', None)

        if not name and not repo and not user:
            raise ParseError(
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
                if hook.path != "send-signal":
                    hook.execute()
                else:
                    hook_signal.send(HookView, info=info, repo=repo, user=user, request=request)
                    
        except Hook.DoesNotExist:
            # If there is not a script defined, then send a HookSignal
            hook_signal.send(HookView, request=request, payload=payload)
            logger.debug('Signal {} sent'.format(hook_signal))
        return Response({})
