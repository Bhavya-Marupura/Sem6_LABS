from django.contrib import admin
from .models import *


class Exercise4ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price',)


admin.site.register(Exercise4Product, Exercise4ProductAdmin)
