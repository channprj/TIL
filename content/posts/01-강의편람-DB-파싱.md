Title: 강의 편람 DB 파싱
Slug: ku-lecture-db-parsing
Date: 2015-10-08 00:00
Category: Project
Tags: ku, db, parsing, python
Author: CHANN
Summary: 졸업프로젝트 임시 기록용.


> 작성중
> 
> 이 글은 개인 기록용으로, 다소 불친절할 수 있습니다.

강의평가 시스템을 구축하기 전에, 먼저 강의 편람 정보를 가지고 있어야 한다.  
고려대는 강의편람을 xml 등의 형식으로 따로 제공하지 않으므로, html 파싱을 해서 추출해야 한다.  
추출하기 전에 앞서 소스 URL을 찾아내야만 했다.  

`http://sugang.korea.ac.kr` 의 코드를 면밀히 분석한 결과, 아래의 URL을 찾아낼 수 있었다.  
아래의 주소를 통해 수강 편람을 파싱받아 DB에 뼈대를 저장해 두면 될 것 같다.  

`http://infodepot.korea.ac.kr/lecture/LecMajorSub.jsp?yy=2010&tm=1R&col=4460&dept=4548`

---

아래의 코드를 참고하여 GET으로 값을 전달하면 쉽게 HTML 파싱을 할 수 있다.  
각 변수별 값은 `html`과 `js`를 통해 추출 가능하다.  
```html
...
<select name="yy">
<option value="2015" selected="">2015년</option>
<option value="2014">2014년</option>
...
<select name="tm">
<option value="1R">1학기</option>
<option value="1S">여름학기</option>
<option selected="" value="2R">2학기</option>
<option value="2W">겨울학기</option>
<option value="SC">국제하계대학</option>
</select>
<select name="col" onchange="changeCol(frm_ms, this, frm_ms.dept);">
<option selected="" value="0137" style="color:black">법과대학</option>
<option value="0140" style="color:black">경영대학</option>
<option value="0143" style="color:black">문과대학</option>
<option value="4652" style="color:black">생명과학대학  </option>
...
<option value="4460" style="color:black">과학기술대학</optin>
...
<select name="dept">
...
<option value="4548" style="color: black;">컴퓨터정보학과 </option>
<option value="4549" style="color: black;">정보통계학과   </option>
<option value="4550" style="color: black;">전자및정보공학부 </option>
...
```

Parser는 `Python`의 `Beautiful Soup` 라이브러리를 사용하면 편리할 것 같다.

---

### Making the soup
아래의 코드는 링크를 모두 가져오는 bs4 예제다.

```python
from bs4 import BeautifulSoup
import requests

r  = requests.get("http://kuple.kr/free")

data = r.text

soup = BeautifulSoup(data, "lxml")

for link in soup.find_all('a'):
  print(link.get('href'))
```

---

## 참고
1. [zevross의 블로그 글](http://zevross.com/blog/2014/05/16/using-the-python-library-beautifulsoup-to-extract-data-from-a-webpage-applied-to-world-cup-rankings/)
2. [점프 투 파이썬](https://wikidocs.net/book/1)
