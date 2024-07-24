# 문자열 인덱싱
# 문자열 인덱스는 0부터 시작
text = "Hello, world!"
print(text[0]) # H
print(text[7]) # W
print(text[-1]) # !
# 문자열 슬라이싱
text = "Python Programming"
# [start:end:step] default 1
print(text[0:6]) # 0인덱스부터 6인덱스 전까지
print(text[7:18]) # Programming
print(text[7:]) # 7인덱스부터 끝까지
print(text[:6]) # 처음부터 6인덱스 전까지
print(text[0:6:2]) # Pro 0 ~ 5까지 2칸씩 건너뛰며
print(text[::2]) # 처음부터 끝까지 2칸씩 건너뛰며
print(text[::-1]) # 뒤에서부터 처음까지
# 문자열 함수 find(str) 찾고자하는 문자열 str의 인덱스를 리턴 없으면 -1 리턴
email = input("이메일 주소를 작성해주세요:")
print(email.find('@'))
# @를 구분으로 id 와 domain을 분리해서 출력하시오 (슬라이싱을 이용하면 편함.)
idx = email.find('@')
id = email[:idx]
domain = email[idx+1:]
print(f"id:{id}, domain:{domain}")
