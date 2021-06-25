# 1번(p.179)
def is_odd(number):
    if number % 2 ==1:
        return True
    else:
        return False
num = is_odd(11)
print(num)

# 2번
# 가변 매개변수(파이썬에만 있음)
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
        print(i, result)  # 즉 result가 sum이 됨, 값을 모르겠으면 중간에 print출력 해보길
    return result / len(args)

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))

# 3번
"""
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)

# 4번
print("you""need""python")
print("you"+"need"+"python")
print("you","need","python")
print("".join(["you","need","python"]))"""


