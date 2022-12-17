from django.contrib import admin
from visitors import models
# Register your models here.

@admin.register(models.Visitor)
class VisitorAdmin(admin.ModelAdmin):
    pass
