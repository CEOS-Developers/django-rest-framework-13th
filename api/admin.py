from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'created_at', 'updated_at' ]
    list_display_links = ['id', 'nickname']

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ['id', 'following', 'followed']
    list_display_links = ['id', 'following', 'followed']

admin.site.register(Post)
admin.site.register(File)
admin.site.register(Heart)