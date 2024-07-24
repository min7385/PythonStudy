# for문은 반복적으로 코드를 실행하는데 사용됨.
# 코드의 중복을 줄이고, 효율성을 높이며, 데이터 집합을 처리하기 위함.

# 방법1 기본 for문: 시퀸스(list, tuple, str)의 각 요소를 하나씩 순회하며 실행
# 리스트 순회
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)
word = "Hello"
for letter in word:
    print(letter)
# 방법2 단순 반복 range() 일정 범위로 반복
# 0 ~ 4 숫자 순회
for i in range(5):
    print(i)
print("=" * 10)
# 1 ~ 5까지
for i in range(1, 6):
    print(i)
print("=" * 10)
# 1 ~ 10까지 2씩 증가하며
for i in range(1, 11, 2):
    print(i)
# enumerate() 인덱스와 값이 동시에 필요할 때
for idx, val in enumerate(nums):
    print(f"index:{idx} value:{val}")

dan = int(input("원하는 구구단은?:"))
for i in range(1, 10):
    print(f"{dan} X {i} = {dan * i}")

# 중첩 for문 (for문 안에 for문)

for i in range(2, 10): # 2단부터 9단까지 반복
    print(f"{i}단 ========")
    for j in range(1, 10): # 각 단에서 1부터 9까지 반복
        print(f"{i} X {j} = {i * j}")
