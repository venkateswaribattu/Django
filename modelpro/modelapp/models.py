from django.db import models

class studentdata(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    contact=models.BigIntegerField()
    fee=models.IntegerField()
    course=models.CharField(max_length=50)
    iname=models.CharField(max_length=80)
