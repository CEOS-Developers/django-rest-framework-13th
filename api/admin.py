from django.contrib import admin
from .models import Profile, Post, Media, PeopleTag, HashTag

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Media)
admin.site.register(PeopleTag)
admin.site.register(HashTag)
