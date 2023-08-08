class Home:
    def room1(self):
        width = 100
        breadth = 100
        print('area of room1', width * breadth)
    def kitchen(self):
        width = 1222
        breadth = 4888
        print('area of kitchen', width * breadth)

class FirstHome(Home):
    def __init__(self):
        self.home = "First Home"
    def study_room(self):
        width = 120
        breadth = 120
        print('area of study room in first home ', width * breadth)

class SecondHome(Home):
    def __init__(self):
        self.home = "Second Home"
    def work_area(self):
        width = 100
        breadth = 100
        print('area of work area in second home ', width * breadth)

fh = FirstHome()
sh = SecondHome()

print(fh.home)
fh.room1()
fh.kitchen()
fh.study_room()

print(sh.home)
sh.room1()
sh.kitchen()
sh.work_area()
