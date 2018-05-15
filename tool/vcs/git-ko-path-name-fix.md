Title: Git 한글 깨짐문제
Date: 2016-01-20 14:28
Category: VCS
Tags: vcs, git, i18n, github, terminal, cli
Slug: git-ko-path-name-fix
Author: CHANN
<!--Summary: -->

인코딩 문제. 아래 한 줄이면 됨.

```bash
$ git config core.quotepath false
```

------

## 참고
1. [KLDP 글](https://kldp.org/node/132431)
