# 파일 열기 (open()) -> 파일 쓰기(write()) -> 파일 닫기(close())
f = open('c:/pyfile/hello.txt', 'w')
f.write("Hello~ python\n")
#f.write(1000)  # 숫자는 직접적으로 입력 불가 - 포맷 방식으로 입력해야함
f.write("%d\n" % 100) # 숫자는 %d 형식으로 넣어야함
f.write("%.1f\n" % 7.3)
num = "%d\n" % 100000 # 또는 num이란 변수를 지정해서 입력해준다(틀은 같음)
f.write(num)
f.write("안녕~파이썬")

f.close()