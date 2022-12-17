from rest_framework import routers

from customers import views as customer_views

router = routers.SimpleRouter()

router.register(r'customer', customer_views.CustomerView, basename='customer_views')

urlpatterns = router.urls
