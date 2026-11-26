"""여러 태그 추출"""

from bs4 import BeautifulSoup

html = """
<p>노트북</p>
<p>스마트폰</p>
<p>태블릿</p>
"""

soup = BeautifulSoup(html, "html.parser")

# find_all()은 리스트처럼 사용할 수 있는 ResultSet 객체를 반환한다.
products = soup.find_all("p")

for product in products:
    print(product.get_text())