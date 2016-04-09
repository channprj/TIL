Title: 파이썬 제어문
Date: 2016-04-09 21:00
Category: Python
Tags: python, programming, dev, scrpit, loop, condition, 파이썬, 프로그래밍, 스크립트, 언어, 반복문, 조건문, 개발
Slug: loop-condition
Author: CHANN
<!--Summary: -->
## 조건문
다른 언어들과 마찬가지로 `if`, `elif`, `else` 조건문이 있음. 여러줄일 경우 들여쓰기로 블록을 지정해야 함. 예시는 아래와 같음.

------
### if 문

```python
    if a == 1:
        print("a is 1 !!")
    elif a == 2:
        print("a is 2 !!")
    else:
        print("a is not 1 and 2")
```

------

#### 파이썬에서의 장점
*C* 나 *Java* 계열의 언어와는 다르게 `score >= 80 && score < 90` 과 같은 방식으로 표현하지 않고 `80 <= score < 90` 과 같은 구문을 지원. 코드를 쓰기에도 쉽고 보기에도 편리함.

------

### 조건식 참/거짓 판별
조건식의 참/거짓은 `bool()` 내장함수의 판단방식과 같음. 대략적인 판단은 아래와 같음.

* 상수의 값이 0일 경우 거짓인 `False`, 0이 아닐 경우 `True`
* 리스트, 튜플, 딕셔너리가 비어있거나 빈 문자열의 경우 `False`
* 논리연산자는 왼쪽에서 오른쪽방향으로 진행하여 판단 (좌변을 우선으로 단축평가 가능)

단축평가(short-circuit evaluation)란 앞부분에서 참이나 거짓임이 자명할 때 조건식 전체를 연산하여 평가하지 않는 것을 의미.

------

## 반복문
파이썬은 당연히 `while`, `for` 와 같은 반복문이 있음. 조건문과 마찬가지로 여러줄일 경우 들여쓰기로 블록을 지정해야 함. 예시는 아래와 같음.

------

### while 문
```python
i = 0
while i < 5:
    print("print", i, "times !!")
    i += 1
```

------

### for 문
```python
for i in range(5):
    print("print", i, "times !!")
```

#### 파이썬에서의 한계
`for` 문에서 주목할 점은 `while` 문과는 다르게 순회 가능한 시퀸스형 자료를 토대로 반복문을 수행한다는 것. 이터레이터(iterator)이기 때문에 수행 중 점프가 힘들다는 단점을 가짐. `continue` 혹은 `break` 는 가능하나 임의로 수행을 단축시킬 수는 없음. 파이썬의 `for` 문은 *C* 나 *Java* 의 `for` 문과는 다름. `foreach` 에 가깝다고 봐야함. 이러한 경우엔 `while` 문을 사용해야.

```python
for i in range(10):
    if i % 3 == 0:
        print(i, "jump!")
        # iterator 값이 우선이라 index 값으로 반복을 제어할 수 없음.
        i += 5
        continue
    print(i, "numbers.")

### result:
# 0 jump!
# 1 numbers.
# 2 numbers.
# 3 jump!
# 4 numbers.
# 5 numbers.
# 6 jump!
# 7 numbers.
# 8 numbers.
# 9 jump!
```

하지만 `foreach` 에 가까우므로 `for i in [1,2,3,4,5]:` 와 같은 구문으로 시퀸스형 자료를 이터레이터(iterator)로 사용 가능.

------

## 응용
`for` 문을 아래와 같이 C 스타일로도 사용 가능.

```python
word = "APPLE"
for i in range(len(word)):
    print("index: {0}, value: {1}".format(i, word[i]))
```

------

아래와 같이 `enumerate()` 내장함수도 이용 가능.

```python
word = "APPLE"
for i in enumerate(word):
    print(i)
```

------

아래와 같이 조건문을 넣을 수도 있음.

```python
word = ["Apple", "Cat", "Banana", "Tea"]
print([i for i in word if len(i) > 4])
```

------

```python
m = [10, 99, 101, 1000]

### filter 사용 가능
result = filter(big_money, m)

### 아래와 같이 lambda 가능
# result = filter(lambda m: m > 100, m)

for i in result:
    print("Big Money: {0}".format(i))

### result: 
# Big Money: 101
# Big Money: 1000
```

------

## 참고
1. [Python Documentation](https://docs.python.org/3.4/index.html)
2. [Wikidocs](http://wikidocs.net/)