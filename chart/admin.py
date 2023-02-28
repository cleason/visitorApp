from django.contrib import admin
from .models import *

# Register your models here.

class AdminVisitor(admin.ModelAdmin):
    list_display = ('click', 'viewer')
    
admin.site.register(Visitor, AdminVisitor)
