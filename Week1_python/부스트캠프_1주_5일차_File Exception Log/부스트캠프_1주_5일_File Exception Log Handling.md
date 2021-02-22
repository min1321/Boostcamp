# 가장어려웠던 개념
   - **Pickle**

## - exception 이란 ?
    - 프로그램 짜다가 여러 오류 발생가능
    - 예상치 못했던 일

- 예외 종류
    - 예상가능한 예외
    - 예상 불가능항 예외 (인터프리터 과정에서 발생하는 예외)
         - 정수를 0으로 나누는 등등..

- excception 문법?
    - try ~ exception

![image.png](attachment:image.png)

 - except 이후에 나올 수 있는 구문
    - else, finaly 가 나올수 있으나 권장하지 않음

- assert 무엇이고 왜 사용?
    - 함수에서 인스턴스 값이 제대로 안들어 갔을 때 멈춰 줄 수있음
    - 뒷쪽 리소스 많이 들어갈때 미리 멈추어 줌

## - 파일의 종류
    - text파일은 메모장으로 열림
    - binary파일은 메모장에서 이상한 글자로 뜸
        - 컴퓨터만 이해할수 있는 파일, 이진파일이라고도 함
        - ex. excel, 워드파일 등

![image.png](attachment:image.png)

- 파이썬에서 파일 처리를 위해서는 어떤 함수 사용?
    - f = open("<파일이름>", "접근모드")  
        - <같은 폴더에 파일이 있어야함

- 접근모드의 종류

![image.png](attachment:image.png)

- 파일을 열었다가 닫는 방법

![image.png](attachment:image.png)

- with 구문이란?
    - 인덴테이션 끝나면 자동으로 close 됨

![image.png](attachment:image.png)

- file write 방법?
    - mode는 'w', encoding="utf8"을 사용

## - 폴더를 반드는법?
    - import os
    - os.mkdir('sukmin')

- 파일 옮길때??
    - import shutil 을 사용함
    - 최근에는 pathlib 모듈을 사용함, 장점은 리눅스 맥에서 사용 가능
        - path를 객체형태로 사용가능

# <span style="color:blue"> - picle 이란? </span>
    - 객체는 어디에 있을까?
        - 메모리에 있음
    - 변수를 파일형태로 저장해서 영속화 할 수 있음

![image.png](attachment:image.png)

![image.png](attachment:image.png)

- longging handling
    - 핵을 잡으려면?

- 우선 일어나는 일을 기록부터 하기
    - 개발시점에 기록
    - 실행시점에 기록

- logging 무슨모듈 사용할까?
    - import logging

![image.png](attachment:image.png)

- 로그파일 세팅을 해주려면 레벨이나 여러개를 해줘야하는데, 방식이 2개 있음
    - configparser : 파일에 설정해서 알려주는 방법
    - argparser : 실행시점에 알려주는 방식

```python

```
