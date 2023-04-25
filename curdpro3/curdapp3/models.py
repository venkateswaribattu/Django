from django.db import models
class EmpData(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    company=models.CharField(max_length=100)
    salary=models.IntegerField()
    location=models.CharField(max_length=100)
    expirence=models.IntegerField()
