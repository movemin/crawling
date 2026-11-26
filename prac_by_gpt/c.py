from bs4 import BeautifulSoup

html = """
<div class="product">
    <h2>노트북</h2>
    <p>100만원</p>
</div>
"""

# HTML 문자열을 파싱
# "html.parser"는 HTML 문법을 해석하는 파이썬 내장 파서다.
soup = BeautifulSoup(html, "html.parser")

# 태그 탐색
# soup.find("h2")는 문자열이 아니라 BeautifulSoup의 Tag 객체를 반환한다.
product_name = soup.find("h2")
product_price = soup.find("p")

print(product_name)
print(product_name.get_text())
print(product_price.get_text())