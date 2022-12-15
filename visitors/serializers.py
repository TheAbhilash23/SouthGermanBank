from rest_framework import serializers
from visitors import models


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Visitor
        # exclude = ('',)