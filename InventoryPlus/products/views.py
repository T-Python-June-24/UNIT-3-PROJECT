from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.


def test_view(request: HttpRequest):

    return render (request, 'products/test.html')