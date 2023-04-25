from django.db import models
class CommentData(models.Model):
    Comment=models.CharField(max_length=1000,default='hi')
