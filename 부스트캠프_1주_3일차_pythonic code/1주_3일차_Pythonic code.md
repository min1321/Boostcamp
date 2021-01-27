- Pythonic code란?
    - 파이썬 스타일의 코딩 기법
    - 파이썬 특유의 문법을 활용한 효율적인 코딩
    - 딱 나눠서 이야기 할수는 없음

- Pythonic code 대표 종류
    - split & join
    - list comperehension
    - enumerate & zip
    - lambda & map & reduce
    - generator
    - asterisk

- 왜 이걸 배우나?
    - 남 코드에 대해서 이해도 높이기
    - 효율적으로 조금더 빠르게
    - 잘짜는 것 처럼 보이기

- split & join
    - split으로 문자열 빈칸 자르기
    - join으로 붙이기


```python
items = "zero one two three"
items = items.split()
items  

# ['zero', 'one', 'two', 'three']
```




    ['zero', 'one', 'two', 'three']




```python
num = " ".join(items)
num

# 'zero one two three'
```




    'zero one two three'



- list comperehension (list 내부 한줄로 사용??)
    - for 문 돌아서 append 보다 빠름
    - \[i for i in range(10)\]


```python
num1 = [1,2,3,4]
num2 = [5,6,7,8]
result = [i + j for i in num1 for j in num2]
result

# [6, 7, 8, 9, 7, 8, 9, 10, 8, 9, 10, 11, 9, 10, 11, 12]
```




    [6, 7, 8, 9, 7, 8, 9, 10, 8, 9, 10, 11, 9, 10, 11, 12]




```python
result = [i + j for i in num1 for j in num2 if j > i*2]
result
# 단 else까지 사용할때는 앞으로 빼서 for 문 앞에 사용

# [6, 7, 8, 9, 7, 8, 9, 10, 10, 11]
```




    [6, 7, 8, 9, 7, 8, 9, 10, 10, 11]



- print 말고 깔끔하게 보이려면??
    - pprint 사용   >> pprint.pprint()

- enumerate & zip
    - 인덱스랑 같이호출, 두개 묶어서 같이 호출

- lambda 란??
    - 함수 이름 없이 함수처럼 사용할 수 있는 익명 함수


```python
f = (lambda x, y : x+y)
f(10, 50)

# 60
```




    60




```python
(lambda x, y : x+y)(10, 50)

# 60
```




    60



- python3에서는 lambda 사용을 권장하지 않으나 많이 사용함
    - test가 어려움
    - 안쓰는게 좋지만 많이 사용함

- map fuction
    - 시퀀스 데이터에 각각 적용해줌
    - map도 가독성이 떨어지니 사용 권장하지 않으나 많이 사용함


```python
ex = [1,2,3,4,5]
f = lambda x : x ** 2

list(map(f, ex))

# [1, 4, 9, 16, 25]
```




    [1, 4, 9, 16, 25]




```python
f = lambda x, y : x + y
list(map(f, ex, ex))  # zip 처럼도 사용 가능함

# [2, 4, 6, 8, 10]
```




    [2, 4, 6, 8, 10]



- 이터러블 오브젝트는 내부적으로 __iter__와 __next__ 가 사용됨

- generator란??
    - iterable object를 특수한 형태로 사용해주는 함수
    - 주소만 가지고 있다가 사용되는 시점에 값을 던져주는 경우


```python
def generator_list(value):
    result = []
    for i in range(value):
        yield i
```


```python
result = generator_list(10)
print(result)   # 주소만 출력이됨
[value for value in result]

# <generator object generator_list at 0x00000187E1EBA190>
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

    <generator object generator_list at 0x00000189E3EB74A0>
    




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
import sys
def general_list(value):
    result = []
    for i in range(value):
        result.append(i)
    return result
result_general = general_list(50)
result_generator = generator_list(50)
print(sys.getsizeof(result_general))
print(sys.getsizeof(result_generator))

# 520
# 112
```

    520
    112
    


```python
gen_ex = (n*n for n in range(500))
print(type(gen_ex))

# <class 'generator'>
```

    <class 'generator'>
    

