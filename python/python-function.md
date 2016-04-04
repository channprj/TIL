Title: 파이썬 함수
Date: 2016-02-08 13:00
Category: Python
Tags: python, programming, dev, scrpit, function, 파이썬, 프로그래밍, 개발, 스크립트, 함수, 공부, 스터디, study
Slug: python-function
Author: CHANN
<!--Summary: -->

## 파이썬 함수 개념
```python
def test(a, b)
	return a+b
```

파이썬에서는 함수도 객체. `def` 는 함수 객체를 만드는 구문. test 라는 이름은 생성된 함수 객체를 참조하는 레퍼런스. 메모리 어딘가에 함수 객체가 생성되는 것이고, 객체이기 때문에 생성할 때마다 다른 주소값을 가짐.

`return` 에서는 함수를 종료하고, 해당 함수를 호출한 곳으로 다시 되돌아감. 객체를 되돌려줌. `return` 을 적지 않아도, `return` 만 적어도 종료되며, 이때 반환값은 None.

------

## 일반 구조
일반적인 파이썬 함수는 아래와 같이 생김.

```python
def 함수이름(변수1, 변수2, ...):
	if(조건):
		# something...
	return 반환값
```

return 을 붙이지 않아도 실행이 모두 끝나면 자동으로 `return` 이 됨.
함수의 결과값 반환은 언제나 하나여야 하지만, 클래스 반환 등이 가능하므로 필요시 이러한 점을 응용하여 함수를 만들면 됨.

> return 은 언제나 하나의 객체만을 반환하지만, 리스트나 튜플, 심지어 클래스도 반환가능.

------

## 입력 변수 설정(Input Variable)
입력 변수의 갯수가 변화할 때는 아래와 같음.

```python
def 함수이름(*변수):
	for i in args: 
		sum = sum + i 
	# something...
	return 반환값
```

선택인자와 여러 개의 입력 변수를 통해 아래와 같이 활용 가능. 아래와 같이 `*args` 로 가변인자를 받는 것은 튜플 형태로 처리가 됨. 가변인자는 맨 뒤에 위치해야.

```python
def sum_mul(choice, *args): 
    if choice == "sum": 
        result = 0 
        for i in args: 
            result = result + i 
    elif choice == "mul": 
        result = 1 
        for i in args: 
            result = result * i 
    return result 
```

------

아래와 같이 함수에서 입력받는 변수의 초기값을 설정 가능. 단, 초기값을 부여할 변수는 항상 맨 뒤에 위치시켜야.

```python
def true_or_false(is_false, is_true=1): 
    if isTrue == 1: 
    	# something...
```

`true_or_false(1)` 또는 `true_or_false(1, 0)` 과 같은 형태로 함수를 사용할 수 있음.

------

정의되지 않은 인자는 **를 붙이면 되며, 인자를 사전 형식으로 만들어서 전달하는 것이 특징. 아래와 같이 URL 처리 시 매우 편리하고 유용하게 사용. 위의 내용들과 마찬가지로 정의되지 않은 인자는 항상 맨 뒤에 위치시켜야.

```python
def add_student(**student):
    url = "https://chann.kr/?"

    for key in student.keys():
        url += key + "=" + student[key] + "&"

    return url

print(add_student(id='student_id', password='student_pw'))
# https://chann.kr/?id=student_id&password=student_pw&

```


------

## 인자 전달
파이썬에서는 인자를 호출자 내부 객체의 레퍼런스로 전달함. 그러나 기존 컴파일언어인 C/C++의 `Call-by-reference` 와는 다름. 호출자가 전달하는 변수는 변경 가능한 경우와 변경 불가능한 경우의 처리방식이 다름.

```python
a = 1
b = 2
c = 3

def sum(x, y):
    return x + y

def sum_modify(a, y):
    a = 100  # 이름이 x이고 값이 100인 객체가 생성됨.
    return a + y

print(sum(a, b))  # result: 3

print(sum_modify(a, c))  # result: 103
# 함수 내부의 변경사항이 함수 외부에 영향을 미치지 않음.

print(a)  # result: 1
print(b)  # result: 2
print(c)  # result: 3
```

