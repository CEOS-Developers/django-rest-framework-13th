# CEOS 13기 백엔드 스터디
## REST API 서버 개발
### 인스타그램 클론

## 유의사항
* 본 레포지토리는 백엔드 스터디 2-3주차의 과제를 위한 레포입니다.
* 따라서 해당 레포를 fork 및 clone 후 local에서 본인의 깃헙 ID 브랜치로 작업한 후 커밋/푸시하고, PR 보낼 때도 `본인의 브랜치-> 본인의 브랜치`로 해야 합니다.

## 2주차 과제 (기한: 3/25 목요일까지)
https://brunch.co.kr/@ddangdol/4 - Field와 옵션에 대해 자세한 설명 참고
### 모델 설명
<img src="/image/modeling.PNG"></img>
#### Profile
userid - 가입하기 위한 아이디. 아이디는 중복이 불가(UNIQUE)  
password - 가입하기 위한 비밀번호  
nickname - 유저의 활동 닉네임. 닉네임은 중복이 불가(UNIQUE)   
user_image - 유저의 프사. 기본 이미지 가능(BLANK)  
post_num - 유저의 프로필 들어가면 게시글의 썸네일만 뜨게 하려고 만든 건데 생각해보니 필요없을거같아요.. 마이그레이션 할때 default를 설정하라는 오류가 떠서 DEFAULT=0으로 했어용  
#### Upload  
profile_id를 FK로 사용함 (1:N관계)  
description - 게시글의 본문. 가끔 갬성있게 올리고 싶을때 사진만 올리고 본문 안쓰는 경우를 대비(BLANK)  
upload_date - 생성의 타임스탬프를 뜻하는 AUTO_NOW_ADD 옵션 사용. 굳이 수정 시간이 필요하나 싶었습니다  
like_num - 특정 게시글의 좋아요 수를 나타냄   
comment_num - 특정 게시글의 댓글 수를 나타냄  
#### Upload_file  
Upload_id를 FK로 사용함 (1:N관계)  
file - 업로드한 사진/영상 저장
#### Comment
profile_id와 upload_id를 FK로 사용함 (둘다 1:N관계)  
description - 댓글의 본문  
comment_date - 수정의 타임스탬프를 뜻하는 AUTO_NOW 옵션 사용(근데 upload_date랑 통일시킬 필요가 있어보입니다)
#### Like 
comment 모델과 같음
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

