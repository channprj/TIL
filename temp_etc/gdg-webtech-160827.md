Title: GDG Webtech 160827
Date: 2016-08-27 18:30
Category: Study
Tags: study, programming, dev, web, chrome, service worker, optimization, tech, gdg
Slug: gdg-webtech-160827
Author: CHANN
<!--Summary: -->
> 단순 참고용 메모, 개인 기록임.

* CPU 와 GPU 사이에 통신하면서 발생하는 이슈
* 메모리의 한계에 도달했을 때
* CPU 데이터 변경 시 GPU 데이터도 변경 필요

------

## Vertex & Plolygon
개념 숙지

------

## 렌더링
GPU를 효율적으로 활용하도록 잘 이용해야.

* 텍스쳐로 이미지 고속 출력
* 이미 가지고 있는 텍스쳐 재활용
* 회전, 확대, 축소, 기울임, 반투명 등
* 동시 처리 등

------

## 주의해야 할 점
* GPU 비디오 메모리로 데이터 전송하는 것이 매우 느림
* 데이터 전송 시간 = 데이터 크기 / 버스 속도
* **CPU 처리시간** : CPU에서 데이터 생성 후 GPU로 전송

------

## 웹페이지 & 크롬 렌더링
HTML tab soup --> DOM Tree --> Render Tree --> Paint
크롬 렌더링은 조금 더 복잡

## 레이어 모델
* 이미지 단위의 요소
* 최종적으로 표현될 이미지 단위
* 텍스쳐로 GPU로 업로드
* 레이어 배치 합성하여 최종 웹페이지 표현
* 레이어 이미지는 CPU에서 생성 --> 레이어에 생성되는 이미지는 CPU 소모

------

## 컴포지트(Composite)
Content Rendering --> Page Composition --> Desktop Composition
뭐 하나만 바뀌어도 이 과정을 모두 다시 거치게 됨.

------

## Reflow 이슈
Reflow = Layout = Layouting
* DOM 노드가 가지는 레이아웃 정보(Geometry)가 변경되면 레이아웃은 다시 재계산을 해야함.

1. 레이아웃의 변경이 트리를 따라 전파 (CPU)
2. 레이어 이미지의 갱신 필요 (CPU)
3. 레이어 이미지 변경으로 VRMA의 텍스터 갱신 필요 (RAM to VRAM Bandwidth)


------

## Repaint 이슈
Repaint = Redraw

컨텐츠 변경으로 텍스쳐를 새로 생성해야함

------

## 최적화
* 네이티브 어플리케이션 --> 최대한 가벼운 렌더링 프로세스 구성
* 렌더링 패스는 철저히 브라우져 영역
* 병목 구간의 발생을 줄여야

------

## 가장 간단한 Hack - 레이어 분리
### 크롬에서 DOM 노드가 레이어로 분리되는 조건들
1. 3D혹은 Perspective 를 표현하는 CSS Transform 속성을 가진 경우
2. 하드웨어 가속 디코딩을 사용하는 <video> 엘리먼트
3. 3D 컨텍스트 혹은 하드웨어 가속 2D 컨텍스트를 가지는 <canvas> 엘리먼트
4. 플러그인 영역
5. Opacity 또는 Trasform 애니메이션의 사용
6. 가속 가능한 CSS 필터
7. COmposite Layer 를 가진 하위 노드
8. 낮은 z-index 를 가진 형제노드가 Composite Layer 를 가진 경우

분리 조건 요약 : 해당 DOM 노드가 주변 노드와는 별개로 렌더링되어야 빠른 경우

### 강제적인 레이어 분리가 만능은 아님
* 레이어 분리는 필연적으로 텍스쳐 이미지 분리를 의미 --> 추가 메모리 소모
* 메모리 공간 부족 시 기존 데이터 릴리즈 후 새로운 데이터 업로드
* 레이어 분리를 통한 성능 향상은 송수신 오버헤드를 발생시킴

**하드웨어 가속으로 얻는 성능은 공짜가 아님**

------

## CSS의 will-chage
* 바뀔 가능성이 큰 CSS 엘리먼트를 hint 로 제공
* 브라우져가 가능할 경우 레이어로 분리해둠
* 효과가 미미할 수 있으나 퍼포먼스에 도움이 될 것

------

## 렌더링 퍼포먼스
web fundamental, w3c 등 문서 참고.

## Webp
```html
<picture>
    <img ...>
    <img ...>
    <img ...>
</picture>
```

## <img>의 sizes, srcset, src...etc
자세한 건 검색

## Round Trip
Wifi, LTE, 3G, 2G 등의 통신환경에 따른 대처. 한국은 인프라가 짱짱하므로 국내 서비스에선 대체로 신경쓰지 않아도 됨. HTTP Request 관련 문서 참고. 

## Regioning, Critical then Rest...
초반에 Preload 하여 보여준 후 나중에 전체 로딩. FOUC vs 형태 초기로딩 후 천천히 형태를 완성하는 방식. 애니메이션 렌더링 등과 관련된 JS 참고. [링크](https://aerotwist.com/blog/guitar-tuner/)

------

## Defer iFrames
```html
<iframe data-src="#"></iframe>
<script>// async loading iframes</script>
```

## HTTP/2
HTTP/2는 커넥션을 연결하고 한꺼번에 요청을 보내서(stream) 속도가 매우 빨라짐. simplehttp2server by google 참고.

## Lie-Fi
네트워크 인프라의 문제로 서버와의 통신이 원활하지 않음. 그럴 땐 Application Cache를 사용. 

## Service Worker
Background 에서 작업을 돌림. 로딩만을 위한 규격은 아님. 오프라인이나 느리게 로딩되는 것을 Service Worker 가 캐시해둠.

* UI 스레드에서 분리되어 실행해야 하므로 DOM 에 대한 직접 접근/조작 불가
* 자체적 글로벌 스코프
* 일부 속성, API 만 허가

Shared Worker는 Lifecycle을 가지고 있음.