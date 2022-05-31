# input() 함수로 좋아하는 계절을 물어보고 season에 할당한다.
# season을 출력
# input() 함수로 태어난 날짜를 물어보고 date에 할당한다. (정수로 대답해야함)
# date를 정수로 변환하여 재할당
# date 출력
# 사용자가 입력한 계절과 날짜를 한 문장으로 출력한다.

season = input('좋아하는 계절은 무엇입니까?: ')
print(season)

date = input('태어난 날짜는 언제입니까?: ')
date = int(date)
print(date)

print('좋아하는 계절은 {}이고, 태어난 날짜는 {}일입니다.'.format(season, date))