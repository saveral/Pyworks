'''# 1번(p.179)
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

input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)

# 4번
print("you""need""python")
print("you"+"need"+"python")
print("you","need","python")
print("".join(["you","need","python"]))"""


# 5번
f1 = open("test.txt",'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt",'r')
print(f2.read())
f2.close()


# 6번
user_input = input("저장할 내용을 입력하시오:")
f = open('test.txt','a')
f.write(user_input)
f.write('\n')
f.close()
'''

# 7번
f = open('test.txt','r')
body = f.read()
f.close()

body = body.replace('java','python')

f = open('test.txt','w')
f.write(body)
f.close()