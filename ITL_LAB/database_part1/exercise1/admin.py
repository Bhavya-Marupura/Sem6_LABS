from django.contrib import admin
from .models import *


class Exercise1CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class Exercise1PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category',)


admin.site.register(Exercise1Category, Exercise1CategoryAdmin)
admin.site.register(Exercise1Page, Exercise1PageAdmin)
