from django.db import models


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    head = models.ImageField(upload_to='upload', default='xxx/default.png')
    is_del = models.IntegerField(default=0)
