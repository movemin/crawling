html = """
<div class="product">
    <h2>노트북</h2>
    <p>100만원</p>
</div>
"""

# h2 태그의 시작 위치
start = html.find("<h2>")

# h2 태그의 종료 위치
end = html.find("</h2>")

# 제목 추출
product_name = html[start + len("<h2>"):end]

# p 태그의 시작 위치
start = html.find("<p>")

# p 태그의 종료 위치
end = html.find("</p>")

# 문단 추출
price = html[start + len("<p>"):end]

print(product_name)
print(price)