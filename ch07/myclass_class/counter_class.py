# Counter 클래스 - 클래스 변수 사용
class Counter:
    x = 0   # 클래스 변수(전역 변수 역할을 함. 즉, 우려먹고 붙어서 또 우려먹는 것임)

    def __init__(self):   # init를 빼먹지 말자(몇번째여)
        Counter.x += 1

    def showinfo(self):
        print(self.x)

c1 = Counter()
c1.showinfo()
c2 = Counter()
c2.showinfo()
c3 = Counter()
c3.showinfo()