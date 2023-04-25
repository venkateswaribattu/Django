from django.shortcuts import render
from.models import UserData
from django.http import HttpResponse
def contactView(request):
    if request.method=='GET':
        return render(request,'user.html')
    else:
        UserData(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        email_id=request.POST['email'],
        mobile=request.POST['mobile'],
        course=request.POST['course'],
        institute=request.POST['iname'],
        location=request.POST['location']
        ).save()
        return render(request,'user.html')
