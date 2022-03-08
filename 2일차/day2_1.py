while(1) :
      a = input("1st input?")
      if a == "0000" :
          break;
      a = int(a)
      
      b = int(input("2nd input?"))
      result = a + b
      print(a, "+", b, "=", result)
      result = a - b
      print(a, "-", b, "=", result)
      result = a * b
      print(a, "*", b, "=", result)
      result = a / b
      print(a, "/", b, "=", result)

print("exit")
