Title:  Pelican에서 글 쓰는 법
Date: 2015-11-18 17:27
Category: Pelican
Slug: how-to-write-on-pelican

Pelican에서 글을 쓰는 건 간단하다.

## 작성법

```shell
├── LICENSE
├── Makefile
├── __pycache__
│   └── pelicanconf.cpython-34.pyc
│
├── content  # 이 폴더 안에 다음과 같이 xxx.md(마크다운) 파일을 넣자
│   ├── about.md
│   ├── hello.md
│   └── how-to-write.md
│
├── develop_server.sh
├── fabfile.py
├── pelicanconf.py
├── pelicanconf.pyc
├── publishconf.py
├── publishconf.pyc
│
└── output  # 이 폴더가 바로 github page에 동기화되어야 할 폴더
```

Pelican을 사용할 때 명시해야 할 형식은 아래와 같다.

```markdown
Title:  제목을 적으면 된다
Date: 2015-11-18 17:27
Category: 카테고리를 적으면 된다

그리고 여기에 내용을 적으면 된다.
```

내용에서의 마크다운 문법은 Git-Flavored Markdown  의 형식을 준수하면 된다.

파일 제목을 영어로 작성하자. 한글로 작성시 오류가 날 확률이 있다.

---
## Github Pages에 업로드하기

단순하니 아래의 명령어를 참고하자.

```shell
# 펠리칸으로 빌드를 하고
$ pelican content

# output 폴더로 가서
$ cd output

# 커밋을 하고 푸시한다
$ git add .
$ git commit -m "커밋 메시지"
$ git push origin master
```

좀 더 편리한 방법으로 Travis-CI를 연결하여 자동으로 푸시되게 하는 방법이 있는데, 이 부분은 나중에 작성할 예정이다.

현재 upload.sh 파일을 작성하여 위의 과정을 쉘 스크립트로 자동화시켜놓았다.
Travis와 연동하면 의미없는 짓이긴 하지만... 당장 바로 써먹을 땐 무식하게 돌아가도록 짜는 것도.... 생각보다 그리 나쁘진 않다. (...)