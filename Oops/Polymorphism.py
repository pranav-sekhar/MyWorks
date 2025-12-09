class Animal:
    def sound(self):
        print("animal")
class Dog(Animal):
    def sound(self):
        print("dog")
class Cat(Animal):
    def sound(self):
        print("cat")
def new(food):
    food.sound()
o1=Dog()
o2=Cat()
new(o1)
new(o2)
