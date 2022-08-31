from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from chub.models import User_questions

@csrf_exempt
def guide(request):
    return render(request,'chub/guidelines.html')
@csrf_exempt
def q1(request):
    if request.method=='POST':
        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q1.html')
@csrf_exempt
def q2(request):
    if request.method=='POST':
        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q2.html')
@csrf_exempt
def q3(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q3.html')   
@csrf_exempt
def q4(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q4.html')

@csrf_exempt
def q5(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q5.html')

@csrf_exempt
def q6(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q6.html')

@csrf_exempt
def q7(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q7.html')

@csrf_exempt
def q8(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q8.html')

@csrf_exempt
def q9(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q9.html')

@csrf_exempt
def q10(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q10.html')

@csrf_exempt
def q11(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q11.html')

@csrf_exempt
def q12(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q12.html')

@csrf_exempt
def q13(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q13.html')

@csrf_exempt
def q14(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q14.html')

@csrf_exempt
def q15(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q15.html')

@csrf_exempt
def q16(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q16.html')

@csrf_exempt
def q17(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q17.html')

@csrf_exempt
def q18(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q18.html')

@csrf_exempt
def q19(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q19.html')

@csrf_exempt
def q20(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q20.html')

@csrf_exempt
def q21(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q21.html')

@csrf_exempt
def q22(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q22.html')

@csrf_exempt
def q23(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q23.html')

@csrf_exempt
def q24(request):
    if request.method=='POST':

        print(json.loads(request.body))
        data=json.loads(request.body)
        ques = User_questions(rollno=request.user,question=data['question'],score=data['score'],duration=datetime.datetime.now())
        ques.save()
    return render(request,'chub/Q24.html')