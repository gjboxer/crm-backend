from django.db import models
from categories.models import Category
from agents.models import Agent


class Lead(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    age = models.IntegerField(default=0)
    hotel_name = models.CharField(max_length=30, default='')
    hotel_address = models.CharField(max_length=30, default='')
    country = models.CharField(max_length=30, default='')
    phone_number = models.CharField(max_length=30, default='')
    url=models.CharField(max_length=30, default='')
    description = models.TextField(default='')

    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL
    )
    agent = models.ForeignKey(
        Agent,
        null=True,
        on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'