from import_export import resources, widgets, fields

from account.models import Profile
from . import models


class EventResource(resources.ModelResource):
    visitors = fields.Field(
        attribute='visitors',
        widget=widgets.ManyToManyWidget(
            model=Profile, separator=' ,', field='full_name'),
    )

    class Meta:
        model = models.Event
        fields = (
            'name',
            'date',
            'visitors',
        )


class NoteResource(resources.ModelResource):
    created_by = fields.Field()
    user = fields.Field()

    class Meta:
        model = models.Note
        fields = (
            'user',
            'event__name',
            'note',
            'created_at',
            'updated_at',
            'created_by',
        )

    def dehydrate_created_by(self, obj):
        return obj.created_by.full_name

    def dehydrate_user(self, obj):
        return obj.user.full_name
