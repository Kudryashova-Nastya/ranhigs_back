from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import TeamViewSet

router = DefaultRouter()
router.register(r'', TeamViewSet, basename='team')

urlpatterns = [
    path('team', include(router.urls)),
]
