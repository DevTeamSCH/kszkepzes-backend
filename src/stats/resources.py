from django.contrib.auth.models import User
from import_export import resources, widgets, fields

from . import models


class EventResource(resources.ModelResource):
    visitors = fields.Field(
        attribute='visitors',
        widget=widgets.ManyToManyWidget(model=User, separator=' ,', field='username'),
    )

    class Meta:
        model = models.Event
        fields = (
            'name',
            'date',
            'visitors',
        )
