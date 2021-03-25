from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
from django.db.models import CheckConstraint
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    username = models.CharField(max_length=100, default='', unique=True)
    password = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=254, null=True)
    phone = models.CharField(max_length=32, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    website = models.TextField(max_length=100, blank=True, null=True)
    profile_name = models.CharField(max_length=32, blank=True, null=True)
    gender = models.CharField(max_length=10, null=True)
    birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="profileImages", null=True)

    def __str__(self):
        return self.username

    # email and phone cannot be both null
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=(models.Q(phone__isnull=False) | models.Q(email__isnull=False)),
                name='not_both_null'
            )
        ]
    """
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    """


# related name is used to make two fks from one table
class Follow(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_id')
    following_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following_id')


class Post(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(max_length=500, blank=True, null=True)
    createdDate = models.DateField(auto_now_add=True)
    updatedDate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(max_length=500, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_id = models.IntegerField()


class Like(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)


class Tag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    tagged_id = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Location(models.Model):
    post = models.OneToOneField(
        Post, on_delete=models.CASCADE, primary_key=True,
    )
    place = models.TextField(max_length=100, blank=True)


class Photo(models.Model):
    image = models.ImageField(upload_to='upload_photos/% Y/% m/% d/')  # 어디로 업로드 할지 지정
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # 로그인 한 사용자, many to one relation
    pub_date = models.DateTimeField(auto_now_add=True)  # 레코드 생성시 현재 시간으로 자동 생성


class Video(models.Model):
    video = models.ImageField(upload_to='upload_videos/% Y/% m/% d/')  # 어디로 업로드 할지 지정
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # 로그인 한 사용자, many to one relation
    pub_date = models.DateTimeField(auto_now_add=True)  # 레코드 생성시 현재 시간으로 자동 생성
