# 사용자에게 문장을 입력 받아 줄임말을 만들어주세요.
# 갑자기 분위기 싸함 <-- 입력
# 갑분싸            <-- 출력
# 1. 입력받기
msg = input("문장을 입력하세요").split()
print(msg)
# 2. 특정 기준으로 문자열 자르기
# 3. 자른 문자만큼 반복하며 첫글자 더하기
message = ""
for n in msg:
    message += n[0]
# 4. 출력
print(message)