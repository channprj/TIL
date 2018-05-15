Title: 파이썬 코딩 컨벤션
Date: 2016-03-11 14:00
Category: Python
Tags: python, programming, dev, scrpit, function, study, coding style, coding convension, coding standard, 파이썬, 코딩 스타일, 코딩 컨벤션
Slug: coding-convention
Author: CHANN
<!--Summary: -->

<center>![Imgur](https://i.imgur.com/P58yvJI.png)</center>

[코딩 컨벤션(Coding convention)](https://en.wikipedia.org/wiki/Coding_conventions)이란 읽고, 관리하기 쉬운 코드를 작성하기 위한 일종의 코딩 스타일 규약(약속)임.

 대부분의 언어는 대표적인 코딩 컨벤션을 가지고 있고, 일반적으로는 그러한 암묵적인 표준을 따르게 됨. 하지만 프로젝트별, 회사별, 기타 단체마다 각자 다른 규칙을 가짐. 단체에서는 아무리 작은 프로젝트라 하더라도 유지 보수 및 추가 개발 등의 관리를 해야 하기 때문에 코딩 스타일 규약은 반드시 필요.

완벽한 코딩 컨벤션은 없음. 효율성이나 편의성이 확실히 증명되어 채택된 방식이 있을 수도 있지만 대개 취향의 차이임. 그러나 각 언어별 '존잘'~~(존나 잘하는)~~ 분들이 계신데, 대체로 그 분들의 영향력이 많이 끼침. 취향의 차이라서 그런지 서로 많이들 싸우기도 하는데, 대표적인 예로는 아래와 같음.

* 인덴트 2칸 vs 4칸 vs 8칸(...소수)
* 인덴트 Tab vs Space
* 괄호를 어떻게 열고 닫을 것이냐
* 변수나 함수 등 이름짓는 법
* 주석 다는 법
* camelCase vs PascalCase vs snake_case vs hgCase vs ...
* ...

사실 코딩 컨벤션은 취향이지만 종교와도 같은 것이어서 이렇다 할 정답이 없음. 프로그래머 10명 잡고 물어보면 다들 선호하는 코딩 스타일이 다름. 예를 들어 함수이름만 봐도 어떤 프로그래머는 private함수는 getNum() 이란식으로 작성하고 public 함수는 GetNum()이라고 작성하자고 하는 반면 다른 프로그래머는 get_num()과 GetNum()이라고 하자고도 할 것.

단체에서는 일의 효율과 체계를 갖추기 위해 엄격하게 규칙을 정해놓고 프로그래머들에게 강요하지만, 이로 인해 스타일을 바꾸야 하는(개종해야하는) 사람들에게는 오히려 생산성 저하의 요소가 되기도 함.

대표적인 코딩 컨벤션으로는 BSD, K&R, GNU 와 같은 것이 있는데 예시는 아래와 같음.

BSD
```c
if(condition)
{
    statement();
}

```

K&R
```c
if(condition) {
    statement();
}
```

GNU
```c
if(condition)
    {
        statement();
    }
```

------

스크립트 언어들은 다른 고급 언어에 비해 유연한 문법 구조를 가지고 있어 좀 더 엄격한 코딩 스타일 규약이 필요. 코딩 컨벤션은 코딩 스탠다드, 코딩 스타일 가이드 등으로도 불림.

------

## 어떤 규칙을 따라야 하나
개인적으로 제가 코딩 컨벤션을 정하는 방법은 아래와 같음.
~~... 회사에선 높은 사람이 시키는대로...~~

1. 창시자가 시키는대로 하기
1. 존잘러 구글의 권장사항을 참고
1. 기타 존잘러의 의견을 참고
1. 커뮤니티와 통계를 참고

### 그럼 파이썬에서는
우선, 파이썬은 주로 스네이크 표기법을 따름. ~~(파이썬이 도마뱀이니 뱀 표기법을...)~~ 그리고 앞서 말씀드린 바와 같이 창시자, 존잘러 구글, 기타 존잘러, 커뮤니티와 통계 순으로 내용을 다룰 예정.

#### 창시자의 권장사항
> PEP 8 is pretty much "the root" of all common style guides.

PEP 8은 파이썬에서 광영높으신 최고존엄 **귀도 반 로썸** 형님이 작성하신 PEP(Python Enhance Proposal)에 작성하신 권장사항. PEP란 파이썬을 개선하기 위한 개선 제안서를 뜻하는 것으로 3가지로 구분됩니다.

* Standard Track : 파이썬의 새로운 기능이나 구현을 제안
* Informational : 파이썬의 디자인 이슈나 일반적인 지침을 제안
* Process : 파이썬 커뮤니티에 정보를 제안

이들 PEP 제안 중에서 PEP8은 파이썬 코딩 스타일 가이드라인을 의미하며 파이썬 커뮤니티에 정보를 제안하는 Process에 해당함. 이러한 PEP8(파이썬 코딩 스타일 가이드라인)의 대표적인 사항을 요약하면 아래와 같음.

1. 들여쓰기는 공백 4개
1. 한 줄의 최대 글자는 79자
1. 파일은 UTF-8 또는 ASCII로 인코딩
1. 하나의 import에는 모듈 하나만 하기
1. import는 표준 라이브러리, 서드파티, 로컬 라이브러리 순서로 묶기
1. 소괄호 안, 중괄호 안, 대괄호 안, 쉼표, 콜론과 세미콜론 앞에 추가로 공백을 입력하지 말기
1. 키워드 인자와 인자의 기본값(default parameter value)의 = 는 붙여 쓰기
1. 불필요한 주석은 달지 말기, 한 줄 주석은 신중하게 달기
1. 불린형(boolean)의 값을 조건문에서 ==를 통해 비교하지 말기
1. ...

파이썬의 대표적이고 기본적인 가이드라인이니만큼 규칙만 빽빽할 것 같지만, PEP 8는 서두부터 예외를 언급한 섹션이 있음.

> A Foolish Consistency is the Hobgoblin of Little Minds. 

멍청하게 일관성을 유지하는 것은 소인배(홉 고블린...)의 발상.

> A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is most important.

스타일 가이드는 일관성(consistency)에 관한 것. 이 스타일 가이드의 일관성은 중요. 하지만 프로젝트의 일관성은 더욱 중요하며, 하나의 모듈이나 함수의 일관성은 더더욱 중요함.

> But most importantly: know when to be inconsistent – sometimes the style guide just doesn’t apply. When in doubt, use your best judgment. Look at other examples and decide what looks best. And don’t hesitate to ask!

하지만 가장 중요한 건 언제 이것을 어길지 아는 것. – 때때로 스타일 가이드는 적용되지 않음. 의심이 들 때는 여러분의 최선의 판단을 따라야. 다른 예제를 보고 어느 게 제일 나은지 고르기. 그릭호 언제든 질문하기!

> Two good reasons to break a particular rule:
> 
> When applying the rule would make the code less readable, even for someone who is used to reading code that follows the rules.
To be consistent with surrounding code that also breaks it (maybe for historic reasons) – although this is also an opportunity to clean up someone else’s mess (in true XP style).

다음은 규칙들을 어기는 2가지 좋은 예외 사항.

규칙을 적용한 코드가 (규칙을 숙지한 사람 눈에도) 읽기 어려운 경우.
일관성을 지키려고 한 수정이 다른 규칙을 어기는 경우(아마도 역사적인 이유).

기타 자세한 세부규칙은 아래의 참고 링크에서 확인 가능. 영어가 살짝 귀찮으시다면 [번역된 버전](http://kenial.tistory.com/902)도 있음. [번역 및 요약된 버전](http://spoqa.github.io/2012/08/03/about-python-coding-convention.html)도 있으니 참고.

------

#### 구글의 권장사항
최고존엄 귀도 반 로썸 형님이 구글에 계시므로, PEP8과 구글의 스타일 가이드가 크게 다르진 않은데, [이러한 식](https://github.com/google/yapf/blob/master/yapf/yapflib/style.py#L119)으로 조금 다름. 

idiosyncratic (the two-space indents instead of the popular four-space ones, and the CamelCase style for functions and methods instead of the camel_case style, are pretty major idiosyncrasies).


이것 역시 자세한 건 직접 확인을 해야.

------

#### 커뮤니티와 통계
[2014-07-19 통계](http://sideeffect.kr/popularconvention#python)를 요약하자면 아래와 같음.

* 스페이스 4칸 사용 : 94.86%
* 줄 길이가 80자 이내 : 93.05%
* import를 다른 라인에 명시 : 96.06%
* 괄호에 추가적인 빈칸 사용하지 않기 : 79.83%

다수가 사용하는 방식을 채택하는 것 또한 나쁘지 않다고 봄. 협업하는 데엔 도움이 많이 될 것.

------

## 참고
1. [PEP8 by Guido van Rossum](http://legacy.python.org/dev/peps/pep-0008/)
1. [PEP8의 한글 번역](http://kenial.tistory.com/902)
1. [PEP8의 한글 번역 2](http://coreapython.hosting.paran.com/etc/CS%2011%20Python%20track%20coding%20style%20guide.htm)
1. [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
1. [Popular Coding Convention on Github](http://sideeffect.kr/popularconvention#python)
1. [파이썬 코딩 컨벤션 - Spoqa 기술 블로그](http://spoqa.github.io/2012/08/03/about-python-coding-convention.html)
1. [NULI NAVER 코딩컨벤션](http://nuli.navercorp.com/sharing/fe/coding)
1. [hanul93님 블로그](http://www.hanul93.com/kicomav-pep8/)
1. [홍민희님 블로그](http://blog.dahlia.kr/post/18035893350)
1. [포프님 블로그](http://www.gamedevforever.com/116)
1. [melange 스타일 가이드](https://code.google.com/p/soc/wiki/PythonStyleGuide)
1. [ukupat의 Tab or Space](https://ukupat.github.io/tabs-or-spaces/)
