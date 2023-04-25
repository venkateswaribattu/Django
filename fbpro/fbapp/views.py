from django.shortcuts import render,redirect
import faker
fake=faker.Faker()
from .models import fbView
def fbdata(request):
    abc=fbView.objects.all()
    return render (request,'mainPage.html',{'abc':abc})

def booking(request):
    if request.method=='GET':
        abc=fbView.objects.all()
        return render(request,'bookingPage.html',{'abc':abc})
    else:
        fbView(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        Startin_place=request.POST['sp'],
        Destinatio_place=request.POST['dp'],
        Seates=fake.random_element(elements=(4,5,6,7))

        ).save()

        abc=fbView.objects.all()
        return render(request,'bookingPage.html',{'abc':abc})
        return redirect(fbdata)
def display(request):
    abc=fbView.objects.all()
    return render (request,'display.html',{'abc':abc})
