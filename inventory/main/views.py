from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

def home(request: HttpRequest):

    response = render(request, "main/home.html")
    return response