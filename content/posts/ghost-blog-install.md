Title: ghost 블로그 설치하기
Slug: ghost-blog-install-guide
Date: 2015-12-10 20:00
Category: Dev
Tags: dev, nodejs, ghost, blog, server, package
Author: CHANN
<!--Summary: -->

> ==작성중인 문서입니다.==

----------------------------------------

Ghost는 정말 블로그를 위한 도구다. 마크다운[^n] 기반의 에디터가 기본이며, 별다른 기능이 없다. 그래서 가볍고 빠르다. 마크다운 에디터라서 글 쓰는 속도 또한 빠르고 편리하다. 아직 0.7.x 버전[^n]이라 완성되었다고 보긴 힘들지만, 당장 사용하기에 전혀 무리가 없다. Ghost는 워드프레스가 점점 기능이 많아지면서 무겁고 사용하기 어려워진 것에 반해 오로지 블로그만을 위해 태어났고, 제 역할에만 충실하여 매우 마음에 든다.

Ghost 블로그를 사용하는 방법은 워드프레스와 마찬가지로 2가지이다.

1. [Ghost](http://ghost.org) 호스팅을 이용하는 방법(유료)
2. 직접 서버를 구축해서 설치하여 사용하는 법(사실상 유료)

1번의 경우에는 편리하지만 자유도가 떨어진다. 워드프레스닷컴과 마찬가지로 제공하는 기능만 사용 가능하다는 단점이 있다. 하지만 업데이트가 가장 빠르고, 안정적이다. 사용하려면 [Ghost](http://ghost.org) 홈페이지에 접속해서 회원가입해서 사용하면 된다.

2번의 경우에는 서버를 직접 운영해야 하고 생소할 수 있는 `node.js`를 사용하여 직접 설치해야 하기 때문에 번거롭다. 대신 자유롭게 수정 가능하다는 장점이 있다. 직접 만들기 귀찮으면 1번, 아니면 2번을 고르자.

사실 직접 써 보기 전까진 모르니까 서버에 설치하기 전에 미리 체험을 해 보는 것을 추천한다. 14일 무료체험을 해볼 수 있으니 지금 한번 써보자. 그마저도 귀찮다면 [Ghost 에디터만 사용해보자.](http://ghosditor.herokuapp.com)

----------------------------------------

## 서버 준비
직접 만들기 위해서는 당연히 서버가 있어야 한다. 서버를 구입하거나, 월정액으로 빌려 쓰거나, 자신의 PC를 서버화하거나, Github Page를 이용하는 방법이 있다.

1. AWS, Digital Ocean, Vultr와 같은 가상화 서버를 사용 (시간제 요금, $5 ~)
2. 라즈베리파이2, 오드로이드, 인텔 에디슨과 같은 SBC[^n] 구매 (구입비 $30)
3. 자신의 PC
4. Github Pages 기능을 우회해서 구현

이 글에서 중심적으로 다룰 내용은 1번의 가상화 서버를 활용하는 방법이지만 사실 2, 3번도 크게 상이하진 않다. 운영체제를 설치하고 네트워크를 설정한 이후에는 거의 동일한 과정이라고 볼 수 있다. 4번의 경우엔 무료인 대신 많이 복잡하다. Github Pages 기능은 기본적으로 `Ruby` 기반의 페이지라서 Ghost의 `node.js`를 사용할 수가 없기에 자신의 PC 혹은 노트북에 로컬 서버환경울 구축하고 Ghost를 설치한 후 [Buster](https://github.com/axitkhurana/buster)라는 정적 페이지 생성기를 사용하여 자신의 Github Pages 저장소에 커밋해야 한다. 4번의 경우 나중에 따로 다룰 예정.

우선, 서버를 사자. Cafe24나 스마일서브 같은 국내 가상화서버 혹은 AWS가 가장 좋긴 한데 비싸다. Digital Ocean도 물론 좋지만, 일본지역 서버가 없다. Linode는 일본지역 서버가 있는데 자리가 모두 나가서 새로 서버를 생성할 수가 없다. ~~그러니 Vultr를 사용하도록 하자.~~ ==(2015-12-10) AWS 서버로 이전함.==

----------------------------------------

## Linuxbrew  설치
먼저, ruby 기반 통합 패키지 도구인 `Homebrew`를 설치하자. 맥에서 주로 쓰이는 도구이지만, 리눅스에서도 사용하기 유용하다. apt-get에 비해 패키지 버전이 빠르다. 그러나 서버 전역에서 쓰이는 패키지라면 apt-get으로 설치하는 것이 좀 더 바람직하다. `Homebrew`는 루트 권한으로 패키지 설치가 안 되기 때문. 리눅스에서는 `Linuxbrew` 라는 별칭으로 불린다.

ruby 기반이기 때문에 서버에 당연히 ruby가 설치되어 있어야 한다.

----------------------------------------

### AWS를 이용할 경우
> 우분투 저장소 업데이트는 해당되는 사람만 진행하자.

AWS에서 제공하는 패키지 저장소 문제인지 `apt-get install` 이 안 되더라. 아직은 일본 노드를 사용하고 있으므로 일본 저장소를 추가하려 했으나... 안 된다. 한국 저장소 죽었단 소린 언뜻 들었는데, 해보니 일본 저장소도 죽었다;; 우분투 공식 저장소를 추가하도록 하자.

`$ vim /etc/apt/sources.list` 명령어를 입력해서 아래의 코드를 추가하도록 하자. main 저장소가 여러개 있으면 충돌이 날 가능성이 있으니 조심.

```shell
###### Ubuntu Main Repos
deb http://archive.ubuntu.com/ubuntu trusty main
deb-src http://archive.ubuntu.com/ubuntu trusty main

###### Ubuntu Update Repos
# Major bug fix updates produced after the final release of the distribution.
deb http://archive.ubuntu.com/ubuntu trusty-updates main
deb-src http://archive.ubuntu.com/ubuntu trusty-updates main

## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu
## team. Also, please note that software in universe WILL NOT receive any
## review or updates from the Ubuntu security team.
deb http://archive.ubuntu.com/ubuntu trusty universe
deb-src http://archive.ubuntu.com/ubuntu trusty universe
deb http://archive.ubuntu.com/ubuntu trusty-updates universe
deb-src http://archive.ubuntu.com/ubuntu trusty-updates universe
```

저장소 목록을 업데이트 했다면 `apt-get update` 로 목록을 갱신해주고, 다음 단계를 진행하면 된다.

----------------------------------------

우선, 아래와 같은 명령어로 필수 패키지들을 설치하자. `-y` 는 패키지마다 설치할 것이냐고 묻는 걸 모두 `yes` 처리 해준다.

```shell
$ sudo apt-get install build-essential curl git m4 ruby texinfo libbz2-dev libcurl4-openssl-dev libexpat-dev libncurses-dev zlib1g-dev -y
```

그 다음, 아래의 명령어를 입력하자.

```shell
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/linuxbrew/go/install)"
```

마지막으로,  `.bashrc` 혹은 `.zshrc` 파일 하단에 아래와 같은 내용을 추가하자.

```shell
# linuxbrew
export PATH="$HOME/.linuxbrew/bin:$PATH"
export MANPATH="$HOME/.linuxbrew/share/man:$MANPATH"
export INFOPATH="$HOME/.linuxbrew/share/info:$INFOPATH"
```

`source .zshrc` 로 쉘 설정파일을 다시 불러오자.

----------------------------------------

## nvm 설치
nvm은 node  의 버전관리도구인데, ghost는 node의 0.10.x 버전에서 안정적으로 돌아가기에 버전을 맞춰줄 필요성이 있다. ~~(언제적부터 0.10.x를 계속 권장하는거냐... ghost 재단은 일을 해라!!)~~

아래와 같이 설치하자.

```shell
$ brew install nvm
```

그리고 `.zshrc` 하단에 아래와 같이 추가해주자.

```shell
# nvm
export NVM_DIR=~/.nvm
source $(brew --prefix nvm)/nvm.sh
```

`source .zshrc` 로 쉘 설정파일을 다시 불러오자.

----------------------------------------

## npm 설치
npm은 node의 패키지 관리도구인데, ghost 설치를 위해 필요하다. 2015년 12월 현재 2.5.x 버전을 권장하니 거기에 맞춰주자. ~~(언제적부터 2.5.x를 계속 권장하는거냐... ghost 재단은 일을 해라!!)~~

아래와 같이 설치하자.

```shell
$ brew install npm
```

----------------------------------------

## ghost 설치
이제 본격적으로 ghost를 설치하자. 

[Ghost 저장소](https://github.com/TryGhost/Ghost)에 적힌 조언대로, 직접 서비스할 예정이니 가급적 [Stable 버전](https://github.com/TryGhost/Ghost/tree/stable)을 다운받아 서버에 올려서 설치하자. 지금은 귀찮으니 master 버전을 설치하겠다. 아래와 같이 github에서 ghost 파일을 받아오자.

```shell
$ git clone git://github.com/tryghost/ghost.git ghost
```

그리고 `$ cd ghost` 로 이동을 해서 grunt를 설치하자.

```shell
$ npm install -g grunt-cli
```

그리고 아래와 같이 node 패키지를 설치하자.

```shell
$ npm install
```

그리고 아래처럼 마무리를 하자.

```shell
$ grunt init
$ grunt prod
```

----------------------------------------

### ghost 환경 설정
config.js를 설정하자.

```shell
$ cp config.example.js config.js
$ vim config.js
```

보통 아래에 있는 url만 수정해주어도 된다. 우선은 sqlite3를 사용해보도록 하자. 개인 블로그 정도이니 sqlite3를 사용하여도 무방하다.

```js
...
    production: {
        url: 'http://my-ghost-blog.com',
        mail: {},
        database: {
            client: 'sqlite3',
            connection: {
                filename: path.join(__dirname, '/content/data/ghost.db')
            },
            debug: false
        },
...
```

mariadb 혹은 mysql을 사용할 경우엔 database 부분을 아래와 같이 따로 수정해 주어야 한다. mariadb, mysql을 설치하고, 데이터베이스와 사용자를 생성한 후 아래에 적절히 값을 넣어주면 된다.

```js
...
database: {
    client: 'mysql',
    connection: {
        host: '127.0.0.1',
        user: '{블로그-DB-유저}',
        password: '{DB-비밀번호}',
        database: '{DB-이름}',
        charset: 'utf8'
    },
},
...
```

혹시 DB명, DB ID, DB PW가 그대로 노출되는 게 싫다면 쉘 환경변수를 응용하자.

그리고 nginx의 sites-available에 아래와 같이 추가하자.

```nginx
# https://gist.github.com/vvo/7414035

# cache 200 10 minutes, 404 1 minute, others status codes not cached
proxy_cache_valid 200 10m;
proxy_cache_valid 404 1m;

proxy_cache_key "$scheme$host$request_uri";

client_body_buffer_size 128k;

# default expires (browser cache) set to 1 minute
expires 1m;

# add a cache HIT/MISS header
add_header X-Cache $upstream_cache_status;

##################################

server {
	listen 80;
	server_name your.blog.com;
	#	access_log /var/log/nginx/ghost.log;

	client_max_body_size 20m;

	root /home/blog/ghost;
	index index.html index.htm;

	location / {
		proxy_set_header X-Real-IP $remote_addr;
		proxy_set_header HOST $http_host;
		proxy_set_header X-NginX-Proxy true;

    proxy_ignore_headers "Set-Cookie";
    proxy_hide_header "Set-Cookie";

		proxy_pass http://ghost;
		proxy_redirect off;
	}

  # add some caching on static assets
  location ~* \.(jpg|jpeg|png|gif|ico|css|js|eot|woff)$ {
  # ghost sends Cache-Control max-age=0 on CSS/JS for now
  # see https://github.com/TryGhost/Ghost/issues/1405?source=c#issuecomment-28196957
    proxy_ignore_headers "Cache-Control";
    expires 10y;
    proxy_pass http://ghost;
  }

}

upstream ghost {
	ip_hash;
	server 127.0.0.1:2368 weight=3;
	keepalive 100;
}

server {
	listen 2368;
	server_name your.blog.com;

	access_log /var/log/nginx/ghost.log;

	root /home/blog/ghost;
	index index.html index.htm;

	location / {
		proxy_set_header X-Real-IP $remote_addr;
		proxy_set_header HOST $http_host;
		proxy_set_header X-NginX-Proxy true;

		proxy_pass http://localhost:2368;
		proxy_redirect off;
	}
}
```

`$ sudo service nginx reload` 로 nginx 서버 설정을 다시 불러오자.

그리고 아래와 같은 명령어로 블로그를 실행하면 된다.

```shell
$ npm start --production
```

명령어 끝이 & 을 붙이면 백그라운드로 돌아간다. 근데 더 안전한 방법은 forever 패키지를 사용하는 것이다.

----------------------------------------

## Ghost run forever
Ghost를 계속해서 Background Task로 실행시키기 위해서는 forever를 사용하는 것이 좋다. 예기치 않은 오류로 프로세스가 종료되더라도 forever가 좀비처럼 계속 살려준다. ~~(오오 좀비 오오)~~

설치는 아래와 같다.

```shell
$ npm install forever -g
```

실행은 `NODE_ENV=production forever start index.js` 로 하고,  
종료는 `forever stop index.js` 로 한다.  
프로세스 확인은 : `forever list` 로 하면 된다.

껏다 킬 때가 많을 땐 자동화 스크립트를 만들어두면 편리하다.  
`restart.sh` 파일을 만들어 아래의 코드를 넣자.

```shell
forever stop index.js  
NODE_ENV=production forever start index.js  
```

그럼 `$ ./restart.sh` 만으로 간단히 블로그를 껏다 켤 수 있다. 테마를 개발할 때 자주 사용하게 되더라.

그리고 `/etc/init.d` 에 ghost 라는 파일을 생성하고 아래와 같은 코드를 붙여넣자.

```shell
#!/bin/sh

### BEGIN INIT INFO
# Provides: blog
# Required-Start:
# Required-Stop:
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
### END INIT INFO

USER="blog"
APP="/home/blog/ghost/index.js"
LOG="/var/log/ghost/server.log"

stop() {
	sudo su - $USER -c"NODE_ENV=production forever stop $APP"
}

start() {
	sudo su - $USER -c"NODE_ENV=production forever start --append -l $LOG -o $LOG -e $LOG $APP"
}

case "$1" in
	start)
		stop
		start
		;;
	stop)
		stop
		;;
	restart)
		start
		;;
	*)
	echo "Usage: $0 {start|stop|restart}"
esac
```

그럼 서버가 부팅하면 블로그가 백그라운드로 실행된다.

> 작성중입니다.

---

## 참고
1. [Github Ghost 저장소](https://github.com/TryGhost/Ghost)
2. [Ghost의 Troubleshooting](http://support.ghost.org/deploying-ghost/)
4. [Mailgun 코드 생성기](https://ghost.mailgun.com)  
5. [sharadchhetri 글](http://sharadchhetri.com/2015/06/08/setup-nginx-as-proxy-to-serve-ghost-blog-on-port-80/)
5. [Zetawiki 글](http://zetawiki.com/wiki/리눅스_포트_프로세스_목록_확인)
6. [NULI Grunt 사용법](http://nuli.navercorp.com/sharing/blog/post/1132682)
7. [Ghost 도움말](http://support.ghost.org/installing-ghost-linux/)
8. [Digital Ocean 커뮤니티](https://www.digitalocean.com/community/tutorials/how-to-host-ghost-with-nginx-on-digitalocean)
9. [taking 글](http://taking.kr/blog/archives/1051.html)  
12. [Ghost 공식 문서](http://docs.ghost.org/ko/installation/)    


[^n]: 텍스트 문서를 편집하는 문법 중 하나. 쉽게 HTML 등 다른 문서형태로 변환이 가능한 것이 장점.
[^n]: 보통 버전 숫자가 1.0 이하라면 베타라 보는 것이 좋다.
[^n]: Single Board Computer의 약자. 보통 작은 마더보드 하나로 작동하는 작은 컴퓨터를 지칭한다.