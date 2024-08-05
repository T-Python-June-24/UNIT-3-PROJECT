from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages




# Create your views here.


def sign_up(request: HttpRequest):
    if request.method == "POST":
        password = request.POST.get("password")
        password_confirmation = request.POST.get("password_confirmation")

        if password != password_confirmation:
            messages.error(request, "Passwords do not match!", "alert-danger")
            return render(request, "accounts/signup.html", {})
           
        try:
            new_user=User.objects.create_user(username=request.POST["username"],email=request.POST["email"],password=request.POST["password"],first_name=request.POST["first_name"],last_name=request.POST["last_name"])
            new_user.save()
            messages.success(request,'sign up successfully',"alert-success")
            return redirect("accounts:sign_in")
        except Exception as e: 
            messages.error(request, f"Error during sign up: {str(e)}", "alert-danger")
    return render(request, "accounts/signup.html", {})




def sign_in(request):
    if request.method == "POST":
        try:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Welcome back!', 'alert-success')
                return redirect(request.GET.get("next", "/"))
            else:
                messages.error(request, "Invalid username or password", "alert-danger")
        except Exception as e:
            messages.error(request, f"Error during sign in: {str(e)}", "alert-danger")

    return render(request, "accounts/signin.html")
def log_out(request: HttpRequest):
    logout(request)

    return redirect(request.GET.get("next", "/"))
