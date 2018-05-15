Title: 파이썬 단위 테스트
Date: 2016-07-02 19:00
Category: Python
Tags: python, programming, dev, scrpit, study, unittest, test, 파이썬, 프로그래밍, 개발, 스크립트, 공부, 스터디, 단위테스트, 유닛테스트
Slug: unit_test
Author: CHANN
<!--Summary: -->
파이썬은 기본적으로 제공하는 unittest(PyUnit) 모듈에서 단위 테스트를 지원. 어떤 모듈이나 함수를 작성할때 정상 작동여부를 테스트하는 과정을 거치는데, 단위 테스트를 사용하면 코드가 수정되어도 테스트를 동일하게 돌려볼 수 있음.

간단한 테스트 작성법은 아래와 같음.

```python
"""
unittest is the batteries-included test module in the Python standard library. Its API will be familiar to anyone who has used any of the JUnit/nUnit/CppUnit series of tools.
"""
import unittest

def add_one(x):
    return x + 1

# testing def have to start with 'test' word
class Test_01(unittest.TestCase):
    def test(self):
        self.assertEqual(add_one(3), 5, msg="Wrong!")
        self.assertEqual(add_one(3), 4)

# if tests are correct, return .(dot). otherwise, it returns F.
class Test_02(unittest.TestCase):
    def test(self):
        self.assertEqual(add_one(4), 5)
        self.assertEqual(add_one(4), 5)

# Run Unit test
unittest.main()

"""Result:
F.
======================================================================
FAIL: test (__main__.Test_01)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/CHANN/git/cs-basics/test/python/unit_test.py", line 12, in test
    self.assertEqual(add_one(3), 5, msg="Wrong!")
AssertionError: 4 != 5 : Wrong!

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
"""
```

------

## 주로 쓰는 함수
* assertEqual(A, B, msg='') : A와 B가 같은지 테스트, 같지 않은 경우 테스트가 실패하며 msg를 출력.
* assertNotEqual(A, B, msg='') : A와 B가 다른지 테스트, 같은 경우 테스트가 실패하며 msg를 출력.
* assertTrue(A, msg='') : A가 True인지 테스트, False인 경우 테스트가 실패하며 msg를 출력.
* assertFalse(A, msg='') : A가 False인지 테스트, True인 경우 테스트가 실패하며 msg를 출력

------

## 더 나은 방법
```python
import unittest

class myClass:
    def __init__(self):
        self.a = 'a'
        self.b = 'b'
    def doA(self, a):
        self.a = a
        return self.a
    def doB(self, b):
        self.b = b
        return self.b

class testUnit (unittest.TestCase):
    '''
    @brief test case using uniitest.TestCase
    '''
    def setUp(self):
        ''' @brief this method is called before every test methods '''
        pass
    def tearDown(self):
        ''' @brief this method is called after every test methods '''
        pass
    def test001_init(self):
        my = myClass()
        self.assertTrue(my.a == 'a' and my.b == 'b')
    def test002_doA(self):
        my = myClass()
        a = 2
        # my.doA(a)
        self.assertTrue(my.a == a)

if __name__ == '__main__':
    '''
    test_main() 과 같이 테스트 하는 대신
    unittest.main() 으로 호출하여 테스트를 진행하면 전체 OK, Not OK 여부가 나오고
    아래와 같이 두줄을 표시해 주면 상단의 test001_init ... ok, test002_doA ... ok 와 같이 출력됨.
    '''
    suite = unittest.TestLoader().loadTestsFromTestCase(testUnit)
    unittest.TextTestRunner(verbosity=2).run(suite)
```

------

## 참고
1. [파이썬 공식 문서](https://docs.python.org/3/library/test.html?highlight=pyunit)
2. [파이썬 가이드 문서](http://docs.python-guide.org/en/latest/writing/tests/)
3. [Dgoon wiki](http://legacy-wiki.dgoon.net/doku.php?id=python:pyunit)
4. [지훈현서님 블로그](http://egloos.zum.com/mcchae/v/10584377)