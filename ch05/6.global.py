# 전역변수(정적변수)
# global 키워드 사용

x = 0
def one_up():
    global x  # x를 전역변수로 사용
    x = x + 1
    return x

print(one_up())
print(one_up())
print(one_up())
