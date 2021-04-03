from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, nickname, password=None):
        if not nickname:
            raise ValueError('must have user nickname')
        user = self.model(
            nickname=nickname
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        user = self.create_user(
            nickname=nickname,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    # User 모델


class User(AbstractBaseUser):
    objects = UserManager()

    CHOICE_GENDER = (
        ('man', '남성'),
        ('woman', '여성')
    )
    username = models.CharField(max_length=255, null=False, unique=True)
    insta_id = models.CharField(max_length=255, unique=True, )
    is_professional = models.BooleanField(default=False)
    gender = models.CharField(max_length=5, choices=CHOICE_GENDER)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username']

# Profile
class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    # CASCADE : ForeignKeyField가 바라보는 값이 삭제될 때 ForeignKeyField를 포함하는 모델 인스턴스(row)도 삭제된다.
    profile_pic = models.TextField(blank=True)
    profile_name = models.TextField()
    profile_website = models.TextField(blank=True)
    profile_info = models.TextField(blank=True)


# 인스타 게시
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    location = models.TextField(blank=True)
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
    index = models.PositiveIntegerField()
    content = models.TextField()


# 인스타 댓글
class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    upload_at = models.DateTimeField(auto_now=True)
    goods = models.PositiveIntegerField()

    def __str__(self):
        return '{}:{}'.format(self.author, self.content)


# 인스타 대댓글
class PostCommentReply(models.Model):
    comment = models.ForeignKey(PostComment, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    upload_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}:{}'.format(self.author, self.content)


# 인스타 스토리 게시
class StoryPost(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    pic = models.TextField()
    upload_at = models.DateTimeField(auto_now=True)

    def publish(self):
        self.upload_at = timezone.now()
        self.save()

    def __str__(self):
        return self.pic
