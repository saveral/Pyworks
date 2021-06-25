# 학생 클래스 hide 생성과 사용
class Student:
    def __init__(self, sid, name):
        self.__sid = sid     # 학번
        self.__name = name

    def getsid(self):
        return self.__sid
    def getname(self):
        return self.__name


if __name__ == "__main__":   # main(원본)이 아닌 곳에서 출력하면 안나오게 함
    s1 = Student(1001,"박대양")
    print(s1.getsid(), s1.getname())
    s2 = Student(1002, "이산")
    print(s2.getsid(), s2.getname())
