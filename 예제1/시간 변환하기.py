# 프로젝트 문제 : 분을 시간으로 바꾸기
# 예) 121분을 입력했다면
#
# 2
# 시간
# 1
# 분
#
# 을 출력해야한다.

# 변환할 분(min)에 대한 변수
minutes_to_convert = 123

# 시간 부분을 정수화
hours_decimal = minutes_to_convert / 60
hours_part = int(hours_decimal)

# 방법 A. 분 부분(시간의 소수부분 * 60)을 반올림하여 정수화(오차 가능성)
minutes_decimal = hours_decimal - hours_part
minutes_part = round(minutes_decimal * 60)

# 방법 B. 전체 시간을 60으로 나눴을 때의 나머지를 통해 반올림 없이 정확한 분 얻기
minutes_part = minutes_to_convert % 60

# 결과
print(hours_part)
print("시간")
print(minutes_part)
print("분")