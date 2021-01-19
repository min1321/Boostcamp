- 정수형 int 4바이트
- 실수형 float 8바이트

- 문자열 특징
    - 슬라이싱 : text\[0:6\] 과 같은 형태로 사용
    - 역슬레시 : \\를 사용하여 '를 문자열에 포함하거나, 줄바꿈을 표시함

- call by object reference
    - call by value : 함수에서 값만 넘기는것 f(a) <<< a값이 복사되어서 들어가기만함
    - call by reference : pointer 개념  f(a)에서 에서 a값이 내부에서 변하면 같이 변함
        - swqp 개념에 많이 사용함
        - list가 안들어가고 -5 ~ 256사이의 값만 들어가면 value만 복사됨


```python
def spam(eggs):
    eggs.append(1)  # ham도 같은 주소를 참조하고 있어서 1이 추가됨
    eggs.append(2)
    del eggs[0]
    eggs = [2,3]  # eggs가 새로 선언되면 주소가 끊어짐
ham = [0]
spam(ham)
print(ham)
```

    [1, 2]
    

변수범위(Scoping Rule) 
 - 지역변수 : 함수 밖에는 영향주지 않음
 - 전역변수 : global s 를 설정해주면 함수 내에서 바뀐것이 밖에도 반영됨

재귀함수 (recursive Function)
 - 자기가 자기자신을 계속 호출하면서 loop를 돌아감

function type hints
 - dynamic typing : 처음 함수를 사용하는 사용자가 interface를 알기 어렵다는 단점
 - 인터페이스 명확히한다는 장점 있음  
 - 함수내 변수의 타입을 정해주고 출력물의 타입을 알려줌  
 
Docstring  
 - 함수 사용법 및 설명을 적어놓는 것
 - vs code에서 받아서 사용 가능  

함수를 사용하는 경우
 - 공통사용하는 경우 함수로
 - 복잡한 수식은 함수로
 - 복잡한 조건은 함수로
