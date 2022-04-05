import random

tries = 0
guess = 0
answer = random.randint(1, 100)

print("1부터 100사이의 숫자를 맞추시오")

while guess != answer:
    tries = tries + 1
    if(tries > 10) :
        break
    guess = int(input("숫자릅 입력하시오:"))
    if guess < answer :
        print("너무 낮음")
    elif guess > answer:
        print("너무 높음")
if guess == answer :
    print("축하 시도 = ", tries)
else :
    print("정답은", answer)