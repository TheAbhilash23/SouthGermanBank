from django.urls import path

from visitors import views

urlpatterns = [
    path('visitor/', views.VisitorView.as_view,),

]

