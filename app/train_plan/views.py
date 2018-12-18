from rest_framework import mixins,viewsets
from .models import Plan, Trial, Record
from .serializers import PlanSerializer, TrialSerializer, RecordSerializer
from app.train_patcher.patch import Patcher

patch = Patcher()

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

    def partial_update(self, request, *args, **kwargs):
        if request.method == 'PATCH' :
            if request.data.get('state', -1) == 1:
                print("Changing the trial status!")
                patch.start_train(19, request.path)

            elif request.data.get('state', -1) == 2:
                print("Stop the training!")
                patch.stop_train()


        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class RecordEdit(mixins.ListModelMixin,
               viewsets.GenericViewSet,
               mixins.RetrieveModelMixin
                 ):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

