from django.urls import path
from . import views
from .views import myUserView, CreateUserView


app_name = 'new_app'

urlpatterns = [
    path("api", myUserView.as_view()),
    path("api/create-room", CreateUserView.as_view()),
    path("register", views.register_request, name = 'register'),
    path("login", views.login_request, name = "login"),
    path("logout", views.logout_request, name = "logout"),

]
