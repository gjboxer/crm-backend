from django.contrib import admin
from .models import *
# Register your models here.

# Override the default Django admin site header
admin.site.site_header = 'Horizon Voyager Administration'

# Optionally, you can also customize the site title and index title
admin.site.site_title = 'Horizon Voyager Admin'
admin.site.index_title = 'Welcome to Horizon Voyager Admin'

class VoyaUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'mobile', 'login_type', 'is_active','date_joined')
    list_filter = ('login_type',)
    ordering = ['-date_joined']
    search_fields = ( 'email', 'first_name', 'mobile', 'login_type')

admin.site.register(User , VoyaUserAdmin)