from django.shortcuts import render

def homePage(request):
    return render(request,'homePage.html')
def contactPage(request):
    return render(request,'contactPage.html')
def feedbackPage(request):
    return render(request,'feedbackPage.html')
def servicePage(request):
    return render(request,'servicePage.html')
