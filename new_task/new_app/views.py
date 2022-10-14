from django.shortcuts import render, redirect
from .form import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import MyUser
from rest_framework import generics, status
from .serializers import myUserSerializer, CreateUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response



class myUserView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = myUserSerializer


class CreateUserView(APIView):
    serializer_class = CreateUserSerializer
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        form = self.serializer_class(data=request.data)
        if form.is_valid():
            username = form.data.get("username")
            email = form.data.get('email')
            first_name = form.data.get('first_name')
            last_name = form.data.get("last_name")
            password  = form.data.get('password')
            password_confirmation = form.data.get("password_confirmation")
            user_type = form.data.get("user_type")
            profile_picture = form.data.get("profile_picture")
            address = form.data.get("address")
            queryset = MyUser.objects.all()
            if queryset.exists():
                user = queryset[0]
                user.email = email
                user.password = password
                user.password_confirmation = password_confirmation
                user.first_name = first_name
                user.last_name = last_name
                user.user_type = user_type
                user.profile_picture = profile_picture
                user.address= address
                user.save( update_fields=['username',
                         "email", "password", "password_confirmation", 'first_name', 'last_name', 'user_type',
                        'profile_picture', 'address'
                    ])
                return redirect(myUserSerializer(user).data, status=status.HTTP_200_OK)
            else:
                user = MyUser(username=username, email= email, password=password, password_confirmation=password_confirmation, first_name=first_name, last_name=last_name,
                                user_type=user_type, profile_picture=profile_picture, address=address)
                user.save()
            return Response(myUserSerializer(user).data, status=status.HTTP_200_OK)
def homepage(request):
    return render(request=request, template_name="new_app/home.html")

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
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
