# CEOS 13기 백엔드 스터디
<hr>

## REST API 서버 개발 - 인스타그램 클론

<hr>

## 2주차 과제

## 인스타그램 서비스 분석
인스타그램은 사진 공유를 기반으로 하는 SNS 서비스입니다.  
사용자가 회원가입을 하면 프로필 사진과 소개를 등록하고, 다른 사람들과 팔로우/팔로잉 관계를 맺을 수 있습니다.  
또한, 사진 혹은 동영상을 글과 함께 개인 페이지에 포스팅하고 다른 이용자들과 '좋아요' 기능과 댓글을 이용하여 소통합니다.  
이 외에도, 인스트그램 내 메신저인 DM 기능과 검색 기능, 실시간으로 24시간 동안 게시글을 올리는  스토리 기능 등이 있습니다.  

이번 과제가 유저와 포스팅의 모델링에 중점을 두기에 이 두가지에 집중해보겠습니다.  
>###User
> * 이용자는 아이디와 비밀번호를 설정하여 회원가입을 진행합니다.
> * 이용자는 다음 정보를 프로필로 등록합니다
>   * 이름
>   * 사용자 이름 (중복 불가, 필수 입력)
>   * 웹사이트
>   * 소개
>   * 프로필 사진
> * 이용자는 다음 정보를 개인 정보로 등록할 수 있습니다.
>   * 이메일 주소
>   * 전화번호 (필수 입력)
>   * 성별(여성/남성/맞춤성별/밝히고싶지않음 : 필수선택)
>   * 생일
> * 이 외 기능 (게시물, 팔로우/팔로잉, DM 등) 은 전부 모델 매핑 형식이 더 효율적일 것이라 생각하여 다루지 않겠습니다.
>###Post
> * 게시물은 최근 순으로 앞에 배치됩니다.
> * 게시물에는 사진과 동영상이 최대 10개까지 등록됩니다.
> * 게시되는 사진의 비율(정사각형,원본)을 일괄 변경하거나 필터를 추가할 수 있습니다.
> * 게시물에는 텍스트로 된 내용이 들어가며 최대 2200자까지 입력됩니다.
> * 사진 당 최대 20명의 사람을 태그할 수 있습니다.
> * 게시물에 최대 30개의 해시태그를 설정할 수 있습니다.
> * 위치정보를 추가할 수 있습니다.
> * 다른 미디어 (Facebook, Twitter, Tumblr)에도 게시할 수 있습니다.
> * 댓글을 작성할 수 있으며 댓글 기능을 해제할 수 잇습니다.
> * 각 사진 및 영상마다 대체 텍스트를 입력할 수 있습니다.