- genorator 언제 사용?
    - 빅데이터 같은 큰 데이터 처리할때 메모리 차지 적음

- function passing arguments 종류
    - keyword arguments
    - default argument
    - 

- keyword arguments


```python
def print_somthing(x, y):
    print(x, y)

print_somthing(y="ABC", x="DSDSDS")

# DSDSDS ABC
```

    DSDSDS ABC
    

- default argument
    - 입력하지 않아도 사용가능


```python
def print_somthing(x, y="디폴트값"):
    print(x, y)
print_somthing(x="DSDSDS")

# DSDSDS 디폴트값
```

    DSDSDS 디폴트값
    

- variable-length asterisk (가변인자)
    - parameter가 안정해져있을때
    - 일반적으로 *args를 변수명으로 사용
    - 튜플형태로 들어감


```python
def asterisk_test(a, b, *args):
    print(list(args))
    print(type(args))
    return a+b+sum(args)
print(asterisk_test(1,2,3,4,5))

# [3, 4, 5]
# <class 'tuple'>
# 15
```

    [3, 4, 5]
    <class 'tuple'>
    15
    

- keyword variable-length 키워드 가변인자
    - \*\*두개 사용
    - dict type으로 입력됨


```python
def kwargs_test_1(**kwargs):
    print(kwargs)
    print(type(kwargs))

kwargs_test_1(first=3, second=4, third=5)

# {'first': 3, 'second': 4, 'third': 5}
# <class 'dict'>
```

    {'first': 3, 'second': 4, 'third': 5}
    <class 'dict'>
    

- 순서 지켜야함 키워드형태로 값을 넣어주기 시작했으면 전부 키워드형태로만 들어가야함


```python
def a(one, two=3, *args, **kwargs):
    print(one)
    print(two)
    print(args)
    print(kwargs)
    
a(one=3, 300, first=3, second=4, third=5)


#   File "<ipython-input-17-e53b846c689a>", line 7
#     a(one=3, 300, first=3, second=4, third=5)
#              ^
# SyntaxError: positional argument follows keyword argument

```


      File "<ipython-input-17-c6044b0a4d2f>", line 7
        a(one=3, 300, first=3, second=4, third=5)
                 ^
    SyntaxError: positional argument follows keyword argument
    



```python
def a(one, two=3, *args, **kwargs):
    print(one)
    print(two)
    print(args)
    print(kwargs)
    
a(3, 300, 2,3,4, first=3, second=4, third=5)

# 3
# 300
# (2, 3, 4)
# {'first': 3, 'second': 4, 'third': 5}
```

    3
    300
    (2, 3, 4)
    {'first': 3, 'second': 4, 'third': 5}
    

- asterisk  (\*)
    - unpacking a container 형태로 사용할 수 있음
    - 풀어서 대입가능
    - \*\* 별표 두개로 하면 dict를 풀어주어서 각각 대입시킴


```python
def asterisk_test( *args):
    print(a, *args)
    print(a, args)
    print(type(args))
    
test = (2,3,4,5,6)
print(asterisk_test(1, *test))
print("----------------------")
print(asterisk_test(1, test))


# <function a at 0x00000187E1E93F70> 1 2 3 4 5 6
# <function a at 0x00000187E1E93F70> (1, 2, 3, 4, 5, 6)
# <class 'tuple'>
# None
# ----------------------
# <function a at 0x00000187E1E93F70> 1 (2, 3, 4, 5, 6)
# <function a at 0x00000187E1E93F70> (1, (2, 3, 4, 5, 6))
# <class 'tuple'>
# None
```

    <function a at 0x00000189E3E78C10> 1 2 3 4 5 6
    <function a at 0x00000189E3E78C10> (1, 2, 3, 4, 5, 6)
    <class 'tuple'>
    None
    ----------------------
    <function a at 0x00000189E3E78C10> 1 (2, 3, 4, 5, 6)
    <function a at 0x00000189E3E78C10> (1, (2, 3, 4, 5, 6))
    <class 'tuple'>
    None
    
