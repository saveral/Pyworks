
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    #pass
    def fly(self):
        print("독수리가 하늘을 높이 납니다. ")
eagle = Eagle()
eagle.fly()