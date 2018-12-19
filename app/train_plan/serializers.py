
from rest_framework import serializers
from .models import *

class RepoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Repository
        fields = '__all__'

    def to_representation(self, instance):

        data = super().to_representation(instance)
        return data


class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = ['id', 'repository', 'name', 'model', 'create_time', 'engine', 'para', 'trials']

    def to_representation(self, instance):

        data = super().to_representation(instance)
        return data


class TrialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trial
        fields = ['id', 'plan', 'state', 'devices', 'create_time', 'last_time',
                  'total_epoch', 'iteration_per_epoch', 'train_records', 'test_records']

    def to_representation(self, instance):

        data = super().to_representation(instance)
        return data

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['epoch', 'iteration', 'time', 'iou', 'acc', 'recall', 'precision', 'loss']

    def to_representation(self, instance):

        data = super().to_representation(instance)
        return data


# class TrainRecordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TrainRecord
#         fields = ['epoch', 'iteration', 'time']
#
#     def to_representation(self, instance):
#
#         data = super().to_representation(instance)
#         return data
#
#
# class TestRecordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TestRecord
#         fields = ['epoch', 'iteration', 'time']
#
#     def to_representation(self, instance):
#
#         data = super().to_representation(instance)
#         return data

