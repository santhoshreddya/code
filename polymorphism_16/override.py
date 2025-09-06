#overriding is nothing but 
class animal:
    def sound(self):
        print("sound like animal")
class dog(animal):
    def sound(self):
        print("sound like dog")
class cat(animal):
    def sound(self):
        print("sound like cat")
a=animal()
d=dog()
c=cat()
a.sound()
d.sound()
c.sound()