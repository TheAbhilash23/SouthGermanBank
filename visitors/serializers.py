from rest_framework import serializers
from visitors import models


class VisitorEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VisitorEnquiry


class VisitorSerializer(serializers.ModelSerializer):
    VisitorEnquirySerializer(required=False, many=True)


class VisitorReadSerializer(serializers.ModelSerializer):
    VisitorEnquirySerializer(read_only=True)
