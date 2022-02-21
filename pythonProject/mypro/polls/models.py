from django.db import models


# Create your models here


class Photo(models.Model):
    num = models.AutoField(primary_key=True)
    art = models.CharField(max_length=50, blank=True, null=True)
    case = models.CharField(max_length=50, blank=True, null=True)
    des = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'photo'

