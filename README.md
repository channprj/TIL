[![Build Status](https://travis-ci.org/channprj/TIL.svg?branch=master)](https://travis-ci.org/channprj/TIL)
[![Requirements Status](https://requires.io/github/channprj/TIL/requirements.svg?branch=generator)](https://requires.io/github/channprj/TIL/requirements/?branch=generator)
# Today I Learned
오늘 배운 내용을 정리하는 곳입니다.

*Read this in other languages: [English](https://github.com/channprj/TIL/blob/master/README-en.md)*

## 규칙
* 폴더와 문서의 이름은 기본적으로 영문
* 문서는 [Github-Flavoured Markdown](https://guides.github.com/features/mastering-markdown/)으로 작성
* 표현은 간결하게 짧은 문장 위주
* Python 기반의 [Pelican](https://github.com/getpelican/pelican)을 이용하여 Github Pages를 생성
* Travis-CI 로 동기화되어 자동으로 [Today I Learned 사이트](https://til.chann.kr)에 반영됨

## 방식
> Github 에서는 마크다운 문서를 먼저 볼 수 있도록 하고, 동시에 Github Pages 로 배포하여 웹으로도 볼 수 있도록 하기

<p align="center">
<img src="https://raw.githubusercontent.com/channprj/TIL/generator/content/images/TIL-Workflow.png">
</p>
* `TIL/contents/posts/` (마크다운 문서)만 저장하는 **master** 브랜치
* Python 기반의 정적 페이지 생성기인 Pelican 전체를 저장하는 **generator** 브랜치
* **generator** 브랜치로 생성한 HTML 문서를 **gh-pages** 브랜치에 저장하여 웹으로 배포
* 이러한 환경을 구성하게 된 계기는 [블로그(글 작성중)](https://blog.chann.kr/) 참고.

## 기타
:electric_plug: [Source](https://github.com/channprj/TIL)
:memo: [Web](https://til.chann.kr)

<p align="right">
Influenced by <a href="https://github.com/thoughtbot/til">Thoughtbot</a>, <a href="https://github.com/jbranchaud/til">jbranchaud</a>, <a href="https://github.com/milooy/TIL">milooy</a>, <a href="https://github.com/ahastudio/til">ahastudio</a>
</p>
