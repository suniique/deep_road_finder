from django.db import models


class Repository(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    dir_path = models.CharField(max_length=256)
    main_file = models.CharField(max_length=256)
    create_time = models.DateTimeField(auto_now_add=True)


class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    create_time = models.DateTimeField(auto_now_add=True)

    model = models.CharField(max_length=64)
    engine = models.CharField(max_length=64)
    para = models.TextField()

    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)


class Trial(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True)
    last_time = models.DateTimeField(auto_now=True)
    state = models.IntegerField(default=0)
    devices = models.CharField(max_length=64)
    total_epoch = models.IntegerField()
    iteration_per_epoch = models.IntegerField()
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)


class Record(models.Model):
    epoch = models.IntegerField()
    iteration = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)


class TrainRecord(Record):
    train_loss = models.FloatField()
    train_acc = models.FloatField()
    train_iou = models.FloatField()
    train_recall = models.FloatField()
    train_precision = models.FloatField()
    trial = models.ForeignKey(Trial, on_delete=models.CASCADE)

class TestRecord(Record):
    test_loss = models.FloatField()
    test_acc = models.FloatField()
    test_iou = models.FloatField()
    test_recall = models.FloatField()
    test_precision = models.FloatField()
    trial = models.ForeignKey(Trial, on_delete=models.CASCADE)

