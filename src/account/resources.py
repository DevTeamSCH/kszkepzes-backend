from import_export import resources
from . import models


class SignUpResource(resources.ModelResource):
    class Meta:
        model = models.Profile
        fields = (
            'user__first_name',
            'user__last_name',
            'user__email',
            'motivation_about',
            'motivation_profession',
            'motivation_exercise',
        )
