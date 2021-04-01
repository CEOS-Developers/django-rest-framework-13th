# CEOS 13기 백엔드 스터디
<hr>

## REST API 서버 개발 - 인스타그램 클론

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
이 부분이 계속 오류가 생겨서 최대한 빨리 수정하겠습니다 ㅜㅜ

### 공부한 내용 정리
* JSON이 무엇이고 Seiraliziation이 왜 필요하며 어떤 방식으로 진행되는 지 알 수 있었습니다.
* Nested Serializer 를 사용하는 데 read_only 와 write_only를 어떤 상황에서 사용하는 지 공부해야 한다고 느꼈습니다ㅜㅜ
* POST에 대한 개념이 부족해서 공부를 해야할 것 같습니다. 왜 안되나요... 눈물만 납니다
    * 한 Model을 Post할 때 nest 된 모델의 field를 같이 입력하는 게 맞는 방향인 지 궁금합니다. 
      저는 Media의 FK로 Post를 잡았는데, Post의 인스턴스를 POST 할 때 하위 모델의 instance를 
      모두 입력해야 하는 게 맞는 상황인 지 궁금했습니다.
* fields= \_\_all__ 과 같이 모든 필드를 갖고 오는 명령문을 쓸 때 조심해야 하는 걸 배웠습니다.      

### 간단한 회고
다양한 에러를 맛 보게 되어 슬펐지만 그만큼 많이 배운 것 같아서 좋았습니다.  
전 주차에서 직접 만든 모델을 활용하는 과제이다 보니 뭔가 만들어져가는 느낌이 들어 재밌었습니다.  
에러는 재미 없었습니다.  
부족한 부분을 많이 느껴 앞으로 열심히 공부해야겠다고 느꼈습니다.