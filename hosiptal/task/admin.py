from django.contrib import admin
from django.utils import timezone

from .models import Category, Blog


admin.site.register(Category)
admin.site.register(Blog)