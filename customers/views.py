
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from customers import serializers, models


# Create your views here.
class CustomerView(ModelViewSet):
    """
    Automatically creates four methods of CRUD operations. All we need to do is create a
    queryset of all customers and instantiate serializer class.
    """
    queryset = models.CustomerCreditRiskParameters.objects.all()
    serializer_class = serializers.CustomerSerializer
    # permission_classes = (IsAuthenticated,)

    @action(
        methods=['get', 'post',
                 ],
        detail=True,
        serializers=serializers.CustomerSerializer,
        url_path='Customer',
    )
    def crud(self, request):
        if request.method == 'POST':
            pass
        elif request.method == 'GET':
            pass
        return Response("Well Done", status=200)
