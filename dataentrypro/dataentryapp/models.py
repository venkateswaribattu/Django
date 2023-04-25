from django.db import models

class StudentData(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    course=models.CharField(max_length=100)
    fee=models.IntegerField()
    location=models.CharField(max_length=100)
    institute=models.CharField(max_length=100)
