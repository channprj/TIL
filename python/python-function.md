Title: 파이썬 함수
Date: 2016-02-08 13:00
Category: Python
Tags: python, programming, dev, scrpit, function, 파이썬, 프로그래밍, 개발, 스크립트, 함수, 공부, 스터디, study
Slug: python-function
Author: CHANN
<!--Summary: -->

## 파이썬 함수 개념
```python
def Test(a, b)
	return a+b
```

파이썬에서는 함수도 객체. `def` 는 함수를 만드는 구문. Test 라는 이름은 생성된 함수 객체를 참조하는 레퍼런스. 메모리 어딘가에 함수 객체가 생성되는 것이고, 객체이기 때문에 생성할 때마다 다른 주소값을 가짐.

`return`에서는 함수를 종료하고, 해당 함수를 호출한 곳으로 다시 되돌아감. 객체를 되돌려줌. `return`을 적지 않아도, `return`만 적어도 종료되며, 이때 반환값은 None.

------
### 일반 구조
일반적인 파이썬 함수는 아래와 같이 생김.

```python
def 함수이름(변수1, 변수2, ...):
	if(조건):
		# something...
	return 반환값
```

return 을 붙이지 않아도 실행이 모두 끝나면 자동으로 `return` 이 됨.
함수의 결과값 반환은 언제나 하나여야 하지만, 클래스 반환 등이 가능하므로 필요시 이러한 점을 응용하여 함수를 만들면 됨.

------
### 입력받는 변수의 설정
입력 변수의 갯수가 변화할 때는 아래와 같음.

```python
def 함수이름(*변수):
	for i in args: 
		sum = sum + i 
	# something...
	return 반환값
```

선택인자와 여러 개의 입력 변수를 통해 아래와 같이 활용 가능.

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

아래와 같이 함수에서 입력받는 변수의 초기값을 설정 가능. 단, 초기값을 부여할 변수는 항상 맨 뒤에 위치시켜야.

```python
def true_or_false(is_false, is_true=1): 
    if isTrue == 1: 
    	# something...
```

`true_or_false(1)` 또는 `true_or_false(1, 0)` 과 같은 형태로 함수를 사용할 수 있음.

------

### 주의할 점
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

> 작성중

------

## 참고
1. [Codecademy](http://codecademy.com)
2. [Wikidocs](https://wikidocs.net)
3. [Udacity](https://udacity.com)
