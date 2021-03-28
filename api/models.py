from django.db import models

#사용자
class User(models.Model):
    # 닉네임, 이메일, 전화번호로 로그인하기 때문에 Unique해야
    nickname = models.CharField(max_length=100, verbose_name="닉네임", unique=True)
    email = models.EmailField(max_length=255, verbose_name="이메일", unique=True)
    phone_number = models.CharField(max_length=100, verbose_name="전화번호", unique=True)

    password = models.CharField(max_length=150, verbose_name="비밀번호", unique=True)
    username = models.CharField(max_length=150, verbose_name="이름", unique=True)
    description = models.TextField(verbose_name="소개")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="가입일자")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트일자")

    def __str__(self):
        return self.nickname #표시할때 닉네임으로

#게시글
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="소개")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자", related_name="_author")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="업로드일자")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트일자")

    def __str__(self):
        return self.title #표시할때 제목으로

#Post와 연결된 사진이나 비디오
class File(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="연결된 게시글", related_name="file_post") #연결된 Post
    # 저장경로 : MEDIA_ROOT/post/ 경로에 저장
    file = models.FileField(blank=True, upload_to="post/", verbose_name="사진or동영상") #사진이나 동영상

    def __str__(self):
        return self.post.title + '의 ' + str(self.pk) +'번째 파일'

#팔로잉 관계
class Follow(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="_following", verbose_name="팔로우하는 사람")
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="_followed", verbose_name="팔로우된 사람")

    def __str__(self):
        return self.following.nickname + ' -> ' + self.followed.nickname

#좋아요
class Heart(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="heart_post", verbose_name="좋아요단 게시글") #연결된 Post
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="_user", verbose_name="좋아요단 사용자") #좋아요 누른 사용자

    def __str__(self):
        return self.user.nickname + ' ♥ ' + self.post.title