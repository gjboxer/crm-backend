from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
from django.conf import settings
class Lead(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30,blank=True,null=True)
    email = models.EmailField(max_length=30)
    age = models.IntegerField(blank=True,null=True)
    hotel_name = models.CharField(max_length=30, default='')
    hotel_address = models.CharField(max_length=30, default='',blank=True,null=True)
    country = models.CharField(max_length=30, default='')
    phone_number = models.CharField(max_length=30, default='')
    url=models.CharField(max_length=30,blank=True,null=True)
    description = models.TextField(blank=True,null=True)

    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL
    )
    agent = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
