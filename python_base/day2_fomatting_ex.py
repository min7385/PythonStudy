# 할인 퍼센트와 물품의 금액을 입력받아
# 할인 금액과 최종 금액을 계산하여
# 출력하는 프로그램을 작성하시오.

# 사용자로 부터 입력
original_price = float(input("상품 금액:"))
dis_percent = float(input("할인 퍼센트(예: 20% 20입력):"))
# 할인 금액 계산   원가 * (할인율 / 100)
dis_amount = original_price * (dis_percent / 100)
# 최종 금액 계산   원가 - 할인 된 금액
final_price = original_price - dis_amount
# 결과 출력
print(f"원가: {original_price}원")
print(f"할인 퍼센트:{dis_percent}%")
print(f"할인 금액 : {dis_amount:.2f}원") # 소수점 둘째 자리까지 출력
print(f"계산할 금액 : {final_price}원")
