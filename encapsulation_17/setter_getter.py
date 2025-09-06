#by usng setter update the data by using getter read the data if there is strict encapulation
class student:
    def __init__(self,age):
        self.__age=age
obj=student(22)
print(obj._student__age) #direct access private name mangling
obj._student__age=-5  #updating private
print(obj._student__age)
#now we go with setter and getter method 
class studen:
    def __init__(self,age):
        self.__age=age
    def set_age(self,age):
        if age<0 :
            print("invalid age")
        else:
            self.__age=age
    def get_age(self):
        print(self.__age) 
obje=studen(25)
obje.set_age(-5)
obje.get_age()



 