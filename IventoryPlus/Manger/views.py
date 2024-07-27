from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.


def Manger(request:HttpRequest):
    return render(request , 'pages/pages_manger.html')