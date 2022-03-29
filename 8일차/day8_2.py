
while 1 :
    v = input("1. 입력한 수식 계산 2. 두 수 사이의 합계(나갈려면 exit를 입력하세요) :")
    if v == "exit" :
        break
    num = int(v)
    result = 0
    if num == 1 :
        a = input("수식을 입력 하세요 : ")
        result = eval(a)
        print(f"{a} 결과는 {result}입니다." )
    elif num == 2 :
        a = int(input("첫번째 수를 입력하세요 : "))
        b = int(input("두번째 수를 입력하세요 : "))
        for i in range(a, b+1) :
            result += i
        print(f"{a}부터 {b}까지의 합계는 {result}입니다.")
    else :
        print("1과 2중에 입력하세요")