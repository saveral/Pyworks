
# 1번(p.262)
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

class UpgradeCalculator(Calculator): # Cal을 상속받는 거임

    def sub(self,val):
        self.value -= val
        return self.value

class MaxlimitCalculator(Calculator):

    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
        return self.value

c = Calculator()
print(c.add(10))
print(c.value)

cal = UpgradeCalculator()
print(cal.add(10))
print(cal.sub(7))
print(cal.value)

cal2 = MaxlimitCalculator()   # 조건문 생생하여 100이상은 100으로 나오게함
print(cal2.add(50))
print(cal2.add(60))
print(cal2.value)


A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A:
    total += score
average = total/len(A)
print(average)

