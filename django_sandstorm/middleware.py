from django.contrib import auth
from django.contrib.auth.middleware import RemoteUserMiddleware
from django.contrib.auth.models import User

from six.moves.urllib.parse import unquote

class SandstormMiddleware(RemoteUserMiddleware):
    """
    Requires 'django.contrib.auth.backends.RemoteUserBackend' in 
    settings.AUTHENTICATION_BACKENDS
    """

    header = 'HTTP_X_SANDSTORM_USER_ID'

    def process_request(self, request):
        super(SandstormMiddleware, self).process_request(request)

        if request.META.get('HTTP_X_SANDSTORM_USERNAME') and hasattr(request, 'user'):
            request.user.first_name = unquote(
                request.META.get('HTTP_X_SANDSTORM_USERNAME')
            )
            request.user.save()
