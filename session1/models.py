from django.db import models


class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    class Meta:
        db_table = 't_user'
