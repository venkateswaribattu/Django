from django.db import models

class UserData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email_id=models.EmailField(max_length=50)
    mobile=models.BigIntegerField()
    course=models.CharField(max_length=50)
    institute=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
