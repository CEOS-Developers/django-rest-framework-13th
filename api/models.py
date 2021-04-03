from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class DateInfo(models.Model):
    created_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Profile(AbstractUser, DateInfo):
    userid = models.CharField(max_length=10, verbose_name="아이디", unique=True)
    # superuser에서 충돌이 나 이름변경 password->userpw
    userpw = models.CharField(max_length=10)
    nickname = models.CharField(max_length=10, unique=True, default="")
    user_image = models.ImageField(blank=True)

    def __str__(self):
        return self.nickname

class Upload(DateInfo):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="uploads")
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(null=True)

    def __str__(self):
        return self.description


class Upload_file(DateInfo):
    upload = models.ForeignKey(Upload, on_delete=models.CASCADE, related_name="upload_files")
    # MEDIA_ROOT/uploads 에 저장
    file = models.FileField(upload_to="uploads/")

    def __str__(self):
        return self.upload + "번째 upload의 파일"

class Like(DateInfo):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    upload = models.ForeignKey(Upload, on_delete=models.CASCADE, related_name="likes")

    def __str__(self):
        return self.profile + "유저의 " + self.upload + "번 게시글 좋아요"

class Comment(DateInfo):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="comments")
    upload = models.ForeignKey(Upload, on_delete=models.CASCADE, related_name="comments")
    description = models.TextField()

    def __str__(self):
        return self.profile + "유저의 " + self.upload + "번 게시글 댓글"