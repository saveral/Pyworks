import sys

print('수를 입력하세요 : ')
n = int(input())
if n == 0:
    print("0으로 나룰 수 없습니다.")
    sys.exit()     # Error를 안나오게 한다

print(3 / n)
