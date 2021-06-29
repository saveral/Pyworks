# 간결하게 할 수 있는 lambda 함수


def oneup2(x):
    return x + 1
print(oneup2(2))   # 일반 함수 호출

# 매개변수가 1개 있는 lambda 함수(익명 함수)
# 1을 더하는 함수
oneup1 = lambda x : x + 1
print(oneup1(2))   # 람다 함수 호출
print((lambda x : x + 1)(2)) # 함수 안에다 통으로 집어 넣음

# 3의 배수를 계산 함수
times = lambda n : n * 3
print(times(2))
print((lambda n : n * 3)(2))


