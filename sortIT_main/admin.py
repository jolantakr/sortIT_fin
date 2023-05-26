from django.contrib import admin
from .models import Type, Category

list_display = ('name', 'address', 'phone', 'working_time',)
search_fields = ('name', 'address',)

admin.site.register(Type)
admin.site.register(Category)
