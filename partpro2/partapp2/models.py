from django.db import models

class venkateswariData(models.Model):
    Salary=models.IntegerField()
    Location=models.CharField(max_length=100)
    Job_role=models.CharField(max_length=100)
    Contact=models.BigIntegerField()
