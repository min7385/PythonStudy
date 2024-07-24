# python은 oop 객체지향 프로그래밍을 지원함.
# class는 객체를 만드는 설계도
# 객체는 class를 인스턴스화 해서 생성함.

class CoffeeFranchise:
    #init 생성자라고 하며 class를 인스턴스화 할 때
    # 필요한 인자값이 있다면 정의해야함(없으면 생략)
    def __init__(self, nm, beans=None, menu=None):
        self.branch_name = nm
        self.beans = beans
        self.menu = menu
        
    def make_ame(self): # class에 종속되어 있는 함수를 메서드라 함.
        if self.beans:
            print(f"{self.branch_name}에서는 {self.beans}(으)로 커피를 만들어요.")
        else:
            print(f"{self.branch_name}에서는 신선한 커피를 제공합니다.")
future = CoffeeFranchise("미래융합점", "미래 블렌드", "미래 라떼")
city = CoffeeFranchise("둔산점")
print(f"인스턴스1: {future.branch_name}, 인스턴스2: {city.branch_name}")
future.make_ame() # 인스턴스 메서드 호출
city.make_ame()