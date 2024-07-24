# 2차원 리스트 순회
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for element in row:
        print(element)

# 두 리스트 병렬 순회
names = ["nick", "jack", "alice"]
score = [85, 90, 95]
for nm, num in zip(names, score):
    print(f'{nm}:{num}')

# 
for idx, val in enumerate(names):
    print(f'{val}:{score[idx]}')

# dict 키를 이용한 for문
stu = {"nick": 85, "jack": 90, "alice": 95}
print(stu.keys())
for key in stu.keys():
    print(stu[key])
# items() 모든 아이템 순회
for key, val in stu.items():
    print(f"{key}:{val}")