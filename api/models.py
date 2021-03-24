from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


# User 모델
# AbstractUser :
# id / password / last_login / is_superuser /
# username / first_name / last_name / email / is_staff / is_active / date_joined
# AbstractBaseUser : id / password / last_login
class User(AbstractBaseUser):
    username= models.CharField(max_length=255)
    USERNAME_FIELD = 'username'
    insta_id = models.CharField(max_length=255, unique=True, )
    is_professional = models.BooleanField(default=False)


# Profile
class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    # CASCADE : ForeignKeyField가 바라보는 값이 삭제될 때 ForeignKeyField를 포함하는 모델 인스턴스(row)도 삭제된다.
    profile_pic = models.TextField()
    profile_name = models.TextField()
    profile_website = models.TextField()
    profile_info = models.TextField()


# 인스타 게시
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    location = models.TextField()
    upload_at = models.DateTimeField(auto_now=True)
    is_good = models.BooleanField()
    is_comment = models.BooleanField()
    goods = models.PositiveIntegerField()

    def publish(self):
        self.upload_at = timezone.now()
        self.save()

    def __str__(self):
        return self.content


# 인스타 이미지
class Images(models.Model):
    post = models.ForeignKey(Post, blank=False, null=False, on_delete=models.CASCADE)
    content = models.TextField()


# 인스타 댓글
class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    upload_at = models.DateTimeField(auto_now=True)


# 인스타 대댓글
class PostCommentReply(models.Model):
    postcomment = models.ForeignKey(PostComment, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    upload_at = models.DateTimeField(auto_now=True)


# 인스타 스토리 게시
class StoryPost(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    pic = models.TextField()
    upload_at = models.DateTimeField(auto_now=True)

    def publish(self):
        self.upload_at = timezone.now()
        self.save()

    def __str__(self):
        return self.content

