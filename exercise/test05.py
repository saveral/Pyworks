
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

# 7번

def find_max(li): # 방법1
    max = li[0]  #-8
    for i in li:
        if max < i
            max = i
    return max

     방법2
    n = len(li)
    for i in range(n):
        if max < li[i]:
            max = li[i]
    print(max)
    return max


# max값 구하기

d1 = [-8, 2, 7, 5, -3, 5, 0, 1]

max = find_max(d1)
print(max)

max = max(d1)
min = min(d1)

print(max)
print(min)
print(max + min)


# 12번
import time
import datetime
now1 = datetime.datetime.now()
print(now1.strftime("%Y/%m/%d %H:%M:%S"))

now2 = time.strftime("%Y/%m/%d %H:%M:%S")
print(now2)

