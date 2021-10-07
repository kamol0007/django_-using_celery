from django.contrib import admin
from .models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_en', 'title_ru', 'created_at', 'updated_at')


admin.site.register(Task, TaskAdmin)
