from django.db import models
class ToDoData(models.Model):
    title=models.CharField(max_length=1000)
    desc=models.TextField(max_length=1000)
    date=models.DateField(max_length=500)
