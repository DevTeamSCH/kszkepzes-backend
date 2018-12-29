from threading import local

_profile = local()


class CurrentUserMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _profile.value = request.user
        return self.get_response(request)

    def get_current_profile():
        return _profile.value.profile
