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

