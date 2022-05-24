# 문자열의 첫 글자부터 0, 마지막 글자부터 -1

print("fall 4 leaves"[0])
print("fall 4 leaves"[-1])

# 문자열을 변수에 저장해도 동일하게 기능

index = "fall 4 leaves"
print(index[0])
print(index[-1])

# [시작 인덱스 : 끝 인덱스 : 간격] -> 부분 문자열 추출
print("부분 인덱스")

print(index[2:7:1])
print(index[2:11:3])
print(index[-2:-11:-3])     #뒤부터 세면 반대로 나옴

# len() -> 문자열 길이
print("문자열 길이")

print(len(""))
print(len(index))

# 대소문자 변경 .upper(), .lower(), .swapcase(), .capitalize()
# 변수에 저장해서 해도 동일

print("Ups AND Downs".lower())
print("Ups AND Downs".upper())
print("Ups AND Downs".swapcase())       #대소문자 반대로
print("Ups AND Downs".capitalize())     #첫 글자만 대문자, 나머지는 소문자