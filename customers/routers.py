from rest_framework import routers

from . import views as customer_views

router = routers.BaseRouter()

router.register(r'customer', customer_views.CustomerView, basename='Customer')

# urlpatterns = router.get_urls()
