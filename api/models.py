from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):  # 사용자 모델

    gender_choices = ("male", "female", "custom", "None")  # Profile.gender의 선택 사항을 저장항 튜플

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # User 모델에서 OneToOne 확장
    name = models.CharField(max_length=None)  # 사용자의 이름, 중복가능, 글자수 제한 없음
    nickname = models.CharField(max_length=30, blank=False, unique=True)  # 사용자의 닉네임, 글자수 제한 30, 필수입력, 중복 불가능
    intro = models.CharField(max_length=2200)  # 사용자의 자기소개, 글자수 제한 2200
    profile_image = models.ImageField(upload_to='profile_images/', blank=True,
                                      null=True)  # 사용자의 프로필사진, /media/profile_images/에 저장되고 미입력 가능
    website = models.URLField(blank=True, null=True)  # 사용자의 웹사이트 url , 중복 가능
    email = models.EmailField(blank=True, null=True)  # 사용자의 이메일 주소 , 중복 가능
    phone = models.CharField(blank=False, unique=True)  # 사용자의 전화번호 , 필수입력, 중복 불가능
    birthday = models.DateField(blank=True, null=True)  # 사용자의 생일
    gender = models.CharField(choices=gender_choices, max_length=None, blank=False)  # 사용자의 성별, 필수 선택


class Post(models.Model):  # 포스트 모델

    ratio_choices = ("original", "square")

    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)  # Profile 모델과 1:N 관계
    pub_date = models.DateTimeField('published date', auto_now_add=True)  # 포스팅 시 생성 날짜 저장
    content = models.CharField(max_length=2200)  # 게시글의 내용, 글자수 제한 2200
    location = models.CharField(max_length=None)  # 게시글에 추가할 수 있는 위치정보
    ratio = models.CharField(choices=ratio_choices, max_length=None, blank=False)  # 게시되는 이미지/비디오의 비율, 필수 선택
    comment_permission = models.CharField(choices=('Yes', 'No'), max_length=None,
                                          blank=False)  # 게시물에 댓글 기능 사용 여부, 필수 선택


class Media(models.Model):  # 미디어 모델 (포스트에 들어가는 사진/동영상)

    post = models.ForeignKey('Post', on_delete=models.CASCADE)  # Post 모델과 1:N 관계
    upload = models.FileField(upload_to='posts', blank=False, unique=True)  # 업로드된 사진 및 동영상, 필수 입력, 중복 불가능
    subs_text = models.CharField('substitutional text', max_length=2200)  # 사진/영상 별 대체 텍스트 입력, 글자수 제한 2200


class PeopleTag(models.Model):  # 피플태그 모델 (각각의 사진/동영상에 추가되는 이용자 태그)
    media = models.ForeignKey('Media', on_delete=models.CASCADE)  # Media 모델과 1:N 관계
    tagged_user = models.CharField(max_length=30, null=True)  # 태그 된 사용자의 Profile.nickname 을 받음
