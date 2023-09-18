from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.models import Team
from app.serializers import TeamSerializer, UserSerializer


class TeamViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated, ]


class ProfileViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]

    def list(self, request, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
