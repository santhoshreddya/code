#property fun we use in pythonic way 
class student:
    def __init__(self,age):
        self.__age=age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        if age<0:
            print("invalid age")
        else:
            self.__age=age
s=student(30)
print(s.age)
s.age=25
print(s.age)
s.age=22
print(s.age)
