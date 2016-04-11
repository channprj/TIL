Title: TIL에 Travis-CI 적용하기
Date: 2016-03-22 23:00
Category: CI
Tags: ci, travis-ci, dev, script, yaml, til, 개발, 스크립트, 자동화, 지속적통합
Slug: travis-ci-setting-on-til
Author: CHANN
<!--Summary: -->
TIL의 Generator 저장소와 Github Pages 저장소를 분리해서 운영하다가 지저분함을 느끼고 하나로 합침. 내 Travis-CI의 YAML 파일은 아래와 같음.

```yaml
language: python

python:
- '3.4'

env:
  global:
  - GIT_COMMITTER_NAME={your-id}
  - GIT_COMMITTER_EMAIL={your-email}
  - GIT_AUTHOR_NAME={your-name}
  - GIT_AUTHOR_EMAIL={your-email}
  - secure: {your-key}

before_install:
- git config --global user.email "{your-email}"
- git config --global user.name "{your-id}"
- git clone -b generator --quiet https://${GH_TOKEN}@github.com/channprj/TIL.git generator
- cd generator

install:
- pip install -r requirements.txt -q
- npm install -g less

before_script:
- git clone -b gh-pages --depth 1 --quiet https://${GH_TOKEN}@github.com/channprj/TIL.git output
- cd content
- rm -rf posts
- git clone -b master --quiet https://${GH_TOKEN}@github.com/channprj/TIL.git posts
- cd ..

script:
- make publish

after_success:
- cd output
- git add -A
- git commit -m "Pages updated from Github using Travis-CI."
- git push https://${GH_TOKEN}@github.com/channprj/TIL.git gh-pages --quiet

branches:
  only:
  - master

notifications:
  email: false
```

------

## 설정법 요약
1. Travis-CI 에서 해당 브랜치를 체크
2. Github 환경설정에서 Key 발급 후 키를 암호화하여 Travis YAML 파일에 사용
3. Travis Document 를 보며 자신에게 알맞은 프로세스로 dotfile 생성
4. 정상 작동하는지 테스트 해보고, 오류가 났다면 Travis 로그를 보고 수정

------

## 후기

Github 저장소 페이지에서 보기 좋게 하기 위해 master 브랜치에서는 오로지 MD 문서만 정리를 하였음. generator 브랜치에서 master 수정 내역을 불러와서 Pelican 으로 Publish 한 다음, gh-pages 브랜치로 Publish 결과를 다시 푸시함.

결과적으로, 저장소를 이중화 했을 때보단 겉보기엔 깔끔해보이나 commit log 를 볼 땐 지저분해 보일 수 밖에 없음. Git-Flow 라던가 Github-Flow 에 맞지 않은 브랜치 전략이지만 일단은 이대로 계속 운영해 볼 생각.

Git 의 Submodule 이나 Subtree 를 좀 더 자유자재로 사용 가능해지면 좀 더 깔끔하고 어썸한 방법으로 구조를 바꿀 생각.
