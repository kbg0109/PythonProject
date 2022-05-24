#예제

import random

chance_left = 4
quiz_answer = random.randint(1,20)              #1부터 20까지 정수 중 랜덤하게 return

while True :
    if chance_left > 0 :
        your_answer = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(chance_left)))
        if quiz_answer != your_answer :
            if quiz_answer < your_answer :
                chance_left -= 1
                print("Down")
            elif quiz_answer > your_answer :
                chance_left -= 1
                print("Up")
        elif quiz_answer == your_answer :
            print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(5-chance_left))
            break
    elif chance_left == 0 :
        print("아쉽습니다. 정답은 {}입니다.".format(quiz_answer))
        break