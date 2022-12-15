
from django.urls import path

from datareader import views

urlpatterns = [
    path('datareader/', views.DataReader.as_view, ),

]