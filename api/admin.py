from django.contrib import admin

from .models import Profile
from .models import Upload
from .models import Upload_file
from .models import Like
from .models import Comment

admin.site.register(Profile)
admin.site.register(Upload)
admin.site.register(Upload_file)
admin.site.register(Like)
admin.site.register(Comment)
