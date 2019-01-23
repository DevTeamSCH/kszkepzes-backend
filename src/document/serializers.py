from rest_framework import serializers
from common.serializers import CurrentUserProfileDefault
from . import models
from common.middleware import CurrentUserMiddleware

_max_count = 5


class DocumentSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.HiddenField(default=CurrentUserProfileDefault())
    uploaded_by_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Document
        fields = ('uploaded_by', 'uploaded_at', 'name', 'description', 'file', 'uploaded_by_name', 'solution', )

    def get_uploaded_by_name(self, obj):
        return obj.uploaded_by.full_name

    def validate(self, data):
        profile = CurrentUserMiddleware.get_current_user_profile()
        if data['solution'] not in profile.solution.all():
            raise serializers.ValidationError('You dont have permission!')
        count = models.Document.objects.filter(uploaded_by=profile, solution=data['solution']).count()
        if count >= _max_count:
            raise serializers.ValidationError('You cant upload more than ' + str(_max_count) + ' document to one solution!')
        return data
