Title: TIL에 Travis-CI 적용하기
Date: 2016-03-22 23:00
Category: CI
Tags: ci, travis-ci, dev, scrpit, yaml, til
Slug: travis-ci-setting-on-til
Author: CHANN
<!--Summary: -->
> WIP

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