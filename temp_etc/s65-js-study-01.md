Title: S65-01 JS, Canvas, SVG
Date: 2016-02-11 22:32
Category: Study
Tags: study, programming, dev, js, javascript, canvas, svg, 자바스크립트, ECMAScript, ES6
Slug: s65-js-study-01
Author: CHANN
<!--Summary: -->

<!-- 첫 번째 출석 8865 -->

* 트렌디한 프레임워크나 라이브러리, 최신기술보다는 원론적인 내용을 다룰것
* 개발자로서 오래 살아남기 위해서는 기초 및 핵심기술이 중요

## Graphic System
디지털 환경에서는 픽셀(점)으로 그래픽을 표현함. 모든 컴퓨터 그래픽 시스템의 기초는 비트맵 시스템임.

점을 하나하나 찍기보다는 계산에 의해 색을 채울 방법을 고민하기 시작함.

* Layer 0 - Fixed Number : 확정되고 고정된 수치
--> Fixed Number로 반응형 환경에 대응하기 힘들었음.

(Layer 0과 1 사이의 애매함 : Drawing API, Shader, Filter, FontRenderer)
--> 보통 Layer 0을 감싸고 있는 기저레이어에서 제공

* Layer 1 - Caculator Hint : 상대적인 수치
ScreenSize, ChromeSize, Foreground, Layout System, LazyDetect, Reflow, etc.

Canvas API --> Apple의 Dashboard API 기반.
Dashboard, Android Widget 등에서 쓰이는 Canvas API도 위와 거의 동일.


* Layer 2 - Components
추상화로 미리 구현된 요소(element)들. (div, input, textarea, img, a, ...)
요소 < 노드

<div>Hello World!</div> --> Static Rendering

Model(Data) - View(Layout)
기억하고 보여주고 싶은 데이터만을 추린 것이 모델.
Runtime Rendering

* Layer 3 - Frameworks

------

## SVG (Scalable Vector Graphics)
2D 그래픽을 표현하기 위해 XML로 정의된 마크업 언어.

* Vector Shape
* Images
* Text

Group, Style, Transform 가능.

* Embedding
* Scripting

**SVG의 선, 도형 하나한가 DOM 엘리먼트로 동작하여 이벤트를 걸 수 있음.**

### SVG(VML) vs Canvas
DOM은 구조적으로 복잡하여 로딩 속도가 느려질 수 밖에 없음.
Canvas는 단일 엘리먼트라 상대적으로 속도가 빠를 수 밖에 없음.

### Tools, Library for SVG
#### Tools
* Adobe Illustrator
* CorelDRAW
* Libre Office Draw, Open Office Draw (무료)
* Inkscape (무료)
* etc...

#### Libraries
* D3.js
* raphaelJS

### SVG as a markup
`<svg>`, `<img src="#" />` ...

