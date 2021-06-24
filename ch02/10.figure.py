# 정사각형의 넓이

size = int(input("한변의 길이 :"))
area = size*size
#print("정사각형의 넓이 : ", area,"cm")
print("정사각형의 넓이 : %dcm" % area)   #cm가 떨어져서 붙이는 방법




# 삼각형의 넓이
width = int(input("밑변의 길이 : "))
height = int(input("높이 : "))
area = (width * height)/2
#print("삼각형의 넓이(cm넓은) : ",area,"cm")
print("삼각형의 넓이(cm좁은) : %dcm" % area)

