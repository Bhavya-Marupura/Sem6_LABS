from django.contrib import admin
from .models import *


class Exercise3AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)


class Exercise3PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)


class Exercise3BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date',)


admin.site.register(Exercise3Author, Exercise3AuthorAdmin)
admin.site.register(Exercise3Publisher, Exercise3PublisherAdmin)
admin.site.register(Exercise3Book, Exercise3BookAdmin)
