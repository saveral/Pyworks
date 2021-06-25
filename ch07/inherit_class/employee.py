from person import Person

# 멤버 매개변수가 있는 상속

"""class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age """

class Employee(Person):
    def __init__(self, name, age, empid):
        super().__init__(name, age)     # Super().__init__ 을 사용하여 부모 멤버를 상속받는다.
        self.empid = empid



e1 = Employee("북한산", 20, 201)
print(e1.name, e1.age, e1.empid)

e2 = Employee("금강", 30, 202)
print(e2.name, e2.age, e2.empid)

