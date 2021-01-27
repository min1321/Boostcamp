# - 무엇을 배울지?  
    - CSV  
    - 웹
    - XML
    - JSON  

- CSV란 ?
    -  엑셀의 텍스트 데이터 형태
    - 콤마, 탭, 스페이스로 분리해서 데이터 저장



- 웹이란?
    - HTML은 웹에서 나타나는 정보의 표현 방법 중 가장 대표적인 방법
    
    
- XML(eXtensible Markup Languages)
    - 데이터를 저장하고 불러오는 전통적인 파일포맷
    
    
- JSON(JavaScript Object Notation)
    - raw파일을 저장하는 대표적인 포맷

- csv 파일 읽어올때 cp949를 사용하는 이유?
    - 윈도우에서 작성된 파일중 utf-8로 안읽어 지는 경우가 있기 때문에 cp949로 열어봄
- 저장할 때 encoding은?
    - utf-8로 저장해라
- csv.writer인자중에 delimiter의 의미?
    - 데이터 자르는 기준임
- csv.writer인자중에 quotechar는? 
    - 데이터 싸매는 기준임 작은 '따움표를 권장한다, 단 데이터에 ' 안들어가있을때

- web은?
    - 인터넷 공간의 정식 명칭
    - www 의 줄인말
    - 물리학자들간 정보 교환을 위해 만들어짐

![image.png](attachment:image.png)

- HTML은?
    - 웹상 정보를 구조적으로 표현
    - 제목, 단락, 링크를 **Tag** 형식으로 표현
    - 꺽쇠 괄호안에 들어가있음
    - 트리형 구조

- HTML 분석방법?
    - string
    - regular expresion
    - beautiful soup

- regular expression(정규식) 이란?
    - 복잡한 문자열 패턴
    - 특정한 규칙을 가진 문자열

- 정규식 많아서 다 알려줄 수는 없고 공부하는 방법 배워야함
    - 문자열 클래스  : [ ] 
    - . 은 전체를 의미
    - *는 앞을 만복 [To] 등등. 규칙을 찾아보고 공부
    - 정규식 연습장 주소 : https://regexr.com/
    - import re를 해서 사용

- **XML 데이터 타입이란?**
    - 데이터의 구조와 의미를 설명  
      Tag를 사용하여 표시
    - markup 언어 사용
    - 매우 유용한 저장 방식

- beautifulsoup 아직도 많이 사용됨

- 연습해보기 ipa110106.xml

- JavaScript Object Notation (JSON)
    - 간결성
    - 코드 연결성이 좋음
    - dict 타입으로 전환이 쉬운 형식이다
    - 용량도 적게 차지
    - 아래 왼쪽은 xml, 오른쪽은 JSON 타입임

![image.png](attachment:image.png)

- JSON 타입 사용방법
    - json 모듈로 쉽게 사용가능
    - 데이터 저장 및 읽기는 dict 타입으로 상호 호환 가능
    - 웹에서 제공하는 API는 대부분 정보 교환 시 JSON 활용
    - 페이스북, 트위터, Github 등 거의 모든 사이트가 사용함
    - 각 사이트 마다 Developer API의 활용법을 찾아서 사용함

- json 모듈에서 데이터 읽어오는 방법?
    - contennt = f.read()
    - json.loads(contents)
    
    
- json 모듈에서 데이터 쓰는방법?
    - json.dump(dict_data, f)


```python

```
