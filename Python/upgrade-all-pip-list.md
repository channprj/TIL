Title: 파이썬 패키지 한번에 업그레이드하기
Date: 2016-04-08 21:00
Category: Python
Tags: python, programming, dev, scrpit, pip, regex, package
Slug: upgrade-all-python-packages
Author: CHANN
<!--Summary: -->
[TIL](https://github.com/channprj/TIL)을 운영하면서 [require.io](http://requires.io) 서비스의 뱃지가 *outdated* 라는 영롱한 글자와 함께 노란불이 들어와 있는 것이 영 거슬렸음.

여러가지 방법이 있지만 요약하면 대개 아래와 같음.

1. 쉘 명령어로 해결
2. 파이썬 코드로 해결 (쉘 사용)

------

1번의 경우 `$ pip list --outdated` 라는 쉘 스크립트와 정규표현식을 활용해서 파일을 작성 가능하지만, 쉘 스크립트와 정규표현식은 아직 내공이 좀 부족하여 파이썬으로 해결하기로 함.

그래서 2번의 경우 코드는 아래와 같음. 쉘 명령을 날리는 건 같지만 파이썬 코드로 간단히 해결 가능.

```python
import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)
```

------

## 유의할 점
특정 버전에서만 동작하는 코드를 사용하는데 의존성 여부를 고려하지 않고 무턱대고 버전만 훅훅 올리다가는 훅 가는 수가 있음. 의존성 체크는 다음에 다루기로.

------

## 참고
1. [Stack Overflow의 관련글](http://stackoverflow.com/questions/2720014/upgrading-all-packages-with-pip)