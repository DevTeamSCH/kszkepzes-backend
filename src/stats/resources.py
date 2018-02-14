from import_export import resources, widgets, fields

from account.models import Profile
from . import models


class EventResource(resources.ModelResource):
    visitors = fields.Field(
        attribute='visitors',
        widget=widgets.ManyToManyWidget(model=Profile, separator=' ,', field='full_name'),
    )

    class Meta:
        model = models.Event
        fields = (
            'name',
            'date',
            'visitors',
        )
