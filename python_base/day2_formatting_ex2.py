# 사용자로 부터 원화 금액을 입력받아
# 환율을 적용해서 출력하시오
# https://open.er-api.com/v6/latest/USD (원달러당 각 나라의 환율정보)
krw_amount = float(input("원화 금액을 입력하세요 (원):"))
exchange_rate = 1382.09 # 현재 환율
# 원화 금액을 외화로 변환
# 결과 출력
print(f"원화 금액 {krw_amount}원")
print(f"환율:1달러당 {exchange_rate}원")
# 외화금액 출력
