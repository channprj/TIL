Title: zsh에서 vim 명령어 자동완성 오류
Date: 2016-01-25 21:12
Category: Shell
Tags: zsh, shell, terminal, cli, sh, ohmyzsh, bug, fix
Slug: ohmyzsh-autocomplete-bug-fix
Author: CHANN
<!--Summary: -->

갑자기 `vim` 을 입력하고 tab을 누르니 `_arguments:450: _vim_files: function definition file not found` 라는 오류메시지가 떴다. 구글링을 해 보니 홈 폴더에서 `.zcompdump*` 파일을 지우면 대체로 잔버그가 해결된다는 답변[^1]에 꽤나 힘이 실려있었는데, 이번 경우에는 좀처럼 통하지 않았다.  알고 보니 `exec zsh` 해야 해결되었다. 아무 생각 없이 `source .zshrc` 를 치고 '어... 왜 안 고쳐지지?' 헤맸던 내가 바보같다... dotfile 은 환경설정이거늘 ㅠㅠ

## 정리
```bash
$ rm ~/.zcompdump*
$ exec zsh
```

[^1]: oh-my-zsh 버전이 올라갈 때마다 잔버그가 자주 나타나는 모양이다.