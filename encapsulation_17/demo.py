#now we go with access modifies called private public protected
#access modifers are not used in python we go with naming only
class a:
 def __init__(self,a,b):
    self.a=a
    self.b=b
obj=a(10,20)
print(obj.a)
print(obj.b)
#now we go with private
class a:
 def __init__(self,a,b):
    self.__a=a
    self.__b=b
obj=a(10,20)
print(obj.a)
print(obj.b)    
#now we go with protected
class a:
 def __init__(self,a,b):
    self._a=a
    self._b=b
obj=a(10,20)
print(obj.a)
print(obj.b)  