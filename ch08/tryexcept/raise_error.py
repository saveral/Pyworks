
class Bird:
    def fly(self):
        #print("새가 날아갑니다.")
        raise NotImplementedError

class Eagle(Bird):
    #pass
    def fly(self):
        print("독수리가 하늘을 높이 납니다. ")

#bird = Bird()
#bird.fly()
eagle = Eagle()
eagle.fly()