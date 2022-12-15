from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Visitor(models.Model):
    VisitorId = models.BigAutoField(
        _("id"),
        primary_key=True,
    )
    Name = models.CharField(
        _("Name"),
        max_length=225,
        null=True,
        blank=True,
        default='',
    )
    Telephone = models.CharField(
        _("Phone Number"),
        max_length=20,
        null=True,
        blank=True,
        default='',
    )
    Email = models.EmailField(
        _("Email Address"),
        max_length=250,
        null=True,
        blank=True,
        default='',
    )
    SocialMediaLink = models.CharField(
        _("Social Media Link"),
        max_length=155,
        null=True,
        blank=True,
        default='',
    )
    HighestEducation = models.CharField(
        _("Highest Education"),
        null=True,
        blank=True,
        max_length=150,
        default='',
    )
    Query = models.TextField(
        _("Write Your Query"),
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.Name}"

    class Meta:
        verbose_name = _("Visitor")
        verbose_name_plural = _("Visitors")
        db_table = "Visitor"
