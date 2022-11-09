from customers import models
from rest_framework import serializers


class CustomerCreditRiskParametersSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomerCreditRiskParameters


class CustomerInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomerInformation


class CustomerSerializer(serializers.ModelSerializer):
    CustomerInformationSerializer(required=False, many=True)
    CustomerCreditRiskParametersSerializer(required=False, many=True)


