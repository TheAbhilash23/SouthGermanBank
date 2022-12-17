from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    CreatedBy = models.PositiveIntegerField(
        _("Create by"),
        null = True,
        blank = True,
    )
    CreationTime = models.DateTimeField(
        _("Time of Creation"),
        auto_now_add=True,
    )

    class Meta:
        abstract = True

