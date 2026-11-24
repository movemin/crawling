# 기존 파일에서 텍스트 추가
# 같은 행 끝에 추가 되기 때문에 줄바꾸고 싶다면 엔터키도 같이 넣어주기
f = open("file_handling_01/test.txt", "a", encoding = "utf-8")
f.write("안녕하세요 파이썬 입니다.\n")