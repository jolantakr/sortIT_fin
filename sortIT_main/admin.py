from django.contrib import admin
from .models import Category, Containers, Location


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'detail1_name', 'detail2_name', 'detail3_name')
    search_fields = ('title',)


class ContainersAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'detail1_name', 'detail2_name', 'detail3_name')
    search_fields = ('title',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'street', 'city', 'country')
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Containers, ContainersAdmin)
admin.site.register(Location, LocationAdmin)
