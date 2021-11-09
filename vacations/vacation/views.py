from rest_framework import viewsets, mixins
from rest_framework import permissions
from django.utils import timezone

from vacation.permissions import IsManager
from vacation.models import Vacation
from vacation.serializers import VacationSerializer, ApproveVacationSerializer


class VacationViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = Vacation.objects.all().order_by('-created')
    serializer_class = VacationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        qs = Vacation.objects.all().order_by('-created')

        if self.request.user.is_manager is False:
            qs = qs.filter(user=self.request.user)

        return qs


class ApproveVacationViewSet(mixins.RetrieveModelMixin,
                             mixins.ListModelMixin,
                             mixins.UpdateModelMixin,
                             viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vacation.objects.all().order_by('-created')
    serializer_class = ApproveVacationSerializer
    permission_classes = [permissions.IsAuthenticated, IsManager]

    def perform_update(self, serializer):
        serializer.save(approver=self.request.user, approved_date=timezone.now())
