함수 : 어떤 일을 수행하는 코드의 덩어리


```python
def calculate_rectangle(x, y):
    return x * y
```

- 함수의 장점
    - 반복적인 수행을 1회만 작성 후 호출 가능
    - 코드를 논리적인 단위로 분리
    - 캡슐화 : 인터페이스만 알면 타인의 코드 사용


```python
# def 함수 이름 (parmaeter #1, #2):  
#     수행문\#1(statements)   "인덴테이션 Tab으로 띄워주는 것"
#     return <반한값>
```

- 함수는 상단에 적어주는 것이 좋음


```python
print("a", 200)
```

    a 200
    

함수 안에 함수를 구현하는 방법  
- 함수와 함수 사이에는 두깐 띄운다


```python
def fx(x):
    return 2 * x + 7


def gx(x):
    return x ** 2
```


```python
x = 2
fx(x) + gx(x) + fx(gx(x)) + gx(fx(x))
```




    151



- parameter : 함수의 입력 값 인터페이스  f(x)에서 x에 해당
- argument : 실제 parameter에 대입된 값 f(2)에서 2에 해당

- 함수 내부 주의사항
    - return을 하는 것과 print를 하는 것은 다름


```python
list_ex = [5, 4, 3, 2, 1]
```


```python
sorted(list_ex)
```




    [1, 2, 3, 4, 5]




```python
list_ex
```




    [5, 4, 3, 2, 1]




```python
list_ex.sort()
```


```python
list_ex
```




    [1, 2, 3, 4, 5]



CLI환경 : Command Line Interface  
input() string type으로만 받을 수 있음

포매팅  
- 3가지방법 있음  
    - %string : "%datatype"%(variable)  
        - %8.2f 는 전체 8칸으로 하고 소수점은 2자리까지 나타내라는 뜻  
    - format 함수  
       "{0} 아아아 {1:10.5f}".format("Apple", 0.9)  
       이렇게 {1:10.5f} 처럼 자리숫자랑 소수점 자리도 정해줄 수 있음  
       {0:<10s} 는 10칸 비우고 왼쪽 정렬해라는 뜻 (padding이라고 함)  
    - fstring 사용방법 (왼쪽 정렬이 기본임, \*을 넣으면 별로채움, ^는 가운데 정렬)  
      name = "choi"   
      count = 10  
      f"메모 내용 및 스트링{name}, 머라머라{count}"


```python
name = "choi"
count = 10  
print(f'메모 내용 및 스트링{name}, 머라머라{count}')
print(f'메모 내용 및 스트링{name:*^10}, 머라머라{count}')
print(f'메모 내용 및 스트링{name:*<10}, 머라머라{count}')
```

    메모 내용 및 스트링choi, 머라머라10
    메모 내용 및 스트링***choi***, 머라머라10
    메모 내용 및 스트링choi******, 머라머라10
    


```python
# Lab화씨 변환기
def fahrenheit():
    print("본 프로;그램은 섭씨를 화씨로 변환해주는 프로그램입니다.")
    C = float(input("변환하고 싶은 섭씨 온도를 입력해 주세요: "))
    F = ((9/5) * C) + 32
    print(f"섭씨온도 : {C:.1f}")
    print(f"화씨온도 : {F:.2f}")
```


```python

```


```python
fahrenheit()
```

    본 프로;그램은 섭씨를 화씨로 변환해주는 프로그램입니다.
    변환하고 싶은 섭씨 온도를 입력해 주세요: 32.2
    섭씨온도 : 32.2
    화씨온도 : 89.96
    


```python

```
