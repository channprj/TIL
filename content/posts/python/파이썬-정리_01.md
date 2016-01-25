Title: 파이썬 기초
Date: 2016-01-04 20:12
Category: Python
Tags: python, programming, dev, scrpit
Slug: python-variable-operator
Author: CHANN
<!--Summary: -->

> 작성중

## 특징
* 인터프리터 언어
* 가독성이 좋음
* 접착성이 좋음(풀 언어(glue language)라고도 부름)
* 무료
* 방대한 오픈소스
* 유니코드 기반
* 동적 타이핑

----

## 2.x와 3.x의 차이
> 작성중

* print 함수 형태 변경
* int 형으로 통일됨
* 하지만 나누기 결과는 float
* 3.x는 문자열 기본 인코딩이 유니코드

----

## 설치법
### 윈도우
[파이썬 재단 홈페이지](https://www.python.org/downloads/) 참고.

----

### 맥
맥에는 기본적으로 2.7.10이 내장되어 있다. 가급적 3.x 이상의 버전을 사용하라고 권고하고 있으니 따로 설치만 해주면 된다.

[파이썬 재단 홈페이지](https://www.python.org/downloads/) 참고.

----

### 리눅스
`apt-get`, `yum` 등 별도의 패키지 관리도구를 이용해서 설치하면 된다.
 
[파이썬 재단 홈페이지](https://www.python.org/downloads/) 참고.
 
----

## 변수명
변수명은 문자, 숫자, 언더바(_)를 포함 가능하지만 숫자가 먼저 올 수 없다.

```python
>>> python = 1
>>> Python = 2
>>> python_var = 3
>>> python_1 = 4
```
<br>

사전에 기능과 의미가 정의된 파이썬 키워드는 변수명으로 사용할 수 없다.

```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

----

## 문자열
반드시 큰따옴표("")나 작은따옴표('')로 감싸야 한다.

```python
>>> 'str'
>>> "str"
>>> "This is 'str'"

# 여러 줄 입력일 경우
>>> print("""
나는
너의
동반자
""")
```
<br>

이스케이프 문자는 C와 유사하다.

* `\n`	: 줄바꿈
* `\t`	: 탭
* `\r`	: 캐리지 반환
* `\0`	:  NULL
* `\\`	: '\'문자
* `\'`	: 따옴표 문자
* `\"`	: 쌍따옴표 문자

```python
>>> print("This is \nEscape character.")
This is
Escape character.
>>> 
```
<br>

문자열을 다루는 것도 쉽다. 잘라 쓰기 쉽고 붙이기는 더 쉽다. 자동으로 배열처럼 인덱싱도 된다. 인덱스를 이용하여 문자열의 특정 문자를 다른 문자로 변경할 수는 없으나 문자열 전체를 변경하는 것은 가능하다.

```python
>>> '파이' '썬'
'파이썬'

>>> '파이'+'썬'
'파이썬'

>>> '파이' * 3
'파이파이파이'

>>> a = '파이썬'
>>> a[2]
'썬'

# 0(시작)부터 2글자 슬라이싱
>>> a[0:2]
'파이'

# 시작(0 생략)부터 3글자까지 슬라이싱
>>> a[:3]
'파이썬'

# 뒤에서부터 1글자만 슬라이싱
>>> a[-1:]
'썬'
```

----

## 리스트
파이썬에서의 리스트는 값의 나열이라 순서가 있으며 여러 종류의 값을 담을 수 있다. 인덱스는 0부터 시작하며 슬라이싱도 가능하다.

```python
# 배열의 선언
>>> food = ['rice', 'cheese', 'apple']

# 배열 출력
>>> food
['rice', 'cheese', 'apple']

# 배열의 타입 체크
>>> type(food)
<class 'list'>

# append() 함수로 리스트 뒤에 새 아이템 추가
>>> food.append('chicken')
>>> food
['rice', 'cheese', 'apple', 'chicken']

# insert() 함수로 리스트 중간에 새 아이템 추가
>>> food.insert(2, 'banana')
>>> food
['rice', 'cheese', 'banana', 'apple', 'chicken']

# extend() 함수로 여러 아이템을 한번에 추가
>>> food.extend(['cola', 'cider', 'coffee'])
>>> food
['rice', 'cheese', 'banana', 'apple', 'chicken', 'cola', 'cider', 'coffee']

# += 연산자로 리스트 붙이기
>>> food += ['cake']
>>> food
['rice', 'cheese', 'banana', 'apple', 'chicken', 'cola', 'cider', 'coffee', 'cake']

# 문자열을 붙일 경우 각 문자단위로 쪼개져서 붙음
>>> food += 'ice'
>>> food
['rice', 'cheese', 'banana', 'apple', 'chicken', 'cola', 'cider', 'coffee', 'cake', 'i', 'c', 'e']

# index() 함수로 인덱스 번호 체크
>>> food.index('apple')
3

## 인덱스 찾는 시작점 부여
>>> food += ['apple'] # 리스트 아이템 추가
>>> food.index('apple', 5)
12

# count() 함수로 리스트 아이탬 갯수 체크
>>> food.count('apple')
2
```
<br>

기본적으로 리스트 아이템을 삭제하는 건 크게 2가지 방법이 있다.

* pop()	: 뒤에서부터 값을 빼내옴.
* remove()	: 위치에 상관없이 리스트 아이템 삭제.

```python
# pop() 함수는 리스트 맨 뒤 아이템을 출력 후 삭제
>>> food.pop()
'banana'

# remove()는 위치에 관계없이 조용히 해당 리스트 아이템만 삭제
>>> food.remove('i')
>>> food.remove('e')

# 지우고자 하는 아이템이 없으면 오류메시지 출력
>>> food.remove('r')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list

```
<br>

정렬방법은 아래와 같다.

```python
# 순방향 정렬
>>> food.sort()
>>> food
['apple', 'apple', 'banana', 'c', 'cake', 'cheese', 'chicken', 'cider', 'coffee', 'cola', 'e', 'i', 'rice']

# 역순 정렬
>>> food.reverse()
>>> food
['rice', 'i', 'e', 'cola', 'coffee', 'cider', 'chicken', 'cheese', 'cake', 'c', 'banana', 'apple', 'apple']
```

----

## 세트
수학에서의 집합과 동일. 데이터의 순서는 없음.

```python
# 변수 선언
>>> set = {1,2,3,4,5}

# 세트 확인
>>> set
{1, 2, 3, 4, 5}

# 타입 확인
>>> type(set)
<class 'set'>

# 합집합
>>> a  = {1,2}
>>> b = {3,4,5}
>>> a.union(b)
{1, 2, 3, 4, 5}

# 교집합
>>> a = {1,2}
>>> b = {1,2,4}
>>> a.intersection(b)
{1, 2}

# 기타 집합 연산자
## 차집합
>>> b - a

## 합집합
>>> a | b

## 교집합
>>> a & b
```

----

## 튜플
> 작성중

리스트와는 다르게 ()로 묶어서 표현. 주로 읽기 전용으로 쓰이기 때문에 제공되는 함수는 적지만 그만큼 속도가 빠름.

```python
>>> tuple = (1,2,3)
>>> type(tuple)
<class 'tuple'>
>>> tuple
(1, 2, 3)

# 튜플을 이용한 Swap 응용. 임시 변수가 필요 없음.
>>> a,b = 1,2
>>> a,b
(1, 2)
>>> a,b=b,a
>>> a,b
(2, 1)

# 튜플 내부 값 확인
>>> a = (1,2,3)
>>> 1 in a
True

# 리스트, 세트, 튜플은 list(), set(), tuple()의 함수를 이용해 서로 언제든지 변환 가능.
>>> a = [1,2,3]
>>> b = tuple(a)
>>> b
(1, 2, 3)
```

----

## 사전
키와 값의 쌍으로 구성된 자료구조. 키와 값 이외의 인덱스는 지원하지 않음.

```python
>>> dictionary = dict(a=1, b=2, c=3, d=5)
>>> dictionary
{'a': 1, 'c': 3, 'd': 5, 'b': 2}

# dict() 생성자 없이 생성 가능
>>> size = {"s":"small", "m":"medium", "l":"large"}
>>> size["l"]
'large'

# 사전의 내용은 items(), keys(), values() 함수로 받아옴
## items()
>>> for z in size.items():
...     print(z)
...
('s', 'small')
('l', 'large')
('m', 'medium')
>>> for z, x in size.items():
...     print(z,x)
...
s small
l large
m medium

## keys()
>>> for z in size.keys():
...     print(z)
...
s
l
m

## values()
>>> for z in size.values():
...     print(z)
...
small
large
medium
```

----

## 논리연산자
```
>>> 1 > 2
False

>>> 1 != 2
True

>>> 1 == 1
True

>>> True & True
True

>>> True | False
True

>>> True or False
True

>>> not False
True

>>> bool(1)
True

>>> bool("Good")
True

>>> bool(None)
False
```

----

## 얕은 복사, 깊은 복사
모든 변수는 객체의 주소를 가짐. 

### 얕은복사
아래 예시에서 `b = a` 의 경우, a가 가리키는 객체의 주소를 b에 복사한 것. 이해가 안 된다면, `id()` 함수를 사용하여 객체의 고유값을 확인해보자.

```python
>>> a = [1,2,3]
>>> b = a
>>> a[0] = 'a'
>>> a
['a', 2, 3]
>>> b
['a', 2, 3]
```

`copy()` 함수를 사용하면 주소가 복사되어 객체를 공유하는 앝은 복사(shallow copy)가 됨. 일반적으로 생각하는 '참조'의 개념과 같음.

### 깊은복사
`deepcopy()` 함수를 사용하면 객체를 공유하지 않는 깊은 복사(deep copy)가 됨. 일반적으로 생각하는 '복사'의 개념과 같음.

------

## 함수
```python
def Test(a, b)
	return a+b
```

파이썬에서는 함수도 객체다. `def` 는 함수를 만드는 구문이다. Test 라는 이름은 생성된 함수 객체를 참조하는 레퍼런스다. 메모리 어딘가에 함수 객체가 생성되는 것이고, 객체이기 때문에 생성할 때마다 다른 주소값을 가진다.

`return`에서는 함수를 종료하고, 해당 함수를 호출한 곳으로 다시 되돌아간다. 객체를 되돌려준다. `return`을 적지 않아도, `return`만 적어도 종료되며, 이때 반환값은 None이다.

