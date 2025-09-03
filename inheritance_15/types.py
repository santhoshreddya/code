#diff types of inheritance single,multiple,mutlilevel,hierarcal,hybrid
#single inheritance
class father():
    def house(self):
        print("father has house")
class son(father):
    def car(self):
        print("son has car")
son_obj=son()
son_obj.house()
son_obj.car()
print("="*50)
#multi level inheritance
class grandfather:
    def land(self):
        print("10 acres of farming land")

class father(grandfather):
    def house(self):
        print("father has house")
class son(father):
    def car(self):
        print("son has car")
son_obj=son()
son_obj.land()
son_obj.house()
son_obj.car() 
#multiple inheritance single class inheriting multipe classes
class grandfather:
    def land(self):
        print("10 acres of farming land")

class father(grandfather):
    def house(self):
        print("father has house")
class mother():
    def gold(self):
        print("mother has 1kg gold")
class son(father,mother):
    def car(self):
        print("son has car")
son_obj=son()
son_obj.gold()
son_obj.land()
son_obj.house()
son_obj.car() 
print("="*50)
#hierarcal inheritance inheriting from one parent class
class grandfather:
    def land(self):
        print("10 acres of farming land")

class father(grandfather):
    def house(self):
        print("father has house")
class mother():
    def gold(self):
        print("mother has 1kg gold")
class son(father):
    def car(self):
        print("son has car")
class daughter(father):
    def business(self):
        print("has business")
daughter_obj=daughter()
daughter_obj.business()
daughter_obj.house()
son_obj=son()
#son_obj.gold()
son_obj.land()
son_obj.house()
son_obj.car() 
#hybrid inheritance getting multiple combination of multiple inheritance
class a:
    def fet1(self):
        print("feature 1")
class b(a):
    def fet2(self):
        print("feature 2")
class c(a):
    def fet3(self):
        print("feature 3")
class d(b,c):
    def fet4(self):
        print("feature 4")
obj=d()
obj.fet1()
obj.fet2()
obj.fet3()
obj.fet4()

