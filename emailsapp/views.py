from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Your view logic here
    return render(request,"/home/utkarsh-singh/Documents/DjangoProjects/EmailSender/mywebsite/emailsapp/templates/emailsapp/base.html")
