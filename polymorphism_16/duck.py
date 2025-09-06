#without inheritance then it is called ducktyping
class duck:
    def quack(self):
        print("sound like quack")
class person:
    def quack(self):
        print("he can also sound like duck")
def makesound(sound):
    sound.quack()
makesound(duck())
makesound(person())
