from django.db import models
class PracticeData(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    contact=models.BigIntegerField()
    course=models.CharField(max_length=100)
    fee=models.IntegerField()
