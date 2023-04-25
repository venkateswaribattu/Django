from django.db import models

class Courses(models.Model):
    course_name=models.CharField(max_length=100)
    fee=models.IntegerField()
    duration=models.CharField(max_length=100)
    start_date=models.DateTimeField(max_length=100)
    trainer_name=models.CharField(max_length=100)
    trainer_exp=models.CharField(max_length=100)
    trainer_mode=models.CharField(max_length=100)

class FeedbackData(models.Model):
    content=models.TextField(max_length=100)
    date=models.DateTimeField()
    user_name=models.CharField(max_length=100)
