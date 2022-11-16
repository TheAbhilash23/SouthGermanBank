from django.contrib import admin
from customers import models
# Register your models here.


class CustomerInformationInline(admin.StackedInline):
    model = models.CustomerInformation


@admin.register(models.CustomerCreditRiskParameters)
class CustomerCreditRiskParametersAdmin(admin.ModelAdmin):
    inlines = [CustomerInformationInline,
               ]
