money, a, b, c, d = 0, 0, 0, 0, 0
while 1:
    money = int(input("교환할 돈은 얼마?"))
    if(money == 0) :
        break
    a = money // 500
    money %= 500
    b = money // 100
    money %= 100
    c = money // 50
    money %= 50
    d = money // 10
    money %= 10

    print(f"500원 짜리 {a}")
    print(f"100원 짜리 {b}")
    print(f"50원 짜리 {c}")
    print(f"10원 짜리 {d}")
    print(f"바꾸지 못한 돈 {money}")

