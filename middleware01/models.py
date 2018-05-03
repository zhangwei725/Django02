from django.db import models


# Create your models here.
class Ip(models.Model):
    cip = models.IPAddressField()
    last_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'T_IP'
