from django.db import models
from django.contrib.auth.models import User
class User_questions(models.Model):
    id=models.AutoField
    rollno=models.ForeignKey(User,to_field='username',on_delete=models.CASCADE)
    question=models.IntegerField(default=0)
    time=models.IntegerField(default=0)
    score=models.IntegerField(default=0)