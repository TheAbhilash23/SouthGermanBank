from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from . import serializers, models


# Create your views here.
class CustomerViewSet(ModelViewSet):
    """
    Automatically creates four methods of CRUD operations for customer's personal information as well as
    their credit risk parameters.
    """
    serializer_class = serializers.CustomerSerializer
    queryset = models.CustomerCreditRiskParameters.objects.all()
    permission_classes = [permissions.AllowAny]

    @action(
        methods=['get', 'post',
                 ],
        detail=True,
        serializer_class=serializers.CustomerSerializer,
        url_path='customer-analysis',
    )
    def analysis(self, request):
        """
        This method is used to get the analysis report of each customer if it exists.


        If it does not exist, we pass the credit risk parameters in order to get the report.
        This method will save the report.
        """
        if request.method == 'POST':
            pass
        elif request.method == 'GET':
            pass
