from django.contrib import admin
from visitors import models
# Register your models here.

@admin.register(models.VisitorEnquiry)
class VisitorEnquiryAdmin(admin.ModelAdmin):
    pass




