from django.db import models

class venkateswaridata(models.Model):
    first_name=models.CharField(max_length=100),
    last_name=models.CharField(max_length=100),
    email=models.CharField(max_length=100),
    fathername=models.CharField(max_length=100),
    mothername=models.CharField(max_length=100),
    location=models.CharField(max_length=100),
    age=models.IntegerField(),
    adharnumber=models.BigIntegerField()
