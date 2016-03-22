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
  - GIT_COMMITTER_NAME=channprj
  - GIT_COMMITTER_EMAIL=chann@chann.kr
  - GIT_AUTHOR_NAME=channprj
  - GIT_AUTHOR_EMAIL=chann@chann.kr
  - secure: A3V1exWLbgsdFB5Vah/hZEzPgn+kef7ING90P6zA3DJE/eYrFD/jPJUToW7F2kzOWDMwr0FPXJWrZR2yVs809H/FqHaE8CR24GnUs5YjSBWY/+ARdF+d1Whbe9dcMUH9CCVZof6leKgTsq5Zmw4At3k03nfLjBCogzJAQ87wF2KcV7+MBKaBHmU9x+qoMnPAwVAI1kda/fp7AlV8psbCieD4G2oj4AVJ2hI7vc1HjmdATbdgihSg4DoCNRWYt9Jtpu0PZyzJ/WBmI1DJHd0oEo4rzPfLNmq1VGW7K12J0SJ2BZkABD65S+P1RWhh6HbQd8T/8Eqp7sbS25d8Et8JYYYVsTTFJDsOSX9JyczJrEcmU3wYKxrm/Gxl/zRXBEp/AIWfdL5M7vwxOyEOl7ryYYbA+PoXQomRY56nfIXQJQ+3lqwqEpChCrgOcIPN5GE7xiZ288NfklV+Mkb8rAmKAE2d6OuTwgt72kyyaHQGpdYcrlu4P/p84ehSKhD8LAZyLg9t2iJUyWM2LUfcFGc6ymwJMjl9o36bjBboJ2FFc+CKFStAJdGscQyz9d4WrQ5ej8rqNJs5B28tSO+aLjI1DPDn5SBSFTduIAXIBKJpwKRkuMIjMjpe1j0wBXrWFMrEcVZS3CZWP8mifkmX/imu9zIoiMW6sas86O/K9P2jQvs=

before_install:
- git config --global user.email "chann@chann.kr"
- git config --global user.name "CHANN"
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