
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from customers import serializers, models


# Create your views here.
class CustomerView(ModelViewSet):
    queryset = models.CustomerCreditRiskParameters.objects.all()
    serializer_class = serializers.CustomerSerializer
    # permission_classes = (IsAuthenticated,)

    @action(
        methods=['get', 'post'],
        detail=True,
        serializers=serializers.CustomerSerializer
    )
    def customer(self, request):
        if request.method == 'POST':
            pass
        else:
            pass
        return Response("Well Done", status=200)