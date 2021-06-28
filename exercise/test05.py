
# 1번(p.262)
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator): # Cal을 상속받는 거임

    def sub(self,val):
        self.value -= val


c = Calculator()
c.add(10)
print(c.value)

cal = UpgradeCalculator()
cal.add(10)
cal.sub(7)
print(cal.value)