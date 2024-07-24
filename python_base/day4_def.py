# python 함수 def로 선언
def adder(a, b):
    sum = a + b
    return sum
def test():
    print("매개변수와 리턴값 없음.")
# 매개변수와 리턴은 없을 수 있음
print(adder(1, 10))
n = adder(10, 2)
print(n)
test()
# return 0 ~ n개 가능
def fn_name():
    return 10, 100
a, b = fn_name()
print(a, b)
# 디폴트 매개변수
def fn_default(nm, level=1):
    print(f"이름:{nm} 레벨:{level}")
fn_default("nick")
fn_default("jack", 100)

# 가변 매개변수(0 ~ n개)
# + 더하기, * 곱하기 연산 후 리턴
def fn_calculator(operator, *args): # *args 튜플형태로 전달됨.
    result = 5
    if operator == "+":
        for n in args:
            result += n
    else:
        result = 1
        for n in args:
            result *= n
    return result
print(fn_calculator("+", 1, 2, 3, 4, 5, 6))
print(fn_calculator("*", 10, 2))
