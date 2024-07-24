# 로또번호 생성
# 1 ~ 45 중복되지 않은 6개 숫자
# 랜덤하게 자동 생성
import random

lotto_num = set() # 빈 set 선언
# 문자열의 길이나 시퀸스 자료형의 길이를 리턴하는 함수 len()
# set 길이가 6이 될 때까지
while len(lotto_num) < 6:
    number = random.randint(1, 45)
    lotto_num.add(number)
    print(f"행운의 로또 번호:{lotto_num}")

# 사용자에게 입력받은 수 만큼 로또번호 생성
cnt = int(input("몇 개 생성할까요?:"))
# 입력 수 만큼 반복
for i in range(cnt):
    user_lotto = set()
    while len(user_lotto) < 6:
        number = random.randint(1, 45)
        user_lotto.add(number)
        print(f"행운의 로또 번호:{user_lotto}")
        