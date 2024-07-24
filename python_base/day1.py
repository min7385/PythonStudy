print('test')
# comment 주석 (단축키 ctrl + /)
# 주석은 코드실행에 영향을 주지 않음.
'''
comment 주석 (단축키 ctrl +/)
주석은 코드실행에 영향을 주지 않음.
'''
# python은 들여쓰기를 하지 않으면 오류남.
if True:
    print('hi')
# Date Type(자료형)
# 숫자형(numeric type) 정수(int) 실수(float)
print(10)
# type함수는 해당 데이터의 타입을 리턴함.
print(type(10))
print(type(10.10))
# 산술 연산자를 활용하여 사칙연산 가능
# +, -, *, /
# % 나머지 반환
# // 몫 반환
# ** 제곱 반환
print('나머지:' , 12 % 5)
print('몫:' , 15//4)
print('제곱:', 2**4)
# 문자열형의 특징
print('가나다'+'라마바사') # 문자열 더하기 가능
print('hi'*10) # 문자열 곱하기 가능
# 문자열은 str
print(type('hi'))
print(" Tom's Diner ")

# 변수(variable, var) 데이터에 붙이는 이름표
# python 변수의 특징: 동적타입(변수 타입을 명시하지 않아도 인식함)
my_num = 3    # 변수 my_num에 3 할당
print(my_num, type(my_num))
my_num = 3.10 # 다시 할당 가능
print(my_num, type(my_num))
my_num = "3.10"
print(my_num, type(my_num))
# 형변환 int to str, str to int... int(), float(), str()
my_num = float(my_num)
print(my_num, type(my_num))

a = 10
b = input("정수를 입력해주세요:")
print(a + int(b))
# 오늘의 문제 !!
# 메세지와 정수를 입력받아 정수 만큼 메세지를 출력하는 코드를 작성하시오
a = input("메세지를 입력해주세요:")
b = input("정수를 입력해주세요:")
print(a*int(b))
