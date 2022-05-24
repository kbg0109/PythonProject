# 예제 : 현재 온도를 화씨 75도로 초기화하는 프로그램을 작성하라. 그 후 화씨를 섭씨로 변환하라. 섭씨 값을 출력하라
# (c = (f-32)/1.8)
# c : 섭씨
# f : 화씨

# 현재 온도를 화씨 75도로 초기화
temperature_now = 75

# 화씨에서 섭씨로 변환 (후 반올림)
temperature_Celsius = round((temperature_now - 32) / 1.8)

# 섭씨로 출력
print(temperature_Celsius)