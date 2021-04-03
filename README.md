# CEOS 13기 백엔드 스터디
## REST API 서버 개발
### 인스타그램 클론

# 유의사항
* 본 레포지토리는 백엔드 스터디 2-3주차의 과제를 위한 레포입니다.
* 따라서 해당 레포를 fork 및 clone 후 local에서 본인의 깃헙 ID 브랜치로 작업한 후 커밋/푸시하고, PR 보낼 때도 `본인의 브랜치-> 본인의 브랜치`로 해야 합니다.

# 2주차 과제 (기한: 3/25 목요일까지)
### 모델 설명
사용자 : 게시글 = 1 : N<br>
게시글 : 사진,동영상 = 1 : N<br>
(좋아요) 사용자 : 게시글 = N : M<br>
(팔로우관계) 사용자 : 사용자 = N : M<br>
<br>
### ERD
![erd](https://user-images.githubusercontent.com/63651422/112450212-8112c080-8d97-11eb-867a-c34842a055c8.png)

### ORM 적용해보기
shell에서 작성한 코드와 그 결과를 보여주세요!<br><br>

User 객체 2개 생성
```python
python manage.py shell
>>> from api.models import *
>>> hy1 = User(nickname="hy1", email="hy@naver.com", phone_number="01011111111", password="1111", username="호영", description="나는호영1")
>>> hy1.save()
>>> hy2 = User(nickname="hy2", email="hy2@naver.com", phone_number="01022222222", password="2222", username="호영2", description="나는호영2")
>>> hy2.save()
>>> User.objects.all()
<QuerySet [<User: hy1>, <User: hy2>]>
```

Follow 객체 1개 생성
```python
>>> Follow.objects.create(following=hy1, followed=hy2)
<Follow: hy1 -> hy2>
```

Post 객체 1개 생성
```python
>>> p1 = Post(title="졸려", content="그냥잘까", author=hy1)
>>> p1.save()
>>> Post.objects.all()
<QuerySet [<Post: 졸려>]>
```

File 객체 2개 생성
```python
>>> File.objects.create(post=p1, file="프사.jpg")
<File: 졸려의 1번째 파일>
>>> File.objects.create(post=p1, file="프사sdf.jpg")
<File: 졸려의 2번째 파일>
>>> File.objects.all()
<QuerySet [<File: 졸려의 1번째 파일>, <File: 졸려의 2번째 파일>]>
```

Heart 객체 2개 생성
```python
>>> Heart.objects.create(post=p1, user=hy1)
<Heart: hy1 ♥ 졸려>
>>> Heart.objects.create(post=p1, user=hy2)
<Heart: hy2 ♥ 졸려>
>>> File.objects.all()
<QuerySet [<File: 졸려의 1번째 파일>, <File: 졸려의 2번째 파일>]>
```

Filter적용
```python
>>> User.objects.filter(nickname__contains='2')
<QuerySet [<User: hy2>]>
>>> Heart.objects.filter(user=hy1)
<QuerySet [<Heart: hy1 ♥ 졸려>]>
```

### 간단한 회고
과제 시 어려웠던 점이나 느낀 점, 좋았던 점 등을 간단히 적어주세요!<br>
->실제 프로젝트에서 ERD를 짤때 고민을 정말 많이해서 만들어야겠다는 생각을 했습니다.

<br>

## 3주차 과제 (기한: 4/1 목요일까지)
### 모델 선택 및 데이터 삽입
선택한 모델의 구조와 데이터 삽입 후의 결과화면을 보여주세요!
```python
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

#팔로잉 관계
class Follow(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="_following", verbose_name="팔로우하는 사람")
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="_followed", verbose_name="팔로우된 사람")

    def __str__(self):
        return self.following.nickname + ' -> ' + self.followed.nickname
```
![image](https://user-images.githubusercontent.com/63651422/113284715-fdbc1680-9324-11eb-9646-76c0755409ad.png)
![image](https://user-images.githubusercontent.com/63651422/113284922-4b388380-9325-11eb-87a8-01808cc7fea8.png)

### 모든 list를 가져오는 API
API 요청한 URL과 결과 데이터를 코드로 보여주세요!
```python
#config/urls.py
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
```
```python
#api/urls.py
from django.urls import path
from api import views

urlpatterns = [
    path('users', views.UserList.as_view()),
    path('posts', views.PostList.as_view()),
    path('files', views.FileList.as_view()),
    path('follows', views.FollowList.as_view()),
    path('hearts', views.HeartList.as_view()),
]
```
* User list 가져오기 (url 변경 전)
![image](https://user-images.githubusercontent.com/63651422/113285700-38727e80-9326-11eb-9d95-e859a947a2b7.png)

* Follow list 가져오기 (url 변경 전)
![image](https://user-images.githubusercontent.com/63651422/113285831-5e981e80-9326-11eb-8f69-3256e2f52d83.png)

### 새로운 데이터를 create하도록 요청하는 API
요청한 URL 및 Body 데이터의 내용과 create된 결과를 보여주세요!<br>

* User create (url 변경 전)
![image](https://user-images.githubusercontent.com/63651422/113286840-b1260a80-9327-11eb-90c5-ed1bb56fa6aa.png)

* Follow create (url 변경 전)
![image](https://user-images.githubusercontent.com/63651422/113287003-eaf71100-9327-11eb-9f48-5e10ea1566b9.png)

### 공부한 내용 정리
REST API에서 혼동을 주지 않기 위해 URI 경로의 마지막에는 슬래시(/)를 사용하지 않는다는 점을 알게 되었습니다. <br>그리고 related name을 지을 때 역참조를 생각해서 모델이름을 부여하는게 좋다는 점을 배웠습니다.

### 간단한 회고
처음에 FBV로 하다가, CBV로도 해보면서 이 부분에 대해 정확히 공부를 해야겠다고 생각했습니다. <br>빨리 프론트와 같이 협업하면서 REST API를 사용해보고 싶습니다.