------

그러나 아래와 같은 경우엔 함수 내부에서의 변경값이 외부 변수에 영향을 미침.

> 정수형 변수는 변경 불가능한 변수이고, 리스트는 변경 가능한 변수임.

```python
word = []
word += 'OSX'

def change_char(a):
    a[-1:] = 'S'
    return

print(word)  # ['O', 'S', 'X']
change_char(word)
print(word)  # ['O', 'S', 'S']
```

------

## 스코핑 규칙(Scoping Rule)
객체는 별도의 네임스페이스를 가짐. 함수 내부의 변수는 일단 함수 내부의 네임스페이스를 참조함. 함수 내부의 네임스페이스에서 변수를 찾지 못하면 상위 네임스페이스에서 찾음. 먼저 함수 내부의 공간인 `Local scope` 에서 찾다가, 전역 영역인 `Global scope` 에서 찾고, 그래도 없을 시엔 파이썬 내장 영역인 `Built-in scope` 에서 찾음. 이것을 줄여서 `LGB Rule` 이라고 부름.

함수 안의 변수는 함수 안에서만 사용 가능. 함수 밖의 변수를 함수 안에서 불러서 변경시키고 싶으면 `global` 키워드를 사용하면 되지만 각 함수는 독립적으로 존재하도록 짜는 것이 좋음. 예시는 아래의 코드 참조.

```python
a = 0
def plus_one(): 
    global a  # 권장 x
    a = a+1

def minus_one(a): 
    a = a-1
    return a
    
a = minus_one(a)  # 권장 o
```

------

내장영역의 변수를 보려면 __builtins__ 를 검색하면 됨.

```python
>>> dir(__builtins__)
```

------

### 리턴(Return)
함수에서는 return으로 함수를 종료하고 해당 함수를 호출한 곳으로 돌아감. 이 때 return값을 통해 어떤 종류의 객체도 반환 가능하지만 오직 한 객체만 반환 가능함. 따라서 리턴하고자 하는 값이 여러개일 때는 class나 tuple로 묶어서 반환 가능. 보통은 상수와 같은 단일값을 리턴. return값을 따로 명시하지 않으면 None 객체가 반환.

```python
def swap(x, y):
    return y, x

a = 1
b = 2
a, b = swap(a,b)  # tuple 형태로 1과 2를 swap
print(a, b)  # result: 2 1
```

위와 같은 함수는 언뜻 보면 2개의 값을 반환하는 것 처럼 보이지만 실은 튜플의 형태로 하나의 객체가 반환되는 것.

------

