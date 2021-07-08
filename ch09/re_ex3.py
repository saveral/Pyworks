import re
# 태그를 추출 - 점(.) 임의의 문자 1개, *- 0개 이상 반복
str = "abcd<hr>Thank you"
pat = re.compile("(<.*>)")
m = re.findall(pat, str)
print(m)