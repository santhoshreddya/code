#accessing private in outside class
#now we go with private access
class A:
 def __init__(self,a,b):
    self.__a=a
    self.__b=b
obj=A(10,20)
print(obj._A__a)  #these is called name mangling technique in python in java direct access modifiers strict
print(obj._A__b)



