from django.shortcuts import render,redirect
from .models import ToDoData
def  ToDoData(request):
    Good=ToDoData.objects.all()
    return render(request,'mainPage.html',{'abc':Good})
def addingdata(request):
    if request.method == 'GET':
        return render(request,'homePage.html')
    else:
        ToDoData(
        title=request.POST['title'],
        desc=request.POST['desc'],
        date=request.POST['date']
        ).save()
        return redirect(ToDoData)
def featchingdata(request,id):
    data=ToDoData.objects.filter(id=id)
    return render(request,'addingPage.html',{'abc':data})
