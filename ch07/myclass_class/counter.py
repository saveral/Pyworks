# Counter 클래스
class Counter:      #인스턴스(지역) 변수 역할을 함, 말 그대로 한번나오고 없어지고 한번나오고 없어짐
    def __init__(self):
        self.x = 0
        self.x = self.x + 1

    def showinfo(self):
        print(self.x)

c1 = Counter()
c1.showinfo()
c2 = Counter()
c2.showinfo()
c3 = Counter()
c3.showinfo()
