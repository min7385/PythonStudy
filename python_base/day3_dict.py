# 딕셔너리
person = {"nm" : "nick", "age" : 20}
# 요소접근은 key로
print(person["nm"])
# 요소 수정도 key로
person["nm"] = "jack"
print(person["nm"])
#요소 삭제
del person["nm"]
print(person)
print(type(person))

# 학생정보
stu = [{"nm":"팽수", "age":10}
       ,{"nm":"동길", "age":20}
       ,{"nm":"길수", "age":15}]
print(stu)
print(stu[0])
print(stu[0]["nm"])
