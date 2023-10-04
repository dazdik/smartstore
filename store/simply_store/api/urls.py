from django.urls import include, path
from rest_framework import routers

from api.views import BasketViewSet, ProductViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'baskets', BasketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
