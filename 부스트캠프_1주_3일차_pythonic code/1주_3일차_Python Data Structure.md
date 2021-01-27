<span style="color:red">붉은 색</span>
<span style="color:blue">파란 색</span>

- Data type
    - 특징 있는 정보는 어떻게 저장하면 될까?  
        1. 전화번호부?
        2. 은행번호표?
        3. 서적 정보는 어떻게 관리하면 좋을까?
        4. 창고에 쌓인 수화물의 위치를 역순으로 찾을 때?

- 구조의 종류  
    - 스택 큐
    - 튜플 집합
    - 사전
    - Collection 모듈

- Stack이란?, python에서 어떻게 구현?, 실생활 예시는??
    - 나중에 넣은 데이터 먼저 반환 (LIFO : Last in First Out)
    - List 활용, append, pop으로 구현
    - 말그대로 쌓아 넣는 택배 화물차

- Queue 구조란?? , python에서 어떻게 구현??
    - 먼저 넣은 데이터 먼저 반환 (FIFI : First in First Out)
    - list에서 append와 a.pop(0) 을 사용하면 됨

- 튜블(Tuple) 구조란??, 파이썬에서 어떻게 구현??, 왜 사용?
    - 값이 변경 안되는 구조
    - () 괄호 안에 넣어서 구현, (1,)과 같이 한개는 콤마 필요
    - 학번 이름 등 중간에 바뀌면 안되는 값을 넣을 때 사용

- set이란?, 하나추가 방법?, 삭제방법?, 여러개 추가방법?, 교집합? 합집합?, 차집합?
    - 순서에 상관없이 중복 불허용
    - 하나추가 : add함수
    - 삭제 방법 : remove함수
    - 여러개 추가방법 : update(\[1, 2, 3, ,4\])
    - 합집합 : |, 교집합 : &, 차집합 : -

- Dict이란?
    - 구분지을 수 있는 값과 함께 저장
    - Key 값과 Value를 관리함

- collections 모듈이란?, 자주사용하는 모듈
    - list, tuple, dict에 대한 확장 자료구조 (모듈), 편의성, 효율성
    - deque, Counter, OrderedDict, defaultdict, namedtuple

- deque???, 한칸씩 옆으로 도는것??
    - stack과 queue를 지원
    - rotate가 가능

- OrderedDict 지금은 크게 의미 없음, 지금 dict는 순서를 보장함

- defaultdict, 언제 주로 활용할 수 있을까??
    - 초기값을 설정해주는 것 기존에 그 key가 없으면 0으로 한다거나 하는식
    - 단어갯수를 count 해줄때 +=1 해주면 처음 값이 없으면 0으로 인식해서 더해줌
    - 때문에 데이터 마이닝에사용가능

- Counter ???
    - 시퀀스타입의 데이터 갯수를 dict형태로 출력해줌
    - 집합연산도 가능
