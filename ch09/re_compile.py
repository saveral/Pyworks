# 정규 표현식 예제
import re

p = re.compile('a.b')  # +는 반복을 의미하는 메타 문자
m = p.match('a3b')
print(m)