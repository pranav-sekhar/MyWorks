class Parent:
    def __init__(self,name,color):
        self.n=name
        self.c=color
    def one(self):
        print(self.n,self.c)
class Child(Parent):
    def __init__(self,name,color,model):
        super().__init__(name,color)
        self.m=model
    def two(self):
        self.one()
        print(self.m)
obj=Child("BMW","BLUE",2025)
obj.two()
