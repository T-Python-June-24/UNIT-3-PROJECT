from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def dashboard_view(request:HttpRequest ):

    return render(request, "index.html")


