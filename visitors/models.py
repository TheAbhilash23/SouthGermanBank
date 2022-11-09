from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class VisitorEnquiry(models.Model):
    VisitorId = models.BigAutoField(
        _("id"),
        primary_key=True,
    )
    Name = models.CharField(
        _("Name"),
        max_length=225,
        null=True,
        blank=True,
    )
    Telephone = models.CharField(
        _("Phone Number"),
        max_length=20,
        null=True,
        blank=True,
    )
    Email = models.EmailField(
        _("Email Address"),
        max_length=250,
        null=True,
        blank=True,
    )
    SocialMediaLink = models.CharField(
        _("Social Media Link"),
        max_length=155,
        null=True,
        blank=True,
    )
    HighestEducation = models.CharField(
        _("Highest Education"),
        null=True,
        blank=True,
        max_length=150
    )
    Query = models.TextField(
        _("Write Your Query"),
        null=True,
        blank=True,
    )
