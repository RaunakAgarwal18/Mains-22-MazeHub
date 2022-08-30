from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
class User_questions(models.Model):
    id=models.AutoField
    rollno=models.ForeignKey(User,to_field='username',on_delete=models.CASCADE)
    question=models.IntegerField(default=0)
    duration=models.DateTimeField(default=datetime.now())
    score=models.IntegerField(default=0)