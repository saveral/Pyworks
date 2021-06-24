# 1번 문제

sub1 = 80
sub2 = 75
sub3 = 55
sum = sub1 + sub2 + sub3
avg = sum/3
print("과목 평균 = ",avg)

'''
국어 = 80
영어 = 75
수학 = 55
평균 = (국어 + 영어 + 수학) / 3
print("평균 : " , 평균)
'''

# 2번 문제

n = 13
if n% 2 == 0:
    print("짝수")
else:
    print("홀수")


# 3 ~ 4번 문제
pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:]

print(yyyymmdd)
print(num)


gender = pin[7]
#print(gender)   #성별 구분 문자
if gender == "1":
    print("남자입니다")
else:
    print("여자입니다.")


# 5번
a = "a:b:c:d"
b = a.replace(":",'#')
print(b)

# 6번
a = [1, 3, 5, 4, 2]
a.sort() # 오름차순 정렬
a.reverse() #내림차순 정

print(a)

# 7번
a = ['life', 'is', 'too', 'short']
result = " ".join(a)
print(result)


# split() 예제
msg = "Life is too short"
msg = msg.split() # 구분기호가 공백이다.
print(msg)

s = "a:b:c:d"
s = s.split(':')
print(s)

# 8번
a = (1, 2, 3)
a = a+ (4,)
print(a)

# 9번
a = dict()

print(a)

# 10번
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B') # 삭제
print(a)
print(result)

# 11번
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a) # 중복 제거
b = list(aSet) # list형으로 변환
print(b)

# 12번
a = b = [1, 2, 3]
a[1] = 4
print(a)
print(b)
