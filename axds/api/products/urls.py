from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import CategoryViewSet, ProductViewSet

app_name = 'products'

router = SimpleRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
