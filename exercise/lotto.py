import random
n = random.randint(1, 10)

# 주사위 10번 던지기
dice= []
for i in range(0,10):
    n = random.randint(1, 6)
    dice.append(n)

print(dice)

# 로또 복권 생성기
lotto = []
while len(lotto) < 6:
    print(len(lotto))
    n = random.randint(1, 45)
    if n not in lotto:   # 중복 숫자 방지
        lotto.append(n)

print(lotto)