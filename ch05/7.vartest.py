def vartest(a):
    a = a + 1  #지역 변수
    return a

a = 1  #전역 변
print(vartest(a))
print(a)
