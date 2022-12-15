from customers import models
from rest_framework import serializers

class CustomerInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomerInformation
        exclude = ('Customer',)


class CustomerSerializer(serializers.ModelSerializer):
    CustomerInformationSerializer(required=False, many=True)
    class Meta:
        model = models.CustomerCreditRiskParameters