## 모델링
>![instagram_modeling](https://user-images.githubusercontent.com/78783840/113481861-ed4b9d80-94d6-11eb-9bbb-2b6fd4daf498.png)
> * User와 Profile을 OneToOne 확장하였습니다.
> * 사용자인 Profile이 올리는 게시글을 Post라는 모델로 1:N 연결하였습니다.
> * Post라는 게시글에 업로드 되는 사진과 영상을 Media 라는 모델로, 해시태그를 HashTag 라는 모델로  
>   1:N 연결하였습니다.
> * 사진과 영상인 Media의 각 instance에 PeopleTag를 달 수 있게 PeopleTag라는 모델과 1:N 연결하였습니다.
>
<hr>

## 모델링 결과
> 사용한 모델 : POST
> 
>![p(1)](https://user-images.githubusercontent.com/78783840/113481875-fdfc1380-94d6-11eb-9d5b-290c57ecb8cd.png)
>![p(2)](https://user-images.githubusercontent.com/78783840/113481889-0c4a2f80-94d7-11eb-9ec1-90bd2c60cd12.png)
>![p(3)](https://user-images.githubusercontent.com/78783840/113481899-1a984b80-94d7-11eb-9eea-f3ad053b4497.png)
>![p(4)](https://user-images.githubusercontent.com/78783840/113481900-1a984b80-94d7-11eb-8416-8b3d8b3ffe5d.png)
> POST 객체 3개 저장 : post1, post2, post3
>  
> 
>![p(5)](https://user-images.githubusercontent.com/78783840/113481901-1b30e200-94d7-11eb-9366-b2541016c29c.png)
> Queryset 조회
> 
>![p(6)](https://user-images.githubusercontent.com/78783840/113481902-1b30e200-94d7-11eb-8e27-205e5535c2ba.png)
> location 을 필터로 조회
> 
>![p(7)](https://user-images.githubusercontent.com/78783840/113481898-19ffb500-94d7-11eb-8ebf-a0a73df7bf90.png)
> comment_permission을 필터로 조회

##배운 점
> *  filter 함수는 반환값이 리스트 형태인 QuerySet이므로 1개의 데이터만 조회하고 싶다면 get 함수를 쓰는 것이 좋다.
> * CharField와 TextField 같은 문자 기반의 필드들에서 null 사용을 피하는 것이 좋다.  
    null= True인 경우에 "no data"의 값이 NULL과 빈 문자열 두 가지가 가능하게 된다.  
    그러나 Django의 규칙은 NULL 대신  빈 문자를 사용하는 것이라 NULL은 불필요하다.
  
<hr>

## 3주차 과제 (기한: 4/1 목요일까지)
### 모델 선택 및 데이터 삽입

>**선택한 모델 : Post**
> 
>![0153](https://user-images.githubusercontent.com/78783840/113311601-72eb1400-9344-11eb-9c8b-ce9955d17526.png)
>
>**데이터 삽입**
>![0154](https://user-images.githubusercontent.com/78783840/113316100-f1e24b80-9348-11eb-9a2e-242c00cb0c89.png) 

### 모든 list를 가져오는 API
>![0155](https://user-images.githubusercontent.com/78783840/113316333-2ce47f00-9349-11eb-9419-13ff81b867e5.png)

### 새로운 데이터를 create하도록 요청하는 API
>![0171](https://user-images.githubusercontent.com/78783840/113481999-92667600-94d7-11eb-993f-582532e7ab7b.png)
>![0172](https://user-images.githubusercontent.com/78783840/113481977-782c9800-94d7-11eb-87ea-ada781543a79.png)
>IntegrityError: (1048, "Column connot be null") 오류 해결 중입니다...

### 공부한 내용 정리
* JSON이 무엇이고 Seiraliziation이 왜 필요하며 어떤 방식으로 진행되는 지 알 수 있었습니다.
* Nested Serializer 를 사용하는 데 read_only 와 write_only를 어떤 상황에서 사용하는 지 알아볼 것.
* 한 Model을 Post할 때 nest 된 모델의 field를 같이 입력하는 게 맞는 방향인 지 궁금합니다. 
  저는 Media의 FK로 Post를 잡았는데, Post의 인스턴스를 create 할 때 하위 모델의 instance를 
  모두 입력해야 하는 게 맞는 상황인 지 궁금했습니다.
* fields= \_\_all__ 과 같이 모든 필드를 갖고 오는 명령문을 쓸 때 조심해야 하는 걸 배웠습니다.      

### 간단한 회고
다양한 에러를 맛 보게 되어 슬펐지만 그만큼 많이 배운 것 같아서 좋았습니다.  
전 주차에서 직접 만든 모델을 활용하는 과제이다 보니 뭔가 만들어져가는 느낌이 들어 재밌었습니다.  
부족한 부분을 많이 느껴 앞으로 열심히 공부해야겠다고 느꼈습니다.

<hr>

## 4주차 과제 (기한: 4/8 목요일까지)  
<br>

### 모든 list를 가져오는 API
API 요청한 URL과 결과 데이터를 코드로 보여주세요!

```json
요청 URL: /api/posts

[
    {
        "profile": 1,
        "id": 1,
        "pub_date": "2021-03-27T11:45:55.080266+09:00",
        "content": "This is 1st post",
        "location": "Seoul",
        "ratio": "origin",
        "comment_permission": "y",
        "medias": [],
        "hashtags": []
    },
    {
        "profile": 1,
        "id": 2,
        "pub_date": "2021-03-27T11:47:49.606663+09:00",
        "content": "This is 2nd post",
        "location": "Busan",
        "ratio": "square",
        "comment_permission": "n",
        "medias": [],
        "hashtags": []
    },
    {
        "profile": 1,
        "id": 3,
        "pub_date": "2021-03-27T11:48:50.818669+09:00",
        "content": "This is 3rd post",
        "location": "Ilsan",
        "ratio": "origin",
        "comment_permission": "y",
        "medias": [],
        "hashtags": []
    },
    {
        "profile": 1,
        "id": 4,
        "pub_date": "2021-04-07T15:16:42.951309+09:00",
        "content": "This is 4th post~~~",
        "location": "Gimpo",
        "ratio": "origin",
        "comment_permission": "y",
        "medias": [],
        "hashtags": []
    }
]
```
<br>
<br>

### 특정 데이터를 가져오는 API
API 요청한 URL과 결과 데이터를 코드로 보여주세요!

```json
요청 URL: /api/posts/1

{
    "profile": 1,
    "id": 1,
    "pub_date": "2021-03-27T11:45:55.080266+09:00",
    "content": "This is 1st post",
    "location": "Seoul",
    "ratio": "origin",
    "comment_permission": "y",
    "medias": [],
    "hashtags": []
}
```
<br>
<br>

### 새로운 데이터를 생성하는 API
요청 URL 및 body 데이터의 내용과 create된 결과를 보여주세요!

```json
요청 URL: /api/posts

{
        "profile": 2,
        "content": "This is 5th post",
        "location": "풍무동",
        "ratio": "origin",
        "comment_permission": "y",
        "medias": [],
        "hashtags": []
    }
```
![0173](https://user-images.githubusercontent.com/78783840/113996067-c653e980-9891-11eb-8d28-04a890eb83dd.png)

<br>
<br>

### 특정 데이터를 업데이트하는 API
요청 URL 및 body 데이터의 내용과 update된 결과를 보여주세요!
```json
요청 URL: /api/posts/6

*기존 데이터
{
    "profile": 2,
    "id": 6,
    "pub_date": "2021-04-08T17:41:43.055577+09:00",
    "content": "This is 5th post",
    "location": "풍무동",
    "ratio": "origin",
    "comment_permission": "y",
    "medias": [],
    "hashtags": []
}

*수정된 데이터
{
    "profile": 2,
    "id": 6,
    "pub_date": "2021-04-08T17:41:43.055577+09:00",
    "content": "This is updated 5th post",
    "location": "이태원",
    "ratio": "origin",
    "comment_permission": "n",
    "medias": [],
    "hashtags": []
}
```
![0174](https://user-images.githubusercontent.com/78783840/113997431-18e1d580-9893-11eb-900d-7369bee331a4.png)

<br>
<br>

### 특정 데이터를 삭제하는 API
요청 URL 및 delete된 결과를 보여주세요!  

![0175](https://user-images.githubusercontent.com/78783840/113997574-40d13900-9893-11eb-9e9c-8d952bf1a113.png)

<br>
<br>

### 공부한 내용 정리
새로 알게된 점, 정리 하고 싶은 개념, 궁금한점 등을 정리해 주세요  

* >###HTTP REQUEST  (출처: https://blog.naver.com/lightsalt28/221591010783)
  >GET : 요청받은 URL의 정보 검색 > 응답  
  >POST : 요청된 자원 생성(Create)  
  >PUT : 요청된 자원 수정(Update)  
  >DELETE : 요청된 자원 삭제(Delete)  
  >PATCH : 요청된 자원 일부 교체(수정)  
  >OPTION : 웹서버에서 지원되는 메소드 종류 확인  
  > (* HEAD 는 장고 base view에서 dispatch가 get()으로 보낸다.싫으면 head() 오버라이딩 : 무슨 말인지 다시 공부할 것)

* >API view는 장고 base view의 하위 클래스이며, 차이점이 있다.
  > * Request는 Django의 HttpRequest 인스턴스가 아닌 REST 프레임워크의 request 인스턴스가 됨
  > * Django의 HttpResponse가 아닌 REST 프레임워크의 Response를 반환
  > * APIException 예외케이스가 발견되면 적절한 response으로 조정됨
  > * Incoming request를 authenticate하고, 적절한 권한 혹은 throttle(제한사항)을 체크한 후 실행함 (?)  
  >  
  >출처: https://velog.io/@phyyou/DRF-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0-3-CBV-APIView

* method 명이 해당 request 의 소문자형으로 정의해야 dispatch 가 request 를 배정할 수 있음  
   

* APIView > Mixin > generics.APIView > ViewSet 순으로 상속을 받아가며 간소화된다. (ViewSet은 CBV가 아닌 헬퍼클래스라고 한다.)   
이 부분은 아직 공부를 많이 못하기도 했고, 각 view마다 종류와 쓰임새도 많아서 꼭 배워놔야 할 것 같다.  
  (참고하면 좋은 : https://ssungkang.tistory.com/entry/Django-APIView-Mixins-generics-APIView-ViewSet%EC%9D%84-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90?category=366160)
  
      
<br>
<br>

### 간단한 회고
과제 시 어려웠던 점이나 느낀 점, 좋았던 점 등을 간단히 적어주세요!

```
처음에 작성했던 모델에 데이터를 만져보는 과정을 해보니 진짜 신기했다.  
로컬 네트워크와 기본 어드민 템플릿에서만 데이터가 도는 게 아닌 실제 서비스에서는 어떤 과정으로 진행될 지 궁금했다.
그리고 CBV의 종류가 정말 많고, 장고에 내장된 것과 RF에 내장된 게 각기 달라 나중에 더 깊게 개발하게 되면 이런 부분도 신경써야 할 것 같다.  
늘 그렇지만 과제를 하면 할 수록 장고에 능숙해지려면 배워야하는 게 정말 많음을 느꼈다.
```
<br>
<br>

<hr>

## 5주차 과제 (기한: 5/13 목요일까지)  
<br>

### 1. Viewset으로 리팩토링하기

```python
[views.py]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = PostFilter

[urls.py]

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = router.urls
```
![image](https://user-images.githubusercontent.com/78783840/118245066-4564bf00-b4db-11eb-9caa-8e2cccf74f5d.png)

<br>
<br>

### 2. filter 기능 구현하기

```python
class PostFilter(FilterSet):
    pub_date__gt = filters.DateFilter(field_name='pub_date', lookup_expr='gt') # 입력된 날짜 이후에 게시된 Post 필터링
    pub_date__lt = filters.DateFilter(field_name='pub_date', lookup_expr='lt') #입력된 날짜 이전에 게시된 Post 필터링
    pub_date__range = filters.DateFromToRangeFilter(field_name='pub_date', lookup_expr='range') #입력된 기간 내 게시된 Post 필터링
    content__icontains = filters.CharFilter(field_name='content', lookup_expr='icontains') #입력된 값을 content field value에 갖고 있는 Post 필터링


    class Meta:
        model = Post
        fields = ['profile', 'pub_date', 'content', 'location'] # 해당 Field에 대해 lookup_expr = 'exact' 필터링

```
![image](https://user-images.githubusercontent.com/78783840/118245178-6f1de600-b4db-11eb-9ebc-5d66c157450d.png)
![image](https://user-images.githubusercontent.com/78783840/118245247-88269700-b4db-11eb-9834-cabdcca95d6e.png)

* method를 이용한 필터링 부분이 잘 구현되지 않아서 더 공부하고 꼭 추가하려합니다.
<br>
<br>

### (선택) permission 기능 구현하기
시간 관리를 못해서 못했는데, 나중에라도 꼭 채워 놓을 예정입니다!
### (선택) validation 적용하기
시간 관리를 못해서 못했는데, 나중에라도 꼭 채워 놓을 예정입니다!

<br>

### 공부한 내용 정리
새로 알게된 점, 정리 하고 싶은 개념, 궁금한점 등을 정리해 주세요  

* >###Router
  >* Router:   
     Request를 약속된 논리에 따라 URL을 자동적으로 결정하고 매핑하며, viewset의 기본적인 action을 실행함 
  >* router.register:  
     URL접두어인 prefix와 viewset을 필수 인자로 받음  
  >* basename:  
   viewset의 attribute로 URLname을 결정함. 설정되지 않으면 viewset의 queryset attribute를 기반으로 자동으로 결정됨  
  > * DefaultRouter : https://www.django-rest-framework.org/api-guide/routers/#defaultrouter  
  > * 참고:  
  >   * https://www.django-rest-framework.org/api-guide/routers/#routers  
  >   * https://kimdoky.github.io/django/2018/07/08/drf-Routers/
  

* >###FilterSet
  >* filter:   
     queryset을 필터링하며, 'field_name'과 'lookup_expr'을 인자로 받음
  >* Field lookups:   
     QuerySet method인 filter(), exclude(), get()의 인자로 사용되며 특정 instances를 호출하기 위한 조건?이 된다.
  > * method:  
   filter의 optional argument로 직접 정의한 메써드로 필터링
  >* types:  
     field의 종류에 따라 그에 맞는 filter를 사용해야 함(ex. CharFilter, BooleanFilter 등)
  >* FilterSet의 Meta에 지정된 fields 들은 기본적으로 lookup_expr = 'exact'  
  >* FK관계에 있는 모델의 필드를 쓰려면 __을 사용한다.
  >* 참고:  
  >   * Field lookups: https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups  
  >   * https://kimdoky.github.io/django/2018/07/08/drf-Routers/

      
<br>
<br>

### 간단한 회고
과제 시 어려웠던 점이나 느낀 점, 좋았던 점 등을 간단히 적어주세요!


이번 주차 과제가 장고에서 정말 중요한 내용을 다룬다는 생각이 들었다.
그래서인지 3,4번 과제인 permission과 validation을 못해서 너무 아쉬웠고 꼭 해봐야겠다.
method를 이용해 최근 12시간 내 등록된 post가 나오는 filerting을 구현하고 싶었는데 애를 많이 먹고 실패했다.  
혹시 일요일 스터디까지 내가 해결을 못하면 CustomLookup을 만들어야 하는 것인 지 여쭙고 싶어용.
