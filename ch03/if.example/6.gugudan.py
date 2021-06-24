# 구구단 5단 출력하기


for i in range(1,11):
    print("4 x %d = %d" % (i,4*i)) # %d %d의 값을 뒤에 % (x,y)로 넣어준


dan = int(input("단을 입력하세요 : "))
for i in range(1,11):
    print("%d x %d = %d" % (dan, i, dan*i))
