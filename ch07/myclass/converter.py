# 단위 변환 클래스
# inch -> mm로 바꾸는 클래스(1 inch - 2.54cm)
class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor

    def convert(self, val):  # self.factor : 25
        return self.factor * val

if __name__=="__main__":
    c1 = ScaleConverter("inches", "mm", 25)
    print("Converting 2 inches")
    print(str(c1.convert(2)) + c1.units_to)     # str로 int보다 크게 만들어서 숫자 + 문자를 붙일 수 있게함