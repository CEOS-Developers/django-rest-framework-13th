from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userid = models.CharField(max_length=10, verbose_name="아이디", unique=True)
    password = models.CharField(max_length=10)
    nickname = models.CharField(max_length=10, unique=True, default="")
    user_image = models.ImageField(blank=True)
    post_num = models.IntegerField(default=0)

    def __str__(self):
        return self.nickname

class Upload(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="uploads")
    description = models.TextField(blank=True)
    upload_date = models.DateField(auto_now=False, auto_now_add=True)
    like_num = models.IntegerField()
    comment_num = models.IntegerField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.description


class Upload_file(models.Model):
    upload = models.ForeignKey(Upload, on_delete=models.CASCADE, related_name="upload_files")
    # MEDIA_ROOT/uploads 에 저장
    file = models.FileField(upload_to="uploads/")

    def __str__(self):
        return self.upload + "번째 upload의 파일"

class Like(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="likes")
    upload = models.ForeignKey(Upload, on_delete=models.CASCADE, related_name="likes")
    like_date = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.profile + "유저의 " + self.upload + "번 게시글 좋아요"

class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="comments")
    upload = models.ForeignKey(Upload, on_delete=models.CASCADE, related_name="comments")
    comment_date = models.DateField(auto_now=True, auto_now_add=False)
    description = models.TextField()

    def __str__(self):
        return self.profile + "유저의 " + self.upload + "번 게시글 댓글"