from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class userType(models.TextChoices):
    DOCTOR = "DOC", "Doctor"
    PATIENT = "PAT", "Patient"


class MyUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=userType.choices, default=userType.DOCTOR, null=True)
    profile_picture = models.ImageField(verbose_name='avatar', null=True, blank=True)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username =models.CharField(max_length=50, default='Username')
    first_name= models.CharField(max_length=50, default='FIRST NAME')
    last_name= models.CharField(max_length=50, default= 'LAST NAME')
    password= models.CharField(max_length=50, default= 'Pass123')
    password_confirmation=models.CharField(max_length=50, default='Pass123')
