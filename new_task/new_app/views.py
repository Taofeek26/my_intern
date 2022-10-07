from django.shortcuts import render, redirect
from .form import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def homepage(request):
    return render(request=request, template_name="new_app/home.html")


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.address = form.cleaned_data['address']
            login(request, user)
            messages.success(request, "Registration Successful")
            return redirect("new_app:homepage")
        messages.error(request, "Unsuccessful Registration, Kindly check the password matched or try increase the strenght of the password")
    form = NewUserForm()
    return render(request=request, template_name="new_app/register.html", context={"form": form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"you are now logged in as {username}.")
                return redirect("new_app:homepage")
            else:
                messages.error(request, "invalid username or password")
        else:
            messages.error(request, "invalid username or password")
    form = AuthenticationForm
    return render(request=request, template_name="new_app/login.html", context={"form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "you have successfully logged out.")
    return redirect ("new_app:homepage")



# Create your views here.
