from django.contrib import admin
from . import models
# from app_first import models

class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'create_at')
    search_fields = ('name', 'content')

admin.site.register(models.Post, PostAdmin)