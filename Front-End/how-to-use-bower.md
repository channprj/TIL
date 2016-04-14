Title: Bower 사용법
Date: 2016-01-15 20:12
Category: Front-End
Tags: dev, bower, package manager, tool, 개발, 패키지매니져
Slug: how-to-use-bower
Author: CHANN
<!--Summary: -->

[Bower](http://bower.io) 는 웹을 위한 패키지 관리도구다. 트위터에서 개발하였고, 웹 개발시 자주 쓰이는 라이브러리를 쉽고 간편하게 관리할 수 있다. `npm`, `pip`, `gem` 과는 다르게 '웹 패키지 관리도구'라서 특정 언어의 종속성을 가지고 있지 않다. 개인적으로 느낀 장단점은 아래와 같다.

## 장점
* 패키지 설치 및 버전 관리, 의존성 관리 용이
* HTML, CSS, JS, Font, Image 파일 등의 최적화된 패키지

## 단점
* 패키지 설치장소 변경 불가, 패키지 디렉토리가 깔끔하지 않음.  
(예시: ~/project/bower_components/bootstrap/dist/js)
* npm 에 의존적인 패키지 관리자. npm으로 bower를 설치 및 관리해야함.

------

## 사용법
### Bower 설치
아래와 같이 설치한다.

```shell
npm install -g bower
```

------

### 패키지 설치
패키지 설치는 `npm` 등 다른 패키지 관리도구와 비슷하다.

```shell
$ bower install bootstrap
```

----

### 패키지 검색
아래와 같다.

```shell
$ bower search bootstrap  # bootstrap 패키지 전체 검색
$ bower lookup bootstrap  # bootstrap과 일치하는 패키지만 찾기
$ bower info bootstrap  # bootstrap의 버전 정보 확인
```

----

### 패키지 버전, 의존성 관리
`node.js` 에서는 `package.json` 으로 관리하는데, bower에서도 비슷하게 `bower.json` 으로 관리를 한다.

```shell
$ bower init  # bower 패키지 정보를 저장
```

패키지 설치할 때, `--save` 를 뒤에 붙여주면 설치하고 나서 `bower.json`에 자동으로 기록해준다.

----

## 참고
1. [Bower 공식 홈페이지](http://bower.io)
2. [Bower 저장소](https://github.com/bower/bower)
