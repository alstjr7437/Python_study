# 딕셔너리
# 쌍 2개가 하나로 묶인 구조
# 'apple : 사과' 이렇게 key와 value 두개로 설정 {}이용
#딕셔너리는 순서가 없음, 수정 삭제 가능

dic = {1:'a', 2:'b', 3:'c'}
print(dic)

student = {'학번':10, '이름':'홍길동','학과':'컴퓨터정보과'}
print(student)
student['연락처'] = '010-1111-2222'
print(student)
student['학과'] = '파이썬'
print(student)
del(student['학과'])
print(student)
print('----------------------------------')

print(student['이름'])           #없으면 오류 발생
print(student.get('이름'))       #없는것 입력해도 오류X
print(student.keys())           #dict_keys([key값]) 이렇게 반환
print(list(student.keys()))     #dict보기 싫으면 list 괄호 활용
print(student.values())         #value
print(list(student.values()))
print(student.items())          #items함수는 튜플형태로 나옴
print('이름' in student)         #딕셔너리 안에 있는지 반환
print('안녕' in student)