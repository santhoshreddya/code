#method resoluton order is nothing but it occurs in multiple inheritance when there is same method name or class name it goes with rules shown in mro
class a():
    def show(self):
        print("show case a found")
class b():
    def show(self):
        print("show case b found")
class c(b,a):              #multiple inheritance
    pass
obj=c()
obj.show()
print(c.mro())
#now we seeing use cases of super() when there is common method names to get parent class
class parent():
    def greet(self):
        print("hii aksh hru")
class child(parent):
    def greet(self):
        super().greet()
        print("hii aarth hru")
        
obje=child()
obje.greet()


