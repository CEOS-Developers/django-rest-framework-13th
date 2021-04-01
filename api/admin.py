from django.contrib import admin
from .models import Profile, Post, Media, PeopleTag, HashTag


class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]


admin.site.register(Profile, ProfileAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields]


admin.site.register(Post, PostAdmin)


class MediaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Media._meta.fields]


admin.site.register(Media, MediaAdmin)


class PeopleTagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PeopleTag._meta.fields]


admin.site.register(PeopleTag, PeopleTagAdmin)


class HashTagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in HashTag._meta.fields]


admin.site.register(HashTag, HashTagAdmin)
