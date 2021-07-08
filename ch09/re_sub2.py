# 주민번호 뒷자리를 *로 표시
import re
data = """  
주석이 아니고 멀티라인
 kim 871212-1234567
 lee 951011-2345678
"""

pat = re.compile("(\d{6})[-]\d{7}")
m = pat.sub("\g<1>-*******", data)
print(m)