# 딕셔너리

person = {}
print(person)


person['name'] = "이순신"
person['age'] = 40
print(person)

person['address'] = "전라도"
print(person)

# dic의 value 출력
for key in person:
    print(person[key])
    
# 요소 삭제 : dic.pop('address')
del person['address']
print(person)
