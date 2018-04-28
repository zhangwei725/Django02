from django.db import models

# Create your models here.
from day06.tools import ImageStorage


class UserInfo(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    "直接定位到media"
    head = models.FileField(upload_to='account/user/zhangsan/%Y%m%d', storage=ImageStorage())
