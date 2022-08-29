from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from chub.models import User_questions
@login_required
def guide(request):
    return render(request,'chub/guidelines.html')

@csrf_exempt
def q1(request):
    if request.method=='POST':
        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'], time=data['time'],score=data['score'])
        ques.save()
    return render(request,'chub/index1.html')

