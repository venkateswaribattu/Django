from django.db import models

class ApplicationForm(models.Model):
    First_name=models.CharField(max_length=100)
    
    Last_name=models.CharField(max_length=100)
    Contact=models.BigIntegerField()
    Email_adders=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
    Institute=models.CharField(max_length=100)
    Course=models.CharField(max_length=100)
