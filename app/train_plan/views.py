from rest_framework import mixins,viewsets
from .models import Plan, Trial, Record
from .serializers import PlanSerializer, TrialSerializer, RecordSerializer

class PlanEdit(mixins.ListModelMixin,
               viewsets.GenericViewSet,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               mixins.CreateModelMixin):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class TrialEdit(mixins.ListModelMixin,
               viewsets.GenericViewSet,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               mixins.CreateModelMixin):
    queryset = Trial.objects.all()
    serializer_class = TrialSerializer

class RecordEdit(mixins.ListModelMixin,
               viewsets.GenericViewSet,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               mixins.CreateModelMixin):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
