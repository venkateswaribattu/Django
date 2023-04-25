from django.shortcuts import render
# from django.http import HttpResponse
def homepage(request):
    # x='Welcome to Venkateswara University'
    # return HttpResponse(x)
    return render(request,'home.html')

def contactpage(request):
    # y='welcome to vekateswaracollege contact number'
    # return HttpResponse(y)
    return render(request,'contact.html')

def feedbackpage(request):
    # z='To check the feedbackpage to contact in this college students are professiors'
    # return HttpResponse(z)
    return render(request,'feedback.html')

def htmlpage(request):
    return render(request,'homepage.html')
