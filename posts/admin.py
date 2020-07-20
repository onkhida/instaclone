from django.contrib import admin
from .models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'date', 'caption']
    list_filter = ['date', 'user']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'date', 'text']
    list_filter = ['user', 'post', 'date', 'text']

