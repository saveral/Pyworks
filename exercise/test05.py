
# 1번(p.262)
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

class UpgradeCalculator(Calculator):  # Cal을 상속받는 거임

        def sub(self, val):
            self.value -= val
            return self.value
cal = UpgradeCalculator()
cal.add(10)
cal.sub(7)

print(cal.value)
# 2번

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



# 3번

# 4번
def positive(a):
    a2 = []
    for i in a:
        if i >= 0:
            a2.append(i)
    return a2


li = [1, -2, 3, -5, 8, -3]
li2 = positive(li)
print(li2)
#print(list(filter(lambda x : x >= 0, li))) - 람다식으로 간편하게 가능


# 5번

# 6번
def times(a):
    a2 = []
    for i in a:
        a2.append(i*3)
    return a2

li = [1, 2, 3, 4]
li2 = times(li)
print(li2)
print(list(map(lambda x : x*3, li)))