# 반복문 while <조건식>이 True일 경우만 반복 False면 종료
i = 1
while i <= 5:
    print(i)
    i += 1 # 반복마다 1씩 증가
# break: 특정 조건일 때, 종료
i = 1
while True:
    print(i)
    if i >= 3:
        break
    i += 1
while True:
    nm = input("이름을 입력하세요(종료q):")
    if nm == "q":
        break
    print(f"{nm}님이 입장하셨습니다.")
print("종료 되었습니다.")
