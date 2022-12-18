from customers import models
from rest_framework import serializers


class CustomerInformationSerializer(serializers.ModelSerializer):
    """
    This class is used to store the personal information of a customer.
    """

    class Meta:
        model = models.CustomerInformation
        exclude = ('Customer',)


class CustomerSerializer(serializers.ModelSerializer):
    CustomerInformationSerializer(required=False, many=True)

    class Meta:
        """
        This class is used to store the personal information of a customer's credit risk parameters.
        """
        model = models.CustomerCreditRiskParameters
        fields = '__all__'
