# 041 upper 메서드
# 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.

# ticker = "btc_krw"

ticker = "btc_krw"
ticker = ticker.upper()
print(ticker)

# 042 lower 메서드
# 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.

# ticker = "BTC_KRW"

ticker = "BTC_KRW"
ticker = ticker.lower()
print(ticker)

# 043 capitalize 메서드
# 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.

a = "hello"
a = a.capitalize()
print(a)

# 044 endswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.

# file_name = "보고서.xlsx"

file_name = "보고서.xlsx"
file_name.endswith("xlsx")

# 045 endswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.

# file_name = "보고서.xlsx"

file_name = "보고서.xlsx"
file_name.endswith(("xlsx", "xls"))

# 046 startswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.

# file_name = "2020_보고서.xlsx"

file_name = "2020_보고서.xlsx"
file_name.startswith("2020")

# 047 split 메서드
# 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.

# a = "hello world"

a = "hello world"
a = a.split()
print(a)
# 기본값은 공백

# 048 split 메서드
# 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.

# ticker = "btc_krw"

ticker = "btc_krw"
ticker = ticker.split("_")
print(ticker)

# 049 split 메서드
# 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.

# date = "2020-05-01"

date = "2020-05-01"
date = date.split("-")
year = date[0]
month = date[1]
day = date[2]
print(f"{year}년 {month}월 {day}일")

# 050 rstrip 메서드
# 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.

# data = "     039490     "

data = "     039490     "
rdata = data.rstrip()
ldata = data.lstrip()
print(data)
print(ldata)
print(rdata)