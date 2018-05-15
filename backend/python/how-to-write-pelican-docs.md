Title: Pelican 문서 작성법
Date: 2016-02-27 18:00
Category: Python
Tags: python, pelican, static site generator, 파이썬, 펠리칸, 정적 페이지 생성기, 블로그, blog, github pages, markdown, 마크다운, writing, 글쓰기
Slug: how-to-write-pelican-docs
Author: CHANN
<!--Summary: -->

개인적으로 `.rst` [(reStructuredText)](https://en.wikipedia.org/wiki/ReStructuredText) 방식의 문서를 선호하지 않으므로, 이 글에서는 `.md` [(Markdown)](https://nolboo.github.io/blog/2013/09/07/john-gruber-markdown/) 방식의 문서를 작성하는 법을 다룰 예정.


## 기본 틀
양식의 기본적인 틀은 아래와 같다. Slug나 Summary 와 같이 없어도 그만인 것들은 생략 가능. Slug는 문서의 URL을 생성하는 것인데, 가급적 영어로 적는 것을 추천. 한글로 적으면 자동으로 한글리쉬(...) 같은 형태로 바꿔버리기 때문. 예를들어, `한글로 적지마요` 를 Slug로 하면 `hangeulro-jeokjimayo` 같은 형태로 문서가 발행됨.

```markdown
Title: 문서 제목
Date: 2016-08-08 18:00
Modified: 2016-09-09 19:00
Category: 펠리칸
Tags: 펠리칸, 문서
Slug: pelican-slug
Authors: CHANN
Summary: 펠리칸 문서를 작성하는 법을 다룹니다. 마크다운이 좋아요.

여기다 본문을 작성하면 됩니다.
```

------

## 확장기능
Pelican 은 [Markdown Extension](http://pythonhosted.org/Markdown/extensions/)을 비롯한 다양한 [Plugin](https://github.com/getpelican/pelican-plugins)들을 제공함. 여러모로 쓸만한 플러그인을 대충 뽑아보자면 다음과 같음.

* Related Post
* Category Order
* CJK auto spacing
* GitHub activity
* Interlinks
* Pelican Page Order
* Share post
* Sitemap

------

## Github Pages 에서 404 페이지 작성
아래와 같이 작성하면 됨. *Status* 를 *hidden* 으로 하면 목록에 뜨지 않음. 

```markdown
Title: Not Found
Slug: 404
Save_as: 404.html
Status: hidden

글을 찾을 수 없습니다. [검색](/search)하시거나 [아카이브](/archives)를 확인해주세요.
```

------

## 단점
글이 이미지 추가 시 마크다운 문법에 맞추어 따로 상대경로를 입력해줘야하는게 귀찮음. 글 수정 시 수정시간을 적어줘야 하는데, 수정시간을 수정하는 걸 깜박하거나 귀찮아서 방치하게 됨.

------

## 추가사항
다국어지원도 되고 연관된 컨텐츠 보여주기 기능도 있는데, 기타 자세한 점은 [Pelican Documentation](http://docs.getpelican.com/en)을 직접 확인하도록 하자. 공개된 Plugin을 찾아보면 입맛에 맞게 커스터미이징 할 수 있음.

## 참고
1. [Pelican Documentation](http://docs.getpelican.com/en)
2. [존 그루버 마크다운 페이지 번역](https://nolboo.github.io/blog/2013/09/07/john-gruber-markdown/)
3. [rst Wikipedia](https://en.wikipedia.org/wiki/ReStructuredText)