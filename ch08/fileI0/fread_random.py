# kbo 구단을 1개씩 랜덤 추출하기
import random

try:
    f = open('c:/pyfile/2021kbo.txt','r')
    data = f.read().split()  # 공백문자로 구분(삼성 - 1개로 인식, split없으면 삼, 성 으로 인식함)
    print(data)
    
    team = random.choice(data)  # 랜덤하게 리스트중 하나를 선택
    print(team)

    f.close()
except FileNotFoundError as e:
    print(e)