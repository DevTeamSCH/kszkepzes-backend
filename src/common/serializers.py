from rest_framework import compat


class CurrentUserProfileDefault(object):
    def set_context(self, serializer_field):
        self.user = serializer_field.context['request'].user

    def __call__(self):
        return self.user.profile

    def __repr__(self):
        return compat.unicode_to_repr('%s()' % self.__class__.__name__)
