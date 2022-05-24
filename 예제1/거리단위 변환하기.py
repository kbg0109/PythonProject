# 예제 : 변수를 5(마일)로 초기화, 5마일을 킬로미터로 변환, 킬로미터를 미터로 다시 변환
# km = mile / 0.62137
# meter = 1000 * km
# 다음과 같은 형식으로 출력
#
# 5
# 마일
# 8.04672
# 킬로미터
# 8046.72
# 미터

# 변수를 5로 초기화
length_mile = 5

# 5마일을 킬로미터로 변환, 5번째 자리로 반올림
length_km = round(length_mile / 0.62137, 5)

# 킬로미터를 미터로 변환
length_meter = length_km * 1000

print(length_mile)
print("마일")
print(length_km)
print("킬로미터")
print(length_meter)
print("미터")