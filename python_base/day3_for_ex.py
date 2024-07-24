# python에서 import문은 다른 모듈이나 라이브러리를
# 현재의 파이썬 프로그램으로 가져와서 사용할 수 있게 함.
import random
# random값을 생성하는 모듈
# 0.0에서 1.0 사이의 난수(float)를 반환
print(random.random())
# a, b 포함 정수를 랜덤하게 변환
print(random.randint(1, 45))

# 구구단 게임: 랜덤한 구구단 문제를 주고, 사용자 입력값이 맞으면 '정답', 틀리면 '오답' 출력
dan = random.randint(2,9) # 2 ~ 9 중 랜덤값
num = random.randint(1,9) # 1 ~ 9 중 랜덤값
# 문제 출력
print(f"{dan} X {num} = ?")
dab = dan * num
# 사용자 입력 받기
answer = int(input("답을 입력하시오."))
if dab == answer:
    print("정답입니다.")
else:
    print(f"오답입니다. 정답은 {dab}입니다.")
print("게임을 종료합니다.")
