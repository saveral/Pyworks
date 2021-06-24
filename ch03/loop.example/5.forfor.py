# 중첩 for 문
# 5행 5열의 배열
for i in range(1,6):
    for j in range(1,6):
        print("가",end=' ')
    print()  #한줄 띄기 

# 1부터 1씩 증가하기
for i in range(0,6):
    for j in range(1,6):
        num = i*5 + j
        if num < 10:
            print(end = ' ')
        
        print(i*5 + j, end=' ')
        
    print()  #한줄 띄기 
