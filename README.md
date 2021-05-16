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
profile_id와 upload_id를 FK로 사용함 (둘다 1:N관계)    
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
## 4주차 과제 (기한: 4/8 목요일까지)
### 모든 list를 가져오는 API

- Method : GET   
- URL : /api/uploads/
#### *수정하다보니 id가 뒤죽박죽 임미다
```python
[
    {
        "id": 1,
        "comments": [
            {
                "id": 4,
                "description": "junki hi 댓"
            },
            {
                "id": 5,
                "description": "junki hi 댓2"
            }
        ],
        "created_date": "2021-04-01",
        "update_date": "2021-04-01",
        "description": "hi",
        "thumbnail": null,
        "profile": 2
    },
    {
        "id": 2,
        "comments": [
            {
                "id": 6,
                "description": "junki immm 댓"
            }
        ],
        "created_date": "2021-04-01",
        "update_date": "2021-04-08",
        "description": "i am",
        "thumbnail": null,
        "profile": 2
    },
    {
        "id": 3,
        "comments": [],
        "created_date": "2021-04-01",
        "update_date": "2021-04-01",
        "description": "junki",
        "thumbnail": null,
        "profile": 2
    },
    {
        "id": 8,
        "comments": [
            {
                "id": 7,
                "description": "dokiman 댓"
            }
        ],
        "created_date": "2021-04-08",
        "update_date": "2021-04-08",
        "description": "dokiman",
        "thumbnail": null,
        "profile": 7
    }
]
```

### 특정 데이터를 가져오는 API
- Method : GET   
- URL : /api/users/2/uploads/
```python
[
    {
        "id": 1,
        "comments": [
            {
                "id": 4,
                "description": "junki hi 댓"
            },
            {
                "id": 5,
                "description": "junki hi 댓2"
            }
        ],
        "created_date": "2021-04-01",
        "update_date": "2021-04-01",
        "description": "hi",
        "thumbnail": null,
        "profile": 2
    },
    {
        "id": 2,
        "comments": [
            {
                "id": 6,
                "description": "junki immm 댓"
            }
        ],
        "created_date": "2021-04-01",
        "update_date": "2021-04-08",
        "description": "i am",
        "thumbnail": null,
        "profile": 2
    },
    {
        "id": 3,
        "comments": [],
        "created_date": "2021-04-01",
        "update_date": "2021-04-01",
        "description": "junki",
        "thumbnail": null,
        "profile": 2
    }
]
```
### 새로운 데이터를 생성하는 API
- Method : POST   
- URL : /api/users/7/uploads/  
- Body : { "description" : "dokiman", "profile" : 7 }
```python
{
    "id": 8,
    "created_date": "2021-04-08",
    "update_date": "2021-04-08",
    "description": "dokiman",
    "thumbnail": null,
    "profile": 7
}
```
### 특정 데이터를 업데이트하는 API
- Method : PUT   
- URL : /api/uploads/2    
- Body : { "profile" : 2, "description" : "i am" }
```python
# 2번 Profile, 2번 Upload
{
    "id": 2,
    "created_date": "2021-04-01",
    "update_date": "2021-04-08",
    "description": "i am",
    "thumbnail": null,
    "profile": 2
}
```
### 특정 데이터를 삭제하는 API
- Method : DELETE   
- URL : /api/uploads/2
```python
Status: 204 No Content
```

### 공부한 내용 정리 
FBV - 읽기가 쉽고 클래스 기반 뷰보다 직관적이지만 확장과 재사용성이 떨어짐   
CBV - 코드를 확장하거나 재사용하기 쉽지만 읽기 어렵다.   
Image파일 관련 좀 더 공부해야함!
### 간단한 회고 
API URL을 어떻게 설정해야 깔끔할지 잘 모르겠다,,,   
과제를 하면서 ORM, serializer가 헷갈리는 부분이 있어서 복습이 필요할 것 같다.

## 6주차 과제 (기한: 5/13 목요일까지)

### 1. Viewset으로 리팩토링하기

```python
class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    
class UploadViewSet(viewsets.ModelViewSet):
    serializer_class = UploadSerializer
    queryset = Upload.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filterset_class = UploadFilter
    permission_classes = (IsAuthorPostorUpdate,)
```

### 2. filter 기능 구현하기

```python
class UploadFilter(FilterSet):
    description = filters.CharFilter(field_name="description", lookup_expr="icontains")
    is_profile = filters.BooleanFilter(method='filter_is_profile')
    profile = filters.NumberFilter(field_name="profile")

    class Meta:
        model = Upload
        fields = ['id','description','profile']

    def filter_is_profile(self, queryset, name, value):
        filtered_queryset = queryset.filter(profile=2)
        return filtered_queryset
```

### 3. (선택) permission 기능 구현하기
```python
class IsAuthorPostorUpdate(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        if request.method != 'GET':
            return obj.profile == request.user
```
### 4. (선택) validation 적용하기

- 자유롭게 validation 을 만들어 적용해보세요
- (권장) validator 만들어서 적용해보기
```python
class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = '__all__'
    def validate(self, data):
        if 'Test' not in data['description']:
            raise ValidationError('Validation Error!')
        return data
```

### 5. 배운점
+ DRF의 CBV - 하나의 url에 하나의 view 처리  
+ Generic Views - 하나의 url에 여러 개의 view 처리   
+ Viewsets - 여러 개의 url 패턴에 대해 여러 개의 view 처리  
#### Filter 옵션 lookup_expr 키워드 참고 https://brownbears.tistory.com/63 
ex) description = filters.CharFilter(field_name="description", lookup_expr="icontains")
+ has_permission에서 먼저 권한 확인 후 has_object_permission(개별 record) 확인 
#### serialize.py에서 Validation
+ def field_validator(self, value), def object_validator(self, data)  
#### model.py에서 Validation  
+ def validators(value) 
+ score = IntegerField(validators=[validators])
### 6. 간단한 회고
오랜만에 장고를 다시 쓰니까 많이 헷갈려서 과제하는데 시간이 꽤 걸린 것   
같습니다... 앞으로 팀 프로젝트 구현을 대비해 장고의 백엔드 전체적인 흐름을 인지하며
공부하면 좋을 것 같습니다.