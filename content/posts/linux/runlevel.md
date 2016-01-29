Title: 리눅스 runlevel 정리
Date: 2016-01-30 06:22
Category: Linux
Tags: linux, server, cli, runlevel, ubuntu, centos, redhat, fedora, 
Slug: runlevel-summary
Author: CHANN
<!--Summary: -->

## runlevel 이란

`runlevel` 이란, 리눅스 시스템 관리의 용이함을 위하여 서비스의 실행을 단계별로 구분하여 적용하는 것을 말함. 보통 0 ~ 6 까지 총 7가지 모드가 있음. 리눅스마다 조금씩 다르지만 0(정지), 1(싱글모드), 6(재시작)은 일치함. 낮은 레벨일수록, 시스템 시작시 불러오는 드라이버나 데몬 수가 적음. `runlevel` 은 높아지는 방향으로 진행되며, 부팅되면 0부터 시작함. `reboot` 명령어를 실행하면 `runlevel` 이 6이 됨.

------

* 0 - halt (DO NOT set initdefault to this)<br/>
시스템 종료를 의미. `runlevel` 0으로 변경하라는 명령은 시스템을 종료하는 것.

* 1 - Single user model<br/>
시스템 복원모드라고도 하며, 기본적으로 관리자 권한을 얻음. 주로, 파일시스템을 점검하거나 관리자 암호를 변경할 때 사용. 윈도우의 안전모드와 유사하다고 보면 됨.

* 2 - Multiuser mode, without NFS (The same as 3, if you do ot have networking)<br/>
NFS(Network File System)을 지원하지 않는 다중 사용자 모드. 네트워크를 사용하지 않음.

* 3 - Full muliuser mode<br/>
CLI(Command Line Interface) 다중 사용자 모드. 그래픽 유저 모드 지원안함.

* 4 - unused<br/>
임의로 정의해서 사용할 수 있는 레벨. 기본적으로는 사용하지 않음.

* 5 - X11<br/>
level 3과 유사하나 그래픽 유저 모드를 지원.

* 6 - reboot (DO NOT set initdefault to this)<br/>
시스템 재부팅을 의미. `runlevel` 6으로 변경하라는 명령을 내리면 시스템을 재부팅.


보통 0, 3, 6 을 많이 사용함. `runlevel` 의 변경은 root 사용자의 경우만 가능.

------

### 우분투
1(싱글유저), 2(GUI)가 특징.

* 0 - 정지
* 1 - 싱글 유저
* 2 - 그래픽, 멀티유저 + 네트워킹 (기본값)
* 3 - 2와 같음 (사용안함)
* 4 - 2와 같음 (사용안함)
* 5 - 2와 같음 (사용안함)
* 6 - 재시작

------

### 레드햇
1(싱글유저), 3(CLI), 5(GUI)가 특징.

* 0 - 정지
* 1 - 싱글 유저
* 2 - 미사용 (사용자 정의 가능)
* 3 - 다중 사용자, 콘솔 로그인
* 4 - 미사용 (사용자가 정의 가능)
* 5 - `runlevel` 3 + X11
* 6 - 재시작<br/>

------

### 솔라리스
* 0: 정지
* S(s): 싱글 유저
* 1: 관리
* 2: 멀티유저
* 3: 멀티유저(+NFS 자원 공유)
* 4: 커스텀 멀티유저[1]
* 5: 정지[2]
* 6: 재시작[3]