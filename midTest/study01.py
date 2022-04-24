print(1,2, end=" ")             #\n안하고 공백으로 띄우기
print(3,4)

print(1,2,3,4,5)
print(1,2,3,4,5,sep=",")        #사이에 ,넣기

f = open('out.txt', 'w')        #파일 열기
print(1,2,3,4,5, file=f)        #file 내용 넣기
f.close()                       #파일 닫기
open('out.txt').read()

print("%d" %123)        #바로 출력
print("%5d" %123)       #5칸으로 출력
print("%05d" %123)      #5칸으로 나머지 0 채워 출력
print("%7.1f" % 123.45) #7칸에 소수점 1까지 반올림

print("{0:d} {1:5d} {2:05d}".format(123,123,123))       #format으로 출력하기
print("{2:d} {1:5d} {2:05d}".format(111,222,333))       #format으로 출력하기(앞에 수는 순서)(함수 위치 인자)
print("{a}, {b}, {c}".format(a=100, b=200, c=300))      #format으로 출력하기(키워드 인자)

print('i love {} for "{}!"'.format('python','coding'))  #format 연습
print('{0} and {1}'.format('python','java'))
print('{1} and {0}'.format('python','java'))
print(r"\n \t \" \\를 그대로 출력")                       #r을 앞에 붙이면 그대로 출력

print(bin(11))  #2진수
print(oct(11))  #8진수
print(hex(11))  #16진수

a = 123
print(type(a))  #타입 출력
print(f"a is {a},{20},{30}")        #f-string연습
print('\hello')
print('I don\t know')
print(r'c:\user\bin')
print("""\
line1
line2
line3\
""")

