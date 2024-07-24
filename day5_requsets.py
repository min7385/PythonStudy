import requests
api_url = 'https://open.er-api.com/v6/latest/USD'
response = requests.get(api_url)
data = response.json() # json 데이터 파싱
# 환율정보
# print(data['rates'])
# print(data['rates']['KRW'])
# for key in data['rates'].keys():
#    print(f"{key}:{data['rates'][key]}")
usd_to_krw = data['rates']['KRW']
while True:
    msg = input("달러를 입력하세요(종료 q):")
    if msg == 'q':
        break
    amount_usd = int(msg)
    amount_krw = amount_usd * int(usd_to_krw)
    print(f"{amount_usd} 달러는 원화로 {amount_krw:,}원 입니다.")