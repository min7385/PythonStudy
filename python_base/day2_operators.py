# 비교 연산자 >, <, >=, <=, ==, !=
# 비교 연산자는 두 값을 비교하여 True or False로 반환

a = 10
b = 20
c = 10
print(a == b) # false
print(a == c) # true
print(a != b) # true
print(a != c) # false
if a == b:
    print("같음")
else:
    print("같지 않음")
print("종료")
if True: # 조건이 True이기 때문에 출력됨.
    print("hi")

# 나이가 20살 이상이면, 입장가능
age = int(input("나이를 입력하세요:"))
if age >= 20:
    print("입장 가능합니다.")
else:
    print("다음 기회에...")
# 논리 연산자 and, or, not
x = True
y = False
print("x and y:", x and y) # false
print("x and x:", x and x) # true   and 둘다 true일 경우
print("x or y:", x or y) # true
print("x or x:", x or x) # true
print("y or y:", y or y) # false
print("a < b and b < c:", a < b and b < c) # false
print("a < b and b > c:", a < b and b > c) # true

gender = input("성별은?")
age = input("나이는?")
# 남자이면서 10살 이상만
if gender == "남자" and age >= 10:
    print("대상자입니다.")
else:
    print("대상자가 아닙니다.")

email = "leeapgil@gmail.com"
if '@' in email:
    print("email 형식입니다.")
else:
    print("email 형식이 아닙니다.")