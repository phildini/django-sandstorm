from django.conf import settings

def sandstorm(request):
    if settings.SANDSTORM:
        return {'SANDSTORM': True}
    return {}
