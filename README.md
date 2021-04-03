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