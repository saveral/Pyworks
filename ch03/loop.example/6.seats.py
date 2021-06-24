# 자리 배치


customer_num = int(input("입장객 수 입력 : "))
cul_num = int(input("좌석 열의 수 입력 : "))


if customer_num % cul_num == 0:
    row_num = int(customer_num/cul_num)   # 나머지는 결과가 실수이므로 정수처리필요
else:
    #row_num = int(customer_num/cul_num + 1)
     row_num = customer_num // cul_num + 1

print(row_num, "개의 줄이 필요합니다.")

print("자리 배치도")
for i in range(0,row_num):     
    for j in range(1,cul_num + 1): #range함수 끝은 앞이 1이면 -1뺀 숫자가 출력되니 추가 +1을 해주는거 알제?
        
        seat_num = i*cul_num+j
        print(seat_num,end=' ')       
        if seat_num >= customer_num:                  
            break
        
    print()
