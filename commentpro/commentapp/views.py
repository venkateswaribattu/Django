from django.shortcuts import render
from .models import CommentData

def featchingData(request):
    if request.method=='GET':
        comment=CommentData.objects.all().order_by('-id')
        return render(request,'comment.html',{'abc':comment})

    else:
        CommentData(
            Comment=request.POST['name']
        ).save()
        comment=CommentData.objects.all().order_by('-id')
        return render(request,'comment.html',{'abc':comment})
