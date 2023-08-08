class Brototype:
    def __init__ (self,name,age,place):   
        self.name=name
        self.age=age
        self.place=place
    def add_age(self):
        self.age=self.age+1
    def relocate(self,place):
        self.place=place
    def display(self):
        print("name : " +self.name)

   

 


x=Brototype("hari",19,"kochi")
y=Brototype("Faizal",26,"calicut")

x.display()
y.display()
