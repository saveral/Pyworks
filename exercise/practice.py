numbers = [1,2,3,4,5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)

numbers = [1,2,3,4,5]
result = [n*2 for n in numbers if n%2==1]
print(result)

A = [70, 60, 55, 75,95, 90, 80, 80, 85,100]
total = 0
for score in A:
    total += score
average = total/len(A)
print(average)

numbers = [1,2,3,4,5]

result = [n*2 for n in numbers if n % 2 ==1]
print(result)

import random
result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)

print(result)