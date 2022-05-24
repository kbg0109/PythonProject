#02

import random

baskin_num = 0
seq_counter_available = [1, 2, 3]

seq_selector = random.randint(0, 1)             #0(computer)과 1(you) 중 무작위 return

print('-------------------------')

while baskin_num < 31:
    if seq_selector == 0 :
        print('컴퓨터의 차례입니다.')
        computer_seq_counter = random.randint(1, 3)
        while computer_seq_counter > 0 :
            baskin_num += 1
            print('컴퓨터의 숫자는 {}입니다.'.format(baskin_num))
            computer_seq_counter -= 1
            if baskin_num == 31 :
                winner_counter = 1
                break
        seq_selector = 1
        print('-------------------------')
    elif seq_selector == 1 :
        print('당신의 차례입니다.')
        your_seq_counter = int(input('1에서 3까지 숫자를 입력해주세요. : '))

        if your_seq_counter not in seq_counter_available :
            print('오류')
        else :
            while your_seq_counter > 0 :
                baskin_num += 1
                print('당신의 숫자는 {}입니다.'.format(baskin_num))
                your_seq_counter -= 1
                seq_selector = 0
                if baskin_num == 31 :
                    winner_counter = 0
                    break
        print('-------------------------')
if winner_counter == 1 :
    print('당신이 이겼습니다.')
else :
    print('컴퓨터가 이겼습니다.')
