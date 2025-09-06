#here same class with differnt function calling with object inputs
#many forms with single entity
#same method with differnt behavior calling with object names
class dog:
    def speak(self):
        print("speak like bow")
class cat:
    def speak(self):
        print("speak like meow")
obj1=dog()
obj2=cat()
obj1.speak()
obj2.speak()
#predefined use cases
print(len("hello"))
print(len([1,2,3]))
print(len({"A":1,"b":2}))
#now we go with operator overloading method overloading does not occur in python
print(2+3)
print("hi"+"hello")
print([1,2,3]+[4]) #here method is same but functionality diff based on input given it will call to its obj
#common use case functinality
class circle:
    def area(self):
     return 3.14 * 5 * 5
class square:
    def area(self):
     return 5*5
def print_area(shape):
   print("area is =", shape.area())
print(print_area(circle()))
print(print_area(square()))
#now we going with database connection functionality changes
class mysql:
   def database(self):
      return "connected to mysql"
class postgressql:
   def database(self):
      return "connected to postgressql"
def connection(db):
   print("database" ,db.database())
connection(mysql())
connection(postgressql())
#now we go with method overloading supported in java and c not in python
class mathops:
   def add(self,a,b):
      return a+b
   def add(self,a,b,c):
      return a+b+c
objec=mathops()
#print(objec.add(1,2))#it will call  to latest one in java based on parameters it called
print(objec.add(1,2,3))



