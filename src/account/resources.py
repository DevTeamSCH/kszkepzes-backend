from import_export import resources, widgets, fields
from . import models


class SignUpResource(resources.ModelResource):
    groups = fields.Field(
        attribute='groups',
        widget=widgets.ManyToManyWidget(model=models.GroupChoice, separator=' ,', field='choice'),
    )

    class Meta:
        model = models.Profile
        fields = (
            'user__first_name',
            'user__last_name',
            'user__email',
            'nick',
            'groups',
            'motivation_about',
            'motivation_profession',
            'motivation_exercise',
            'signed',
        )
