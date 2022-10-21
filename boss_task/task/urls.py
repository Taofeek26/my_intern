from django.urls import path
from .views import RegistrationView, ProfileView, HomeView
from django.contrib.auth import views

urlpatterns = [
    path('home/', HomeView.as_view(), name= 'home'),
    path('register/', RegistrationView.as_view(), name= 'register'),
    path('login/', views.LoginView.as_view(), name= 'login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name= 'profile'),

    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]