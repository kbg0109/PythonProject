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
# 객체.명령어()
# 변수에 저장해서 해도 동일

print("Ups AND Downs".lower())
print("Ups AND Downs".upper())
print("Ups AND Downs".swapcase())       #대소문자 반대로
print("Ups AND Downs".capitalize())     #첫 글자만 대문자, 나머지는 소문자

# 부분 문자열(의 인덱스) 검색
# 객체.find(검색하려는 문자열 객체)

print("some_string".find("ing"))        #ing가 8번 인덱스부터 시작하므로 8을 return (첫 번째 결과만 return)
print("some_string".find(""))           #빈 문자열은 모든 문자열에 들어가므로 0 return
print("some_string".rfind(""))          #뒤부터 검색하는 rfind, 양수 인덱스로 return
print("some_string".find("abcde"))      #검색결과가 없으면 -1 return

# 부분 문자열을 포함하는지 여부 판단 in (boolean)

print("a" in "abc")
print("" in "abc")

# 부분 문자열의 빈도 count()

print("banana".count("an"))

# 부분 문자열 대체 replace()

print("variables have no spaces".replace(" ","_"))