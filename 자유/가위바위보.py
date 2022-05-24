#01

import random

sel = ['가위', '바위', '보']
result = {0:'draw', 1:'win', 2:'lose'}

while True:
    your_choice = str(input('가위바위보를 시작합니다. 가위, 바위, 보 중 하나를 입력하세요. : '))
    if your_choice not in sel :
        print('가위, 바위, 보 중 하나를 입력해주세요.')
        continue

    else :
        computer_choice = random.choice(['가위', '바위', '보'])  # 리스트에서 무작위 문자열 return

        if computer_choice == your_choice:                              #비기면 draw
            state = 0
        elif computer_choice == '바위' and your_choice == '보':
            state = 1
        elif computer_choice == '보' and your_choice == '가위':
            state = 1
        elif computer_choice == '가위' and your_choice == '바위':
            state = 1
        else :                                                          #지면 lose
            state = 2
        print('컴퓨터의 선택 : {}'.format(computer_choice))
        print('당신의 선택 : {}'.format(your_choice))
        print('승부 결과 : {}'.format(result[state]))

    restart = input('다시 하려면 yes를 입력해주세요. : ')
    if restart == 'yes' :
        print('처음으로 돌아갑니다.')
        continue
    else :
        print('종료합니다.')
        break