# Calculator 를 확장한 MorcCalculator 클래스 만들기
from ch07.myclass.calculator import Calculator
# 제곱수를 계산하는 함수 추가
class MoreCalculator(Calculator):
    def pow(self):
        return self.x ** self.y

    def div(self):
        if self.y == 0:
           return 0
        else:
            return self.x / self.y

cal = MoreCalculator(3, 0)
print(cal.pow())
print(cal.sub())
print(cal.mul())
print(cal.div())
