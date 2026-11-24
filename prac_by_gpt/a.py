# 데이터를 요청하고 받아오는 라이브러리
import requests

url = input("URL 입력: ")

# GET 요청을 보내고 응답 객체를 저장
response = requests.get(url)

print(response)
if response.status_code == 200:
    print("요청 성공")

    # 응답 본문을 문자열로 반환
    print(response.text)
else:
    print("요청 실패")

    # HTTP 상태 코드
    print(type(response.status_code))