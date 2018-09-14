from django.contrib import admin
from .models import Map

admin.site.register(Map)

class MapAdmin(admin.ModelAdmin):
    pass
