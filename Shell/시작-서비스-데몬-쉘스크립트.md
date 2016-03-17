Title: 서버 재부팅 시 서비스 자동 실행 쉘스크립트
Date: 2016-02-16 22:00
Category: Shell
Tags: shell, terminal, cli, sh, init, init.d, ubuntu, upstart
Slug: upstart-service-shell-script
Author: CHANN
<!--Summary: -->

> Ubuntu Linux 기준으로 작성함.

## init 파일 생성
`/etc/init.d` 에 example 생성 후 아래와 같이 설정하자.

```bash
$ chmod 755 example
$ chown root:root example
``` 

## 쉘 스크립트
`example` 의 코드는 아래와 같이 작성 가능하다.

```bash
#!/bin/sh

### BEGIN INIT INFO
# Provides: blog
# Required-Start:
# Required-Stop:
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
### END INIT INFO

USER="service"    

stop() {  # -c 옵션은 해당 USER로 실행함을 의미.
    sudo su - $USER -c "# something to stop"
}

start() {  
    sudo su - $USER -c "# something to start"
}

case "$1" in  
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart) 
        stop
        start
        ;;
    # 필요할 경우 reload 등의 옵션을 추가적으로 구현.
    *)
    echo "Usage: $0 {start|stop|restart}"
esac  
```

위의 주석처리 된 부분에서 `runlevel`을 2, 3, 4, 5라고 명시한 것(Default-Start)은 싱글유저 모드 이외엔 자동 시작하겠다는 의미이다. 위의 스크립트는 굉장히 간단하니 기타 응용 방법은 `/etc/init.d/` 의 다른 스크립트들을 보고 참고하자.


## 심볼릭 링크 추가
쉘스크립트 작성이 끝났으면 아래와 같이 심볼릭 링크를 추가해주자. rc는 다목적 시동 스크립트를 의미한다. upstart init은 우분투 6.10 때부터 도입되었다.

```bash
$ update-rc.d ghost defaults
$ update-rc.d ghost enable
```

------