## 람다 함수(Lambda Function)
Java와 마찬가지로 람다 함수는 익명 함수인데, 필요한 곳 어디에서나 쓰일 수 있지만 return 을 적을 수 없음. return 을 적지 않아도 한 줄을 실행한 결과값을 반환함. 예제는 아래와 같음. 이름이 왜 람다인가 찾아보니 [람다 대수](https://ko.wikipedia.org/wiki/람다_대수)에서 영향을 받은 것 같음.

```python
g = lambda x, y : x + y
print(g(1, 2))  # result: 3

print((lambda x: x*x)(3))  # result: 9
```

`globals()` 로 확인해 보면 알겠지만, 람다 함수는 사용한 직후 바로 사라짐. 그러므로 간단한 기능의 경우 람다 함수로 처리를 하여 편리성과 효율성을 높이는 것이 좋음.

람다 함수가 길어질 땐 문장의 끝에 `\` 문자를 붙여서 코드를 여러 줄로 입력 가능하지만 코드의 가독성과 오류를 유발할 수 있으므로 가급적 피해야.

------

## 재귀 함수(Recursive Function)
재귀 함수는 함수 내부에서 자기 자신을 호출함. 그러나 함수 호출이 잦으면 메모리를 과도하게 사용하므로 오버헤드(Overhead)가 날 수 있음. 대개 루프문이 재귀 함수보다 메모리 사용이 적고 속도가 빠르나 하노이의 탑과 같은 일부 문제는 재귀 함수로 접근하는 것이 효율적임.

> 이름 그대로 함수에서 함수를 자꾸 호출하는 함수

```python
def factorial(x):
    if x == 1:
        return 1

    return x * factorial(x-1)

print(factorial(5))  # result: 120
```

재귀 함수는 제네레이터(generator) 에서도 유용하게 쓰임.

```python
def crazy(min_):
    yield min_
    g=crazy(min_+1)
    while True:
        yield next(g)
        yield min_

i=crazy(1)
```

------

## pass
함수 및 클래스의ㅣ 메서드에서 아무런 동작도 하지 않도록 하기 위해 적는 구문. 언뜻 왜 있는건가 싶을 수도 있지만 빈 클래스를 만들어야 할 때 주로 많이 사용됨. 아래와 같은 예문에서는 pass 가 없으면 당연히 에러가 남.

> 이름 그대로 그냥 지나치는 녀석.

```python
class empty_dream:
    pass
```

------

## `__doc__` 속성, help 함수
특정 함수를 어떻게 사용해야 할 지 모를 때, `help()` 를 사용하여 함수의 매개변수와 반환값을 알 수 있음. 아래는 print 함수에 대해 알아보는 예문. 내장함수 뿐만 아니라 프로그래머가 직접 만든 함수에 대해서도 알 수 있음.

> 윈도우에서의 help 라던가 리눅스에서의 `man` 명령어와 유사하다고 보면 됨.

```python
>>> help(print)

Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

직접 만든 함수에 대한 추가 설명을 넣고 싶을 떈 `__doc__` 속성을 사용하면 됨. `__doc__` 속성은 객체에 대한 설명을 적는 데 사용함. 

```python
def plus(x):
    return x + 1

print(plus(1))  # result: 2

plus.__doc__ = "Just plus 1"

help(plus)

### result:
# 2
# Help on function plus in module __main__:
# 
# plus(x)
#     Just plus 1
```

`\_\_doc__` 속성으로 설명을 적지 않아도 """(쌍따옴표 3개)를 아래와 같이 함수 내 최상단에 적어주어도 됨.

```python
def plus(x):
    """
    This is Plus Function!!
    Oh yeah plus me baby :-)
    """
    return x + 1

help(plus)

### result:
# Help on function plus in module __main__:
# 
# plus(x)
#     This is Plus Function!!
#     Oh yeah plus me baby :-)

```

------

## 이터레이터(iterator)
이터레이터는 순회 가능한 객체의 요소에 순서대로 접근할 수 있는 객체임. 아래의 예제는 `for` 문을 기준으로 작성함. `for` 문에서 지정한 순회 가능한 이터레이터 객체를 가져오면 이터레이터 안의 `__next__()` 함수가 실행됨. `__next__()` 는 현재 이터레이터가 가리키는 객체의 요소를 반환하고 StopIteration 예외를 만날때까지 객체의 다음 요소로 이터레이터를 옮김. `__next__()` 함수는 내장함수 `next()` 로도 구현되어 있음.

> 이름 그대로 되풀이, 반복하는 기능을 가진 녀석임.

```python
for i in [1,2,3,4,5]:  # 리스트 순회
    print(i, end=' ')
print()

for i in ('a', 'b', 'c'):  # 튜플 순회
    print(i, end=' ')
print()

for key in {'s':'small', 'm':'medium', 'l':'large'}:  # 딕셔너리 순회
    print(key, end=' ')
print()

for c in "Oh good boy!":  # 한 글자씩 문자열 순회
    print(c, end='')
print()

for l in open("fake.txt"):  # 파일 내용을 라인 단위로 순회
    print(l)
```

이터레이터를 확인해 보는 예제는 아래와 같음.

```python
string = "OSX"

iter_check = iter(string)
print(iter_check)

print(next(iter_check))
print(next(iter_check))
print(next(iter_check))
print(next(iter_check))

### result:
# <str_iterator object at 0x106adb898>
# O
# S
# X
# Traceback (most recent call last):
#   File "/Users/CHANN/git/test.py", line 9, in <module>
#     print(next(iter_check))
# StopIteration
```

위와 같이 이터레이터가 끝에 도달하면 `StopIteration` 예외를 만나고 에러를 출력.

------

## 제네레이터(generator)
제네레이터는 이터레이터를 만드는 강력한 도구임. 함수가 호출되면 지역 변수와 코드가 스택에 적재되고 코드를 실행함. 그리고 함수가 끝나면 결과값을 호출한 곳에 값을 넘겨주고 함수 객체는 스택에서 사라지는데, 함수에 `return` 대신 `yield` 를 적으면 함수를 끝내지 않고 호출한 곳에 값을 전달함.

> 이름 그대로 값을 계속 발생시키는 녀석임.

```
def reverse(string):
    for i in range(len(string)-1, -1, -1):
        yield string[i]

for i in reverse("EM-EVOL"):
    print(i, end='')
print()

### result:
# LOVE-ME
```

위의 코드를 보면 `reverse()` 함수는 7번 호출되며, `yield` 를 호출한 곳에서 계속 값을 돌려주지만 함수는 메모리에 그대로 있음. 그래서 다음에 `reverse()` 가 다시 호출되더라도 가장 최근에 호출된 상태로 실행됨. 위에서 `return` 을 사용했다면 L만 출력됨.

```
def reverse(string):
    for i in range(len(string)-1, -1, -1):
        return string[i]  # <<< yield 대신 return 을 사용

for i in reverse("EM-EVOL"):
    print(i, end='')
print()

### result:
# L
```

앞서 언급한 바와 같이 제네레이터는 함수의 상태가 그대로 보존되기 때문에 이터레이터 객체를 만들 때 매우 강력하고 메모리가 절약된다는 장점을 가짐. 아래의 예제처럼 필요할 때마다 데이터를 생성하면 메모리 사용을 줄일 수 있음.

```
a = [1,2,3,4,5,6,7,8,9,10]  # 10개의 객체를 저장할 메모리 공간이 필요
print(sum(a))

b = (i for i in range(10+1))  # 메모리를 저장할 공간이 필요하지 않음

print(sum(b))
```

------

## 데코레이터(decorator)
Java 의 `annotation` 과 굉장히 비슷해보이지만 실은 많이 다름. 파이썬의 데코레이터는 이름 그대로 본체를 꾸며주는 역할을 함. 디자인 패턴의 일종이며, 원래의 작업에 대한 부가적인 작업을 수행할 경우에 주로 사용함. 그러나 원래의 작업에는 끼어들 수는 없다는 한계를 가짐. 본래 장식이라는 게 장식되는 물건을 바꾸지는 않는 것처럼, `decorator` 또한 원래의 작업은 손대지 않고 그 주변에서 필요한 작업을 하는 것. 이런 방법은 특히나 함수를 비교적 자유롭게 다룰 수 있는 언어(함수형 언어나 Python, Ruby 등의 스크립트 언어 등)들에서는 쉽게 구현됨. 예제는 아래와 같음.

> 함수를 래핑하여 앞뒤에서 전처리와 후처리를 하는 기능이라고 보면 됨

```python
class deco_test(object):
    def __init__(self, func):  # 생성자 내부에서 func를 불러서 데코레이터 이전에 함수를 생성함
        print("생성자!")
        func()  # 함수를 호출

    def __call__(self):  # 소멸자
        print("소멸자!")

@deco_test
def shit():
    print("이건 물소의 똥이야!! 똥!!")
    return

print("끝!!")
shit()

### result:
# 생성자!
# 이건 물소의 똥이야!! 똥!!
# 끝!!
# 소멸자!```



------

## 참고
1. [Codecademy](http://codecademy.com)
2. [Wikidocs](https://wikidocs.net)
3. [Udacity](https://udacity.com)
4. [dgoon Wiki](http://legacy-wiki.dgoon.net/doku.php?id=python:decorator)
5. [Python 3 Patterns Idioms](http://python-3-patterns-idioms-test.readthedocs.org/en/latest/PythonDecorators.html)