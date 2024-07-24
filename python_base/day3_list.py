# list(배열)
# 동적 배열로 타입이 자유로움
arr = [1, "nick", [2, 3, [4, 5]]]
# 인덱스로 요소에 접근
print(arr[1]) # nick
print(arr[-1]) # [2, 3]
print(type(arr))
print(arr[2][1]) # 3
print(arr[2][2][0]) # 4
arr[1] = "jack"
print(arr)
# 추가
arr.append("추가요소")
# 삭제
del arr[0]
print(arr)
# 반복
repated = arr * 5
print(repated)
