from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import TeamViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r'team', TeamViewSet, basename='team')
router.register(r'profile', ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
]
