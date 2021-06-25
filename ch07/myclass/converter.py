# 단위 변환 클래스
class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor

    def convert(self, val):
        return self.factor * val


c1 = ScaleConverter("inches", "mm", 25)
print("Converting 2 inches")
print(str(c1.convert(2)) + c1.units_to)     # str로 int보다 크게 만들어서 숫자 + 문자를 붙일 수 있게함