from django.contrib import admin
from .models import *


class Exercise2WorksAdmin(admin.ModelAdmin):
    list_display = ('person_name', 'company')


class Exercise2LivesAdmin(admin.ModelAdmin):
    list_display = ('person_name', 'city')


admin.site.register(Exercise2Works, Exercise2WorksAdmin)
admin.site.register(Exercise2Lives, Exercise2LivesAdmin)
