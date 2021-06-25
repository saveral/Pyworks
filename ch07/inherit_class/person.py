# Person 클래스 - 멤버 변수(name, age)
# Employee는 Person의 상속을 받음

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    pass

if __name__ == "__main__":
    p1 = Person("한강",25)
    print(p1.name, p1.age)

    e1 = Employee("북한강", 30)
    print(e1.name, e1.age)

