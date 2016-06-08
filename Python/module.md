Title: 파이썬 모듈
Date: 2016-06-06 18:00
Category: Python
Tags: python, programming, dev, scrpit, function, study, module, oop, 파이썬, 프로그래밍, 개발, 스크립트, 함수, 공부, 스터디, 모듈, 객체지향
Slug: module
Author: CHANN
<!--Summary: -->
모듈은 특정 기능을 담당하는 코드모음으로, 함수나 변수 또는 클래스 들을 모아 놓은 파일임. 프로그램에서 불러와 사용할수 있게끔 만들어진 파이썬 파일이라고도 할 수 있음. 이미 만들어 놓은 모듈을 사용할 수도 있고 직접 만들어서 사용할 수도 있음.

```python
import math  # math 모듈을 불러옴

print(math.pi)  # math 모듈의 pi 사용
print(math.pow(2,10))  # math 모듈의 pow() 사용

### result:
# 3.141592653589793
# 1024.0
```

------

## 장점
- 코드의 재사용
- 네임스페이스 분리
- 가독성 향상 및 관리 용이

------

## 생성
`모듈이름.py` 로 파이썬 파일을 만들고 안에 변수, 메서드 등을 구현. 해당 파일을  `~/.pyenv/versions/project/lib/python3.4/site-packages` 와 같이, 사용하고 있는 파이썬 버전의 라이브러리 폴더나 패키지 폴더에 넣어주면 됨. 그리고 아래와 같이 임포트를 해서 테스트를 해볼 수 있음.

```python
>>> import test
>>> test.print_test()
This is TEST!
```

------

## 위치
아래와 같은 순서로 모듈을 탐색함.

1. 현재 작업 폴더
2. 환경변수에 등록된 위치
3. 표준 라이브러리 폴더

표준 라이브러리 폴더의 위치는 아래와 같이 확인 가능.

```python
>>> import sys
>>> sys.path
['', '/Users/CHANN/.pyenv/versions/3.4.2/lib/python34.zip', '/Users/CHANN/.pyenv/versions/3.4.2/lib/python3.4', '/Users/CHANN/.pyenv/versions/3.4.2/lib/python3.4/plat-darwin', '/Users/CHANN/.pyenv/versions/3.4.2/lib/python3.4/lib-dynload', '/Users/CHANN/.pyenv/versions/pelican/lib/python3.4/site-packages']

### 아래와 같이 경로를 추가해 줄 수 있음
>>> sys.path.append('~/my_module/')
```

------

### 임포트
기존의 `import` 구문을 사용 가능. 그러나 `from 모듈 import 애트리뷰트` 와 같이 사용할 경우 `모듈이름.애트리뷰트이름` 와 같이 사용하지 않고, 단순히 애트리뷰트 이름만 가지고 사용 가능함. 하지만 새로 임포트 되는 이름이 이미 사용중일땐 오버라이딩(덮어쓰기)되므로 주의해야.

`import 모듈 as 별칭`

위와 같이 모듈 이름을 별칭으로 바꾸어 사용 가능하나 가급적 사용을 피해야.

------

### 임포트 작업
모듈을 임포트하면 `sys.path` 에서 모듈을 찾기 시작함. 이 과정에서 모듈의 바이트코드(*.pyc)가 있을 경우 이를 바로 임포트하고, 없을 경우 인터프리터로 바이트코드를 생성하여 임포트. 바이트코드는 모듈이 임포트될 때 바로 메모리에 로드되므로 속도가 빠름. 

한번 로딩한 모듈은 중간에 모듈이 수정된다 해도 수정사항이 반영되지 않음. 프로그램이나 파이썬을 재부팅해야 수정사항이 반영됨. 하지만 매번 앱을 껐다 켤 수는 없으니 임포트된 모듈을 다시 임포트하면 됨. 명령어는 아래와 같음

```python
import imp
import overwatch
imp.reload(overwatch)
```

------

### `if __name__ == "__main__":`
모듈을 임포트해서 사용할 수도 있지만 직접 실행할 수도 있음. `__name__` 이라는 애트리뷰트를 통해 임포트 했을 때와 실행했을 때를 각각 다르게 동작하도록 설정 가능. 모듈 실행 시 별도의 테스트코드가 자동으로 동작하도록 하는 데 쓰이기도 함.

------

### 패키지
패키지는 여러 개의 모듈을 묶은 것. 패키지에서는 `__init__.py` 로 패키지를 초기화해야. 패키지를 사용할 때 주의해야 할 점으로는 해당 패키지의 하위 패키지가 자동으로 임포트되지 않는다는 점. 패키지 안의 패키지 모듈을 참조하려면 `from 패키지 import 하위패키지` 와 같은 형태로 명시해야.

아래와 같이 상대경로도 사용 가능.

```python
from . import 모듈
from .. import 상위폴더모듈
from ..car import tesla  # 부모 디렉토리 모듈 중 car의 tesla 모듈을 임포트
```

------

## 참고
1. [Wikidocs - Module](https://wikidocs.net/29)