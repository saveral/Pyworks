import sys

#Terminal에서 경로로 myargv.py 실행 -> python myargv.py cow cat dog 입력
args = sys.argv[1:]  # 리스트형 자료 - 1인덱스부터 시작이라 본인 이름은 빼고 1부터 출력됨
print(args)
sum = 0

for i in args:
    sum = sum + int(i)

print(sum)