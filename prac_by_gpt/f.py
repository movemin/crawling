"""
다음 HTML에서 
모든 상품 이름과 가격을 
추출하는 코드를 만들어봐라.
"""

from bs4 import BeautifulSoup

html = """
<div class="product">
    <h2>노트북</h2>
    <p>100만원</p>
</div>

<div class="product">
    <h2>스마트폰</h2>
    <p>80만원</p>
</div>

<div class="product">
    <h2>태블릿</h2>
    <p>50만원</p>
</div>
"""

soup = BeautifulSoup(html, "html.parser")

products = soup.find_all("div", class_ = "product")

for product in products:
    name = product.find("h2").get_text()
    price = product.find("p").get_text()

    print(f"상품 이름: {name}")
    print(f"상품 가격: {price}\n")