# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.9.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ### List형 자료구조
# * 특징1 인덱싱

colors = ["red", "blue", "green"]

colors[0]

#  * 특징2 슬라이싱

print(colors[1:])
print(colors[-3:])

cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']

# * \[::-1\] 을 슬라이싱 하면 거꾸로 됨
# * \[0:8:2\]로 입력하면 마지막 값인 2는 건너뛰는 숫자를 의미함

print(cities[::-1])

print(cities[0:8:2])

colors * 2

colors.append("white")

colors

colors.extend(["black"])

colors

# 화면에 찍히는 값만 바뀌는 함수도 있고, 변환까지 일어나는 함수도 있음

# 삭제 연산은 del을 활용하여 삭제한다

del colors[0]
colors

# LIST에는 다양한 객체타입이 들어갈 수 있음 (시퀀스 자료형이라 다름)

a = ["color", 1, 0.2, [1,2,3]]

a

a = [5, 4, 3, 2, 1]
b = [1, 2, 3, 4, 5]

# a와 b의 각각의 공간이 생김

b = a

# b가 a의 주소를 가리키게 됨

a

b

a.sort()   # a가 변하는 함수

print(a)
print(b)

# b도 a의 공간을 가리키기 때문에 같이 바뀌게 됨
# 공간을 벗어나려면 재할당을 해주어야 함

a = [5, 4, 3, 2, 1]
b = a[:]

a.sort()
print(a)
print(b)

# 패킹과 언패킹

t = [1, 2, 3]

a, b, c = t   # 묶여져 있던게 풀어져 나온다는 개념

print(t, a, b, c)

# 리스트 안에 리스트를 만들어서 행렬(Matrix) 생성 가능  
# 단, midturm_copy = midturm\[:\] 을 해도 내부 주소가 연동되게되어 값을 바꾸면 바뀜  
# imoprt copy를  
# copy.deepcopy 를 이용해서 카피하면 수정 가능  
