f = open("file_handling_01/test.txt", "r", encoding="utf-8")

# 1. 전체 다 읽음
# print(f.read())

# 2. 엔터바가 나올 때까지의 한 줄을 읽어 옴
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

# 3. 모든 라인들을 읽고 리스트 형태로 반환
# print(f.readlines())

# 4. 원래는 파일 다 읽으면 두번째부터는 못 읽는다.
# print(f.read())
# print(f.read())

# 5. 어디를 읽느냐를 다시 초기화 가능 -> 예제는 0번
# f.seek(0)

print(f.read())
f.seek(0)       # (숫자) 입력시 에러 난다면 바이트와 단위의 문제인데 유니코드의 같은 경우는 3개의 바이트를 쓰고 있는데 자리가 맞지 않는것
print()
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.seek(0)
print()
print(f.readlines())
f.seek(0)
print()