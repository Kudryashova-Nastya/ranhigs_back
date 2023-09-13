from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from app.models import Team
from app.serializers import TeamSerializer


class TeamViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated, ]
