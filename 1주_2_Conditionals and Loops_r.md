- 조건문이란?
    - 조건에 따른 특정 동작을 하게하는 명령어  
      조건을 나타내는 기준과 실행할 명령으로 구성됨  
      참 거짓에 따라 실행되거나 안됨


```python
# if <조건>:  # if 를 쓰고 조건 삽입 후 ":" 입력
#    <수행조건 명령 1-1>
# else:
#    <수행조건 명령 2-1>
```

input()은 String으로 받으니 int로 변환이 반드시 필요.  
a is b 연산으로 비교시 -5 ~ 256까지는 정적 메모리로 관리하기때문에 true가 나옴

논리 연산자


```python
a= True
b = True
a and b 
```




    True




```python
a = True
b = False
a or b
```




    True




```python
boolean_list = [True, False, True, False, True]
all(boolean_list)
```




    False




```python
any(boolean_list)
```




    True




```python
value = 12
is_even = True if value %2 == 0 else False
is_even
```




    True




```python
print("당신이 태어난 년도를 입력하세요")
birth_year = input()
age = 2021 - int(birth_year) + 1

if 20<= age <=26  :
    print("대학생")
elif  17 <= age < 20:
    print("고등학교")
elif  14 <= age < 17:
    print("중학생")
elif   8 <= age < 14 :
    print("초등학생")
else:
    print("학생이 아닙니다")
```

    당신이 태어난 년도를 입력하세요
    1990
    학생이 아닙니다
    

반복문이란 시작조건, 종료조건, 수행명령으로 구성됨  
들여쓰기와 Block으로 구분됨


```python
for looper in [1,2,3,4,5]:
    print(f"{looper} : Hello")
```

    1 : Hello
    2 : Hello
    3 : Hello
    4 : Hello
    5 : Hello
    


```python
for looper in range(1,6):
    print(f"{looper} : Hello")
```

    1 : Hello
    2 : Hello
    3 : Hello
    4 : Hello
    5 : Hello
    


```python
list(range(5))
```




    [0, 1, 2, 3, 4]



반복문 변수명은 i,j,k를 사용함


```python
# for 문과 range를 활용하여 2배수만 뽑거나 -1로 감소가능  
for i in range(2, 10, 2):  
    print(i)  
```

    2
    4
    6
    8
    


```python
print("구구단 몇단을 계산할까요? ")

dan = int(input())

print(f"구구단 {dan}단을 계산합니다.")
for i in range(1,10):
    print(f"{dan} X {i} = {dan * i}")
```

    구구단 몇단을 계산할까요? 
    3
    구구단 3단을 계산합니다.
    3 X 1 = 3
    3 X 2 = 6
    3 X 3 = 9
    3 X 4 = 12
    3 X 5 = 15
    3 X 6 = 18
    3 X 7 = 21
    3 X 8 = 24
    3 X 9 = 27
    

- 디버깅
    - 문법적 오류
    - 논리적 오류


```python
x = 2
 y = 5
print(x+5)
```


      File "<ipython-input-18-fd8490d96080>", line 2
        y = 5
        ^
    IndentationError: unexpected indent
    



```python
x = 2
y = 5
pront(x+5)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-19-9245415cd447> in <module>
          1 x = 2
          2 y = 5
    ----> 3 pront(x+5)
    

    NameError: name 'pront' is not defined



```python
Data = "example"
print(data)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-20-e194e3d3e703> in <module>
          1 Data = "example"
    ----> 2 print(data)
    

    NameError: name 'data' is not defined



```python
#Python 환경에서 실행을 시키면 가장 먼저 실행되는 코드
def main():
    print("S")
if __name__ == "__main__":
    main()
```

    S
    

구글, 스택오버 플로우에서 검색
