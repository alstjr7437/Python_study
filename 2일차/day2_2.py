def add(a, b) :
    c = a + b
    return c
def minus(a, b) :
    c = a - b
    return c
def multi(a, b) :
    c = a * b
    return c
def divide(a, b) :
    c = a / b
    return c
while(1) :
      a = input("1st input?")
      if a == "0000" :
          break;
      a = int(a)
      b = int(input("2nd input?"))

      c = input("어떤것을 하실건가요")

      if(c == "더하기") :
          print("더하기 = ", add(a,b))
      elif(c == "빼기") :
          print("빼기 = ", minus(a,b))
      elif(c == "곱하기") :
          print("곱하기 = ", multi(a,b))
      elif(c == "나누기") :
          print("나누기 = ", divide(a,b))
    
