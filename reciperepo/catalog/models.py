from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    ingredients = models.TextField(default='...')
    directions = models.TextField(default='...')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default= 1)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title