from django.shortcuts import render,redirect
from .models import ToDoData
def ToDoView(request):
    stds=ToDoData.objects.all()
    return render(request,'mainPage.html',{'abc':stds})
def homepage(request):
    if request.method=='GET':
        return render(request,'homePage.html')
    else:
        ToDoData(
        title=request.POST['title'],
        desc=request.POST['desc'],
        date=request.POST['date']
        ).save()
        return redirect(ToDoView)
def fetchingdata(request,id):
    stds=ToDoData.objects.filter(id=id)
    return render(request,'addingPage.html',{'abc':stds})

def update(request,id):
    abc=ToDoData.objects.get(id=id)
    return render(request,'updatePage.html',{'abc':abc})


def updating(request,id):
    abc=ToDoData.objects.get(id=id)
    abc.title=request.POST['title']
    abc.desc=request.POST['desc']
    abc.date=request.POST['date']
    abc.save()
    return redirect(ToDoView)
def delete(request,id):
    abc=ToDoData.objects.get(id=id)
    abc.delete()
    return redirect(ToDoView)
