from django.db import models

class fbView(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    Startin_place=models.CharField(max_length=100)
    Destinatio_place=models.CharField(max_length=100)
    Seates=models.IntegerField()
