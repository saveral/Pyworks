# abs(x) 직접 정의
# 절대값 알고리즘1
import math

def abs_sign(x) :
    if x < 0 :
         return -x
    else:
        return x

# 절대값2
def abs_square(x):
    y = x * x
    return math.sqrt(y)



n1 = abs_sign(-3)
n2 = abs_square(-3)
print(n1)
print(n2)
