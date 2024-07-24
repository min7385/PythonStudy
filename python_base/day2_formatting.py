# 문자열 포맷팅
# 문자열 유형의 서식 데이터를 만들고,
# 서식안에 데이터를 대입하는 방법

# 방법1. 기본 포맷팅(%연산자 사용)
nm = "Nick"
age = 30
formatted_str = "My name is %s and I am %d years old." % (nm, age)
print(formatted_str)
num = 123.456789
formatted_str2 = "The number is %.3f" % num
print(formatted_str2)
# 방법2. str.format() 함수 사용
formatted_str3 = "My name is {0} and I am {1} years old.".format(nm,age)
print(formatted_str3)
# 방법3. (f-strings) 파이썬 3.6 이상에서 사용가능
print(f"my name is {nm} and I am {age} year old.")
