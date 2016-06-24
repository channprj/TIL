Title: zsh 소유권 문제 해결
Date: 2016-06-04 20:00
Category: Shell
Tags: zsh, shell, terminal, cli, sh, ohmyzsh, bug, issue, fix, 터미널, 쉘, 권한, 문제해결
Slug: zsh-ownership-issue-fix
Author: CHANN
<!--Summary: -->
가끔 터미널로 작업하다 보면 아래와 같은 상황을 직면한다.

```shell
Welcome to Ubuntu 14.04.3 LTS (GNU/Linux 3.13.0-66-generic x86_64)

 * Documentation:  https://help.ubuntu.com/
Last login: Sat Oct 31 15:15:36 2015 from 203.229.151.243
zsh compinit: insecure directories, run compaudit for list.
Ignore insecure directories and continue [y] or abort compinit [n]?
```

이러한 상황의 문제점은 대부분 zshell과 관련된 소유권과 권한의 문제일 가능성이 큼. 특정 패키지나 라이브러리 등을 설치할 때 외부의 스크립트를 사용할 경우, 가끔 `/usr/local/share/` 의 소유권과 권한을 변경해버리기 때문.

아래의 두 가지 방법이 있음. zshell을 사용하는 OS X, Linux 모두 적용 가능.

------

## site-functions 의 소유권 문제일 경우

```shell
$ cd /usr/local/share/zsh
$ sudo chown -R root:root ./site-functions
```

------

## zsh 권한과 소유권 문제일 경우

```shell
$ cd /usr/local/share/
$ sudo chmod -R 755 zsh
$ sudo chown -R root:staff zsh
```

------

## 참고
1. [Zsh.org의 글](http://www.zsh.org/mla/users/2012/msg00062.html)  
2. [Homebrew의 이슈](https://github.com/Homebrew/homebrew/issues/7801#issuecomment-2187273)
