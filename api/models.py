from django.db import models
from datetime import datetime
# Create your models here.

class NameSpace(models.Model):

    name = models.CharField(max_length=100)
    createTime = models.DateTimeField("createTime", default=datetime.now)
    updateTime = models.DateTimeField("updateTime", default=datetime.now)
    creater = models.CharField(max_length=100)
    updater = models.CharField(max_length=100)
    delete_flag = models.BooleanField(default="False")

    def __str__(self):
        return self.name


class Project(models.Model):

    name = models.CharField(max_length=100, null=True)
    namespace = models.ForeignKey(NameSpace, on_delete=models.CASCADE)
    createTime = models.DateTimeField("createTime", default=datetime.now)
    updateTime = models.DateTimeField("updateTime", default=datetime.now)
    creater = models.CharField(max_length=100)
    updater = models.CharField(max_length=100)
    delete_flag = models.BooleanField(default="False")
    swagger_json = models.TextField()
    host = models.CharField(max_length=100, null=True)
    basePath = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name