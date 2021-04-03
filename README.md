# CEOS 13기 백엔드 스터디
## REST API 서버 개발
### 인스타그램 클론

## 유의사항
* 본 레포지토리는 백엔드 스터디 2-3주차의 과제를 위한 레포입니다.
* 따라서 해당 레포를 fork 및 clone 후 local에서 본인의 깃헙 ID 브랜치로 작업한 후 커밋/푸시하고, PR 보낼 때도 `본인의 브랜치-> 본인의 브랜치`로 해야 합니다. 

pip freeze > requirements.txt - 가상환경 라이브러리 -> requirements.txt에   
  pip install -r requirements.txt - requirements.txt에 있는 라이브러리들 가상환경에   
  https://docs.djangoproject.com/ko/3.0/intro/tutorial01/ - 장고 튜토리얼   
  https://gist.github.com/ihoneymon/652be052a0727ad59601#24-%EC%BD%94%EB%93%9C - 깃허브 마크다운
## 2주차 과제 (기한: 3/25 목요일까지)
https://brunch.co.kr/@ddangdol/4 - Field와 옵션에 대해 자세한 설명 참고
### 모델 설명
<img src="/image/new_modeling.PNG"></img>
#### Profile(AbstractUser)
userid - 가입하기 위한 아이디. 아이디는 중복이 불가(UNIQUE)  
userpw - 가입하기 위한 비밀번호 (admin에서 충돌을 피하기위해 password->userpw)  
nickname - 유저의 활동 닉네임. 닉네임은 중복이 불가(UNIQUE)   
user_image - 유저의 프사. 기본 이미지 가능(BLANK)  
created_date,update_date - DateInfo 상속  
~~post_num - 유저의 프로필 들어가면 게시글의 썸네일만 뜨게 하려고 만든 건데 생각해보니 필요없을거같아요.. 마이그레이션 할때 default를 설정하라는 오류가 떠서 DEFAULT=0으로 했어용~~  
#### Upload  
profile_id를 FK로 사용함 (1:N관계)  
description - 게시글의 본문. 가끔 갬성있게 올리고 싶을때 사진만 올리고 본문 안쓰는 경우를 대비(BLANK)  
thumbnail - 게시물의 썸네일.  
created_date,update_date - DateInfo 상속  
~~upload_date - 생성의 타임스탬프를 뜻하는 AUTO_NOW_ADD 옵션 사용. 굳이 수정 시간이 필요하나 싶었습니다~~  
~~like_num - 특정 게시글의 좋아요 수를 나타냄~~   
~~comment_num - 특정 게시글의 댓글 수를 나타냄~~  
#### Upload_file  
Upload_id를 FK로 사용함 (1:N관계)  
file - 업로드한 사진/영상 저장
#### Comment
profile_id와 upload_id를 FK로 사용함 ~~(둘다 1:N관계)~~ 각각 1:1,1:N 관계를 맺습니다.    
description - 댓글의 본문  
created_date,update_date - DateInfo 상속   
~~comment_date - 수정의 타임스탬프를 뜻하는 AUTO_NOW 옵션 사용(근데 upload_date랑 통일시킬 필요가 있어보입니다)~~
#### Like 
comment 모델과 같음
### DateInfo
메타 클래스 abstract=True를 이용해 테이블 생성x  
모든 model에 상속해 줍니다.  
created_date - auto_now_add=True   
update_date - auto_now=True
### ORM 적용해보기
```python
>>> from api.models import Profile,Upload
>>> profile1=Profile(user_id=1,userid="a",password="aa",nickname="aaa")
>>> profile1.save()
>>> Upload.objects.create(profile=profile1,description="hi",like_num=0,comment_num=0)
<Upload: hi>
>>> Upload.objects.create(profile=profile1,description="im",like_num=0,comment_num=0)
<Upload: im>
>>> Upload.objects.create(profile=profile1,description="junki",like_num=0,comment_num=0)
<Upload: junki>
>>> Upload.objects.all()
<QuerySet [<Upload: hi>, <Upload: im>, <Upload: junki>]>
>>> Upload.objects.filter(id=2)
<QuerySet [<Upload: im>]>
>>> Upload.objects.filter(like_num=0)
<QuerySet [<Upload: hi>, <Upload: im>, <Upload: junki>]>
```

### 간단한 회고
과제 시 어려웠던 점이나 느낀 점, 좋았던 점 등을 간단히 적어주세요!  

직접 model을 짜보니 더 깊이 공부하게 되서 좋았습니다. 저번 과제때 했던것들도 이번 과제때 다시 써보니 헷갈린 부분도 많았어서
꾸준히 공부해야 겠더라구요.. 앞으로 저희가 짠 모델로 무엇을 할지 기대가 됩니당 !   
Q. 제가 마이그레이션을 모델이 바뀔때마다 자주 해서 마이그레이션 파일이 여러개가 생겼는데 
보니까 다 상관관계가 있는거 같더라구요 이 파일들은 다함께 보관해야 할까요? 그리고 .gitignore?   
A. .gitignore는 로컬, 서버에서 할건지에 따라 다름. 마이그레이션 파일은 최대한 수정해보기.   
변수 이름은 알아서 많이 해봐라 ^-^
## 3주차 과제 (기한: 4/1 목요일까지)
### 모델 선택 및 데이터 삽입
선택한 모델의 구조와 데이터 삽입 후의 결과화면을 보여주세요!
```python
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
```
<img src="/image/upload_model.PNG"></img>
### 모든 list를 가져오는 API
API 요청한 URL과 결과 데이터를 코드로 보여주세요!   
<img src="/image/upload_GET.PNG"></img>
### 새로운 데이터를 create하도록 요청하는 API
요청한 URL 및 Body 데이터의 내용과 create된 결과를 보여주세요!  
<img src="/image/upload_POST.PNG"></img>
### 공부한 내용 정리
  
RESTful한 api를 만들기 위해 DRF(Django Rest Framework)를 설치하고, Serializer를 이용해 json 형식으로 소통해보았습니다. 또한 postman을 사용하여 HTTP 요청을 처리해보았습니다.  
지난 주 받은 피드백을 반영하여 모델링을 수정하는 과정에서, 많은 충돌이 있었습니다.  
* User모델이 아닌 AbstractUser를 상속한 Profile모델에서 superuser가 생성    
* Profile모델의 password(max_length=10) 필드가 superuser의 password와 겹쳐 충돌??이 났습니다. password를 해쉬하는 과정에서 password의 최대길이가
10이기 때문에 짤려서 저장되어 계속 로그인이 안됨 그래서 필드이름 바꿈 password->userpw

### 간단한 회고 
마이그레이션 수정이 너무 어려워서 처음에 모델링을 잘 해야할 것 같습니다... 다들 이번 주도 화이팅해봐요...👊👊