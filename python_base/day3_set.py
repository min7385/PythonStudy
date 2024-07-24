# set: 중복을 허용하지 않음.
my_set = {1, 2, 2, 3, 4, 4, 5}
print(my_set)
# 요소 추가
my_set.add(6)
my_set.add(6)
print(my_set)
# 여러 데이터 추가
my_set.update([7, 8, 9])
# 요소 삭제
my_set.remove(1)
print(my_set)
# 전체 삭제
my_set.clear()
# 집합 연산
set1 = {"apple", "banana"}
set2 = {"banana", "cherry"}
intersection = set1 & set2 # 교집합
print(intersection)
union = set1 | set2 # 합집합
print(union)
differnce = set1 - set2 # 차집합
differnce2 = set2 - set1 # 차집합
print(differnce)
print(differnce2)
