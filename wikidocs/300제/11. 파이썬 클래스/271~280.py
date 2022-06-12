# 271 Account 클래스

# 은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다. Account 클래스를 생성한 후 생성자를 구현해보세요. 생성자에서는 예금주와 초기 잔액만 입력 받습니다. 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.

# 은행이름: SC은행
# 계좌번호: 111-11-111111


from random import randint


class Account:
    def __init__(self, 예금주, 잔액):
        self.예금주 = 예금주
        self.잔액 = 잔액
        self.은행이름 = "SC은행"
        list = []
        for i in range (0, 11):
            i = randint(0, 9)
            list.append(i)
        num1 = str(list[0]) + str(list[1]) + str(list[2])
        num2 = str(list[3]) + str(list[4])
        num3 = str(list[5]) + str(list[6]) + str(list[7]) + str(list[8]) + str(list[9]) + str(list[10])
        num = num1 + "-" + num2 + "-" + num3
        self.계좌번호 = num
        
a = Account("김민수", 100)

print(a.예금주, a.잔액, a.은행이름, a.계좌번호)

# 272 클래스 변수

# 클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요. 

from random import randint


class Account:
    account_count = 0
    
    def __init__(self, 예금주, 잔액):
        self.예금주 = 예금주
        self.잔액 = 잔액
        self.은행이름 = "SC은행"
        list = []
        for i in range (0, 11):
            i = randint(0, 9)
            list.append(i)
        num1 = str(list[0]) + str(list[1]) + str(list[2])
        num2 = str(list[3]) + str(list[4])
        num3 = str(list[5]) + str(list[6]) + str(list[7]) + str(list[8]) + str(list[9]) + str(list[10])
        num = num1 + "-" + num2 + "-" + num3
        self.계좌번호 = num
        
        Account.account_count += 1
        
kim = Account("김민수", 100)
print(Account.account_count)
lee = Account("이민수", 100)
print(Account.account_count)