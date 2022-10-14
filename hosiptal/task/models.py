# core/models.py
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Blog(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    summary = models.TextField()
    image = models.ImageField()
    draft = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']


