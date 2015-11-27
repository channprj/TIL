Title: Python, Django 등의 작업환경 설정하기
Slug: django-python-initial-setting
Date: 2015-10-13 00:00
Category: Project
Tags: ku, django, python, init
Author: CHANN
Summary: 졸업프로젝트 임시 기록용.


> 작성중
> 
> 이 글은 개인 기록용으로, 다소 불친절할 수 있습니다.

## OS X에서 Python 설치하기
ruby 기반의 패키지관리 툴인 brew를 사용해서 Python을 설치하자.  

```shell
$ brew update
$ brew doctor
$ brew install python
$ sudo easy_install pip
$ brew install pyenv
```

[Github pyenv 저장소](https://github.com/yyuu/pyenv) 의 설명을 잘 보고 따라해야 한다. 나는 bash가 아닌 zshell을 사용하므로 `.zshrc` 파일을 수정해주었다. 영어로 되어있지만 어려운 내용은 없으니 그냥 시키는대로 하면 된다.  

제대로 설정이 되었는지 확인해보자.

```shell
CHANN@CHANN-Macbook:~ » python
Python 3.4.0 (default, Oct 26 2015, 06:24:28)
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.1.76)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
CHANN@CHANN-Macbook:~ »
```

------

## python, parser, virtualenv 등 세팅
```shell
$ pip install beautifulsoup4
$ pip install lxml
$ pip install requests
$ brew install pyenv-virtualenv
$ brew install autoenv
```

------

## Django 설치
```shell
$ pyenv virtualenv 3.4.2 kusle-3.4.2
$ pyenv shell kusle-3.4.2
$ pip install django==1.8.6
$ django-admin startproject kusle .
```

그럼 아래와 같은 구조의 폴더가 생성된다.

```shell
kusle
├── __init__.py
├── settings.py
├── urls.py
└── wsgi.py
```

wsgi는 웹 서버 게이트웨이 인터페이스(WSGI, Web Server Gateway Interface)는 웹서버와 웹 애플리케이션의 인터페이스를 위한 파이썬 프레임워크다. Low-Level로 작성되어 웹서버와 웹 어플리케션, 프레임워크간의 벽을 허물었다.

웹 어플리케이션 개발이 목적이므로, 기본적으로는 HTTP의 요청을 받아 응답을 돌려주어야 한다. 이러한 처리는 1차적으로 nginx를 통해 이뤄지는데, uwsgi라는 데몬을 사용하여 서버사이드를 처리할 예정이다.

------

### uwsgi 설치
uwsgi의 역할은 아래와 같다.  
client <-> the web server <-> the socket <-> uwsgi <-> Django

`pip` 를 통해 아래와 같이 `uwsgi` 를 설치하자.

```shell
$ pip install uwsgi
$ mkdir /usr/local/etc/uwsgi/
```

근데 `uwsgi ` 명령어가 자꾸 에러를 뿜는다. 중국 형님들 블로그에서 힌트를 얻어 아래와 같은 방법으로 해결을 했다. linuxbrew를 사용해서 겪는 삽질일지도 모르겠다.<br/>
`sudo ln -s /home/사용자/.linuxbrew/lib/libpcre.so.1 /lib`

이후에 다음과 같이 테스트해보자

```shell
$ uwsgi --http :8000 --module kusle.wsgi
```

그럼 장고 welcome 페이지가 뜰 것이다. 이제 nginx 와 연동을 하자.


```shell
    ################# uWSGI configuration #################

    event = epoll
    ssl = True
    plugin_dir = .
    timer = timerfd
    capabilities = False
    yaml = embedded
    pcre = True
    filemonitor = inotify
    malloc = libc
    zlib = True
    execinfo = False
    json = False
    ifaddrs = True
    xml = expat
    routing = True
    locking = pthread_mutex
    kernel = Linux
    debug = False

    ############## end of uWSGI configuration #############
    total build time: 24 seconds
    *** uWSGI is ready, launch it with /home/kusle/.pyenv/versions/kusle-3.4.2/bin/uwsgi ***
```

```ini
# uwsgi.ini
[uwsgi]
# the base directory (full path)
base            = /home/kusle/django
project         = kusle

chdir           = %(base)

# the virtualenv (full path)
home            = /home/kusle/.pyenv/versions/kusle-3.4.2

# test...
# projectdomain = kusle.kuple.kr
# protocol = uwsgi
# daemonize = /home/kusle/django/log/kusle.log

# Django's wsgi file
module          = kusle.wsgi

# the socket (use the full path to be safe
socket          = kusle.sock

######

# process-related settings
master          = true

# maximum number of worker processes
processes       = 10

# ... with appropriate permissions - may be needed
# chmod-socket    = 664

# clear environment on exit
# vacuum          = true
```

마스터로 계속 돌아가는 uwsgi를 멈추는 방법은 `killall -s INT uwsgi`명령어를 사용하면 된다.

------

## 자동으로 uWSGI 실행되도록 설정

```
description "uWSGI server instance configured to serve my project"

start on runlevel [2345]
stop on runlevel [!2345]

setuid kusle
setgid www-data

env PATH=/home/kusle/django/myprojectenv/bin
chdir /home/kusle/django
exec uwsgi --http :8000 kusle.ini
```

------

## MariaDB 설정
Django는 기본설정으로 Sqlite3를 사용한다. 하지만 이번 프로젝트에서는 새롭게 DB를 구축하는 것 이외에 기존의 DB를 활용하는 방안도 고려중이므로, 되도록이면 같은 DB를 사용하는 것이 나을 것 같다는 판단을 하였다.

먼저, DB를 새롭게 생성하자. 먼저, `$ mysql -u root -p`를 통해 mariadb 콘솔로 접속한다.

```sql
mysql> create user django;
Query OK, 0 rows affected (0.00 sec)

mysql> create user django@localhost identified by '{비밀번호}';
Query OK, 0 rows affected (0.01 sec)

mysql> grant all privileges on django.* to django@localhost;
Query OK, 0 rows affected (0.00 sec)

mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)
```

settings.py에 그대로 드러나는 DB명, 아이디, 암호를 감추어야 하는데, 이것은 쉘 변수를 활용하면 된다. settings.py는 `import os`를 하므로 쉘 변수를 그대로 불러올 수 있다.

.bashrc 또는 .zshrc 등의 쉘 환경설정 파일에 다음과 같이 추가한다

```shell
export DB_NAME="DB이름"
export DB_ID="DB 계정 아이디"
export DB_PW="DB 계정 암호"
```

그리고 settings.py의 DB 관련 코드를 아래와 같이 수정한다.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ["DB_NAME"],
        'USER': os.environ["DB_ID"],
        'PASSWORD': os.environ["DB_PW"],
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

설치를 완료했으면 DB 연동이 제대로 되었는지 테스트를 해보자.

```shell
$ ./manage.py collectstatic
```
------

## 최종 트리
```shell
django
├── 3.4.2
│   ├── bin
│   ├── lib
│   └── local
├── 404.htm
├── 50x.htm
├── db-parsing
│   ├── bs4_test2.py
│   ├── bs4_test3.py
│   └── bs4_test.py
├── index.html
├── kusle
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── wsgi.py.original
├── kusle.sock
├── log
│   └── kusle.log
├── manage.py
├── README.md
├── requirements.txt
├── static
│   └── admin
├── test.py
├── uwsgi.ini
└── versions
    ├── bin
    ├── lib
    └── local
```


------

## 참고
1. [Digital Ocean의 uWSGI, Nginx 관련글](https://www.digitalocean.com/community/tutorials/how-to-deploy-python-wsgi-applications-using-uwsgi-web-server-with-nginx)
2. [위키피디아 wsgi 관련글](https://ko.wikipedia.org/wiki/웹_서버_게이트웨이_인터페이스)
3. [코딩도장의 uwsgi 관련글](http://codingdojang.com/scode/364)
4. [uWSGI Docs](http://uwsgi-docs.readthedocs.org/en/latest/tutorials/Django_and_nginx.html)
5. [link2me님 블로그의 DB 관련글](http://link2me.tistory.com/431)
6. [Django DB 관련 공식 문서](https://docs.djangoproject.com/en/1.8/ref/databases/)
7. [Digital Ocean의 MariaDB, Django 관련글](https://www.digitalocean.com/community/tutorials/how-to-use-mysql-or-mariadb-with-your-django-application-on-ubuntu-14-04)
8. [용이님 블로그의 관련글](http://knot.tistory.com/97)
9. [uwsgi 공식 문서](http://uwsgi-docs.readthedocs.org/en/latest/Install.html)
10. [코딩도장의 django 관련글](http://codingdojang.com/scode/373)
11. [gatsby님 블로그의 관련글](http://software-engineer.gatsbylee.com/uwsgi란-무엇인가-어떻게-사용해야-하는가/)
12. [djangogirls 홈페이지](http://tutorial.djangogirls.org/ko/django_models/index.html)
13. [hannal님 블로그](http://blog.hannal.com)