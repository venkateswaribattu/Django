from django.shortcuts import render,redirect
from .models import Courses
from .models import FeedbackData
from.forms import RegistrationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='loginpage/')
def homepage(request):
    return render(request,'homepage.html')


@login_required(login_url='loginpage/')
def contactpage(request):
    return render(request,'contactpage.html')


@login_required(login_url='loginpage/')
def servicepage(request):
    courses=Courses.objects.all()
    return render(request,'servicepage.html',{'courses':courses})

#
# @login_required(login_url='loginpage/')
# def feedbackpage(request):
    #     return render(request,'feedbackpage.html')


@login_required(login_url='loginpage/')
def gallerypage(request):
    return render(request,'gallerypage.html')

def loginpage(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(homepage)
        else:
            return HttpResponse('Invalid Details')
    else:
        return render(request,'loginpage.html')

def logoutpage(request):
    logout(request)
    return redirect(loginpage)

def registerpage(request):
    if request.method =='GET':
        form=RegistrationForm()
        return render(request,'registerpage.html',{'form':form})
    else:
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(user.password)
            form.save()
            return redirect(loginpage)
        else:
            return HttpResponse("Invalid form")

@login_required(login_url='loginpage/')
def feedbackpage(request):
    if request.method=='GET':
        comment=FeedbackData.objects.all().order_by('-id')
        return render(request,'feedbackpage.html',{'abc':comment})

    else:
        FeedbackData(
            content=request.POST['name'],
            date=request.POST['date'],
            user_name=request.POST['user']
        ).save()
        comment=FeedbackData.objects.all().order_by('-id')
        return render(request,'feedbackpage.html',{'abc':comment})
