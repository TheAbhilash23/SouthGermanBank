from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class DataReader(ModelViewSet):

    pass

    # queryset = Post.objects.none()
    # serializer_class = PostSerializer
    # permission_classes = (IsAuthenticated,)
    # http_method_names = ['get', ]
    #
    # def list(self, request):
    #     query = request.GET.get('query', None)
    #     query_set = Post.objects.filter(title__icontains=query)
    #     return Response(self.serializer_class(query_set, many=True).data,
    #                     status=status.HTTP_200_OK)