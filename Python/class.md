Title: 파이썬 클래스
Date: 2016-04-25 21:00
Category: Python
Tags: python, programming, dev, scrpit, function, study, class, oop, 파이썬, 프로그래밍, 개발, 스크립트, 함수, 공부, 스터디, 클래스, 객체지향
Slug: class
Author: CHANN
<!--Summary: -->

파이썬은 객체지향 언어이기에 클래스를 사용을 권장함. 클래스는 좀 더 효율적이고 간결하게 기능을 구현하기 위해 존재. 클래스는 [객체지향 프로그래밍 언어](https://ko.wikipedia.org/wiki/객체_지향_프로그래밍)에서 주로 사용하는 개념. 상속(Inheritance), 다형성(Polymorphism), 캡슐화(Encapsulation) 또는 정보은닉(Information Hiding)의 개념을 알아야 함.

## 선언
클래스는 선언과 동시에 객체로 생성됨. 일반적인 클래스는 데이터와 메서드로 구성되나 없어도 무방. 

```python
class SamplePerson(object):  # 클래스 정의
    """docstring for SamplePerson"""  # 클래스에 대한 설명, help(클래스이름()) 입력시 나타남.

    name = "CHANN"  # 멤버 변수

    def __init__(self, arg):  # 생성자
        super(SamplePerson, self).__init__()
        self.arg = arg

    def who_am_i(self):  # 멤버 메서드
        print("I am {0}".format(self.name))

person = SamplePerson("Object Sample")  # 인스턴스 객체 생성
person.who_am_i()  # 클래스 내 함수를 호출하여 멤버 변수 출력: I am CHANN

person.name = "찬"  # 인스턴스 객체의 멤버 변수 값 변경
person.who_am_i()  # I am 찬

```

클래스를 정의하면 클래스 객체가 생성되고 독립적인 네임스페이스가 설정됨. 클래스를 사용하려면 일반적으로 인스턴스 객체를 생성해야함. 인스턴스 객체는 클래스의 이름을 사용하여 함수를 호출하는 형태. 인스턴스 객체의 변수나 메서드가 변경되기 전까지는 기존의 클래스 객체를 가리킴.

클래스의 변수와 메서드를 접근할 떈 속성 접근자 `.` 를 사용. 파이썬의 철학은 개발자에게 많은 제약을 가하지 않는 것이기에 기본적으로 클래스와 인스턴스의 접근 권한은 `public` 임.

`self` 는 현재 인스턴스 객체를 가리키는 것이며, C++ 이나 Java 의 this 와 거의 동일하지만 파이썬에서는 특별히 예약어로 지정되지는 않았음. 관용적으로 사용하기 때문에 메서드의 첫 인자는 self로 사용하는 것이 좋음.

------

메서드 호출 시 크게 2가지 방법이 있음.

- 바운드(Bound) 메서드 호출 - `person.who_am_i()`
- 언바운드(Unboud) 메서드 호출 - `SamplePerson.who_am_i(person)`

바운드 메서드 호출은 암묵적으로 첫 인자를 인스턴스 객체로 선언하나 호출할 때엔 자동으로 반영되기 때문에 따로 명시하지 않음. 인스턴스 객체로 클래스 메서드 호출.

언바운드 메서드 호출은 명시적으로 첫 인자로 인스턴스 객체를 전달함. 클래스 객체를 통해 메서드를 호출함. 클래스 객체에서 인스턴스 객체를 받아서 호출.

멤버 메서드에서 `self` 가 누락된 경우 원하는 값을 출력하지 않음. 전역 변수와 이름이 같기 때문에 에러가 뜨지도 않아 규모가 큰 프로그램에서는 문제를 찾기가 힘듦.

```python
msg = "Test String"

class Mistake():
    """docstring for Mistake"""
    msg = ""
    def set(self, msg):
        self.msg = msg
    def make_mistake(self):
        print(msg)
        # print(self.msg)  # self 를 명시해야 원하는 값을 출력

m = Mistake()
m.set("This is Test Message!")
m.make_mistake()

### result:
# Test String
```

------

## 네임스페이스
클래스 객체(Class Object)와 인스턴스 객체(Instance Object)의 네임스페이스는 다른 영역. 기본적으로 아래와 같은 순서로 변수나 메서드 이름을 찾음. `LGB Rule` 과 유사한 방식.

1. 인스턴스 객체 영역
2. 클래스 객체 영역
3. 전역 영역

위의 과정을 거친 후에도 찾지 못할 경우 `AttributeError` 예외가 발생.

```python
class Person():  # 클래스 정의
    """docstring for Person"""  # 클래스에 대한 설명, help(클래스이름()) 입력시 나타남.

    name = "Default"  # 멤버 변수

    def __init__(self):  # 생성자
        super(Person, self).__init__()

    def who_am_i(self):  # 멤버 메서드
        print("I am {0}".format(self.name))

me = Person()
you = Person()

Person.age = 20  # Person 클래스에 age 변수 추가

me.name = "CHANN"
me.age = 26
me.job = "developer"  # 인스턴스에 job 변수 추가

me.who_am_i()
print("age: ", me.age)  # 모든 인스턴스에서 사용 가능
print(me.job)  # 해당 인스턴스에서만 사용 가능

you.who_am_i()
print("age: ", you.age)  # 모든 인스턴스에서 사용 가능
```

------

## 생성자, 소멸자
파이썬은 C++ 나 Java 와 마찬가지로 생성자, 소멸자 메서드를 지원함. 생성자는 인스턴스 객체가 생성될 때 자동으로 호출되며, 소멸자는 인스턴스 객체의 레퍼런스 카운터가 0이 될 때 호출됨. 생성자 메서드와 소멸자 메서드는 각각 `__init__()` 과 `__del__()` 로 미리 정의되어 있음. 파이썬에서 앞뒤로 언더바(__) 2개가 있는 것은 특별한 용도로 미리 정의된 것들임. 생성자 메서드의 경우 인스턴스 객체 생성 시 초기화할 멤버 변수값을 전달할 수 있음.

```python
class student:
    """docstring for student"""
    def __init__(self, arg):
        super(student, self).__init__()
        self.arg = arg
        print("생성자! value:", arg)

    def __del__(self):
        print("소멸자!")

def test():
    s = student(10)

test()
### result:
# 생성자! value: 10
# 소멸자!
```

함수 내부에서 생성할 경우 함수 블록을 벗어났을 떄 자동으로 소멸자가 호출되고 소멸됨. 아래와 같이 명시적으로 `del` 구문을 사용한다고 소멸자가 항상 호출되는 것은 아님. 레퍼런스 카운터가 1 이상일 경우 `del` 구문을 사용해도 소멸자가 호출되지 않음.

```python
class test:
    """docstring for test"""
    def __init__(self):
        print("생성자!")

    def __del__(self):
        print("소멸자!")

a = test()
b = a
c = b

del c
# del b
# del a
print("END")

### result:
# 생성자!
# END  # del 해도 소멸자가 호출되지 않음
# 소멸자!  # 프로그램 종료해서 소멸자가 호출됨
```

------

## 정적 메서드, 클래스 메서드
메서드의 확장 형태로 정적 메서드(Static Method)와 클래스 메서드(Class Method)가 있음. 정적 메서드는 인스턴스 객체 없이 클래스를 통해 직접 호출할 수 있는 메서드임. 이 경우 메서드를 정의할 때 인스턴스 객체를 참조하는 'self' 인자를 선언하지 않음.

인스턴스의 갯수를 관리하고 싶은 경우엔 클래스 영역에서 해당 정보를 관리하는 것이 효율적.

```python
class student(object):
    s_count = 0
    def __init__(self):
        student.s_count += 1  # 인스턴스 객체 갯수 증가
    def print_count():
        print("instance:", student.s_count)

a = student()
b = student()
c = student()

student.print_count()  # 인스턴스 갯수 출력
# a.print_count()  # 에러: 암묵적으로 인스턴스 객체를 받기 때문

### result:
# instance: 3
```

------

정적 메서드와 클래스 메서드의 비교 예시는 아래와 같음.

```python
class student():
    s_count = 0
    def __init__(self):
        student.s_count += 1

    def s_method():  # 정적 메서드 정의
        print("static method:", student.s_count)
    print_s_count = staticmethod(s_method)  # 정적 메서드 등록

    def c_method(self):  # 클래스 메서드 정의, 첫 인자로 클래스를 받음
        print("class method:", self.s_count)
    print_c_count = classmethod(c_method)  # 클래스 메서드 등록


a = student()
b = student()
c = student()

student.s_method()
a.print_s_count()

student.c_method(c)
b.print_c_count()

### result:
# static method: 3
# static method: 3
# class method: 3
# class method: 3
```

------

인스턴스 카운터와 같은 용도의 변수는 외부에서 값이 변경되어선 안됨. 파이썬에서는 이름 변경(Name Mangling) 으로 대처함. 앞에 '__'로 시작하는 변수나 메서드의 경우 클래스 외부에서 참조할 때 명시하는 변수명이 자동적으로 `_[클래스이름]__[멤버이름]` 으로 변경됨. 클래스 내에서는 정의한 이름 그대로 `__[멤버이름]` 만으로 사용할 수 있음.

이렇게 하는 경우는 파이썬 문법의 제약사항으로 정보은닉을 제공하기보다는 이름 변경으로 개발자의 의도를 나타낸 것. 그러므로 외부에서 변경된 이름으로 변수 접근 및 사용을 권장하지 않음.

```python
class student():
    __s_count = 0
# ...중략

a = student()

print(student._student__s_count)  # 외부 참조시 명시하는 이름이 변경됨.
print(dir(student))

### result:
# 1
# [(..중략..) '_student__s_count', 'c_method', (..중략..)]  # 실제 이름이 저렇게 등록되어있음을 확인.
```

------

## 연산자 중복 정의
연산자 중복(Operator Overriding)은 아래와 같은 메서드들을 활용하여 정의함. 자세한 건 [공식 문서](https://docs.python.org/3.5/reference/datamodel.html#emulating-numeric-types)를 참고.

```python
def __add__(self, other):  # 더하기(+)
def __sub__(self, other):  # 빼기(-)
def __mul__(self, other):  # 곱하기(*)
def __truediv__(self, other):  # 나누기(/)
def __floordiv__(self, other):  # 나누기 몫만(//)
def __mod__(self, other):  # 나누기 나머지만(%)
def __divmod__(self, other):  # divmod()
def __pow__(self, other):  # pow(), **
def __lshift__(self, other):  # <<
def __rshift__(self, other):  # >>
def __and__(self, other):  # &
def __or__(self, other):  # |
def __xor__(self, other):  # ^
def __abs__(self):  # abs()
def __pos__(self):  # 더하기(+, 단항)
def __neg__(self):  # 빼기(-, 단항)
def __invert__(self):  # ~(비트연산)
...중략
```

------

연산자 중복 예시는 다음과 같음.

```python
class student(object):
    name = ""
    """docstring for student"""
    def __init__(self, arg=None):
        self.name = arg
    def __sub__(self, string):
        for i in string:
            self.name = self.name.replace(i, "")
        return student(self.name)
    def __abs__(self):
        return student(self.name.upper())
    def s_print(self):
        print(self.name)


a = student("Heechan.B")
a -= ".B"
a.s_print()
a = abs(a)
a.s_print()

### result:
# Heechan
# HEECHAN
```

------

## 상속
부모클래스의 모든 변수, 메서드를 자식클래스로 물려줄 수 있음. 여러 클래스의 공통된 속성은 부모 클래스에서 정의를 하고, 각 자식 클래스(하위 클래스)에서는 각각 용도에 걸맞은 변수, 메서드를 구현하면 됨. 이러한 개념은 같은 코드의 반복을 방지하고 유지보수가 용이해짐. 예시는 아래와 같음.

```python
class car:
    """
    자동차 부모클래스
    변수:
        차명
        가격
        연비

    출처: http://auto.naver.com

    ----------------------------------------------------------------------
    """
    name = None
    price = None
    fuel = None

    def __init__(self, *arg):
        super(car, self).__init__()
        if len(arg) == 3:
            self.name = arg[0]
            self.price = arg[1]
            self.fuel = arg[2]
        elif len(arg) == 2:
            self.name = arg[0]
            self.price = arg[1]
        elif len(arg) == 1:
            self.name = arg[0]

    def print_info(self):
        """차 정보를 출력. Name, Price, Fuel."""
        print("Info(Name={0}, Price={1}, Fuel={2})".format(self.name, self.price, self.fuel))

class kia(car):
    """
    자동차 자식클래스
    변수:
        차명
        가격
        연비
        회사명
    """
    def __init__(self, name, price, fuel, company):
        super(kia, self).__init__()
        self.name = name
        self.price = price
        self.fuel = fuel
        self.company = company  # 자식클래스의 확장 변수

    def print_info(self):  # 다형성, 메서드 재정의(확장)
        """차 정보를 출력. Name, Price, Fuel, Company."""
        print("Info(Name={0}, Price={1}, Fuel={2}, Company={3})".format(self.name, self.price, self.fuel, self.company))

# 부릉이 자동차(부모)
broong = car("Broong", 2000, "13km/L")
broong.print_info()

# 기아 레이 자동차(자식)
ray = kia("Ray", 1800, "13.2km/L", "KIA Motors")
ray.print_info()

# 클래스 간의 관계 확인, issubclass(자식, 부모)
print("kia: child, car: parent ---", issubclass(kia, car))
print("kia: parent, car: child ---", issubclass(car, kia))

# 부모클래스 추적
print("What is kia parent? ", kia.__bases__)
```

------

## 상속과 네임스페이스
클래스 상속의 스코핑 룰(Scoping Rule)은 아래와 같음.

1. 인스턴스 객체 영역
2. 클래스 객체 영역
3. 전역 영역

------

여기서 클래스간의 상속 관계가 포함되면 아래와 같이 규칙이 확장됨. 이러한 규칙을 상속 관계 검색의 원칙(Principles of Inheritance Search)이라고 함.

1. 인스턴스 객체 영역
2. 클래스 객체 상속 영역(자식 -> 부모 순으로 탐색)
3. 전역 영역

이렇게 하는 이유는 중복 변수와 메서드를 최소화하여 메모리 효율을 높이기 위함.

------

## 다중 상속
다중상속은 2개 이상의 클래스를 상속받는 경우를 말함. 두 클래스의 속성을 물려받게 됨. 상속 정보는 MRO(Method Resolution Order)에 저장되어 있으며,  `__mro__()` 를 이용해서 조회 가능.

```python
class person:  # 사람
    name = None
    def __init__(self, name):
        print("person 호출")
        self.name = name

class girl(person):  # 여자
    def __init__(self, name, gender):
        person.__init__(self, name)  # 사람 생성자 호출
        print("girl 호출")
        self.gender = gender  # 확장 변수 추가

class girlfriend(girl):  # 여자친구
    def __init__(self, name, gender, pretty):
        girl.__init__(self, name, gender)  # 사람 생성자 호출
        print(">> girlfriend 호출")
        self.pretty = pretty  # person -> girl -> girlfriend 로 다중 상속 후 확장 변수 추가

    def print_all(self):  # 다중상속 후 확장 메서드 추가
        print("Name: {0}, Gender: {1}, is_pretty?: {2}".format(self.name, self.gender, self.pretty))

class boy(person):
    def __init__(self, name, gender):
        person.__init__(self, name)  # 사람 생성자 호출
        print("boy 호출")
        self.gender = gender

class boyfriend(boy):
    def __init__(self, name, gender, pretty):
        boy.__init__(self, name, gender)
        girlfriend.__init__(self, name, gender, pretty)
        print(">> boyfriend 호출")
    def print_all(self):
        print("Name: {0}, Gender: {1}, is_pretty?: {2}".format(self.name, self.gender, self.pretty))

b = girlfriend("IU", "F", 1)
print()

c = boyfriend("Jongsuk", "M", 1)
print()

b.print_all()
c.print_all()
print()

print("What is girlfriend parent? ", girlfriend.__bases__)  # (<class '__main__.girl'>,)
for i in girlfriend.__mro__:
    print(i)

### result:
# person 호출
# girl 호출
# >> girlfriend 호출

# person 호출  --> 1번 호출
# boy 호출
# person 호출  --> 2번 호출됨 <<
# girl 호출
# >> girlfriend 호출
# >> boyfriend 호출

# Name: IU, Gender: F, is_pretty?: 1
# Name: Jongsuk, Gender: M, is_pretty?: 1

# What is girlfriend parent?  (<class '__main__.girl'>,)
# <class '__main__.girlfriend'>
# <class '__main__.girl'>
# <class '__main__.person'>
# <class 'object'>

```

------

## super()를 이용한 상위클래스 메서드 호출
위와 같은 코드에서는 *person* 클래스가 두 번 호출되는 문제가 있음. 그 이유는 *boyfriend* 클래스의 생성자에서 *boy* 를 호출했음에도  *girlfriend* 를 호출하면서 *person* 생성자가 **2번 호출되기 때문**. 이러한 문제는 다이아 형태로 상속할 때 발생.

------

이러한 문제는 `super()` 내장함수로 해결 가능하며, 부모 클래스의 객체를 반환하므로 Java의 `super` 나 C# 의 `base` 와 유사함. 일반적으로 자식 클래스에서 `super(클래스 이름, self).__init__()` 와 같이 호출하므로 코드의 유지보수가 쉬움.

------

## 참고
1. [Jump to Python](https://wikidocs.net/28)