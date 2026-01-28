class car:
    def __init__(self, windows, doors, enginetype):
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype
    def display_info(self):
        print("car is used for driving")

class audi(car):
    def __init__(self, windows, doors, enginetype, horsepower):
        super().__init__(windows, doors, enginetype)
        self.horsepower = horsepower
    def display_info(self):
        print("audi is a luxury car brand")

my_car = audi(4, 4, "V6", 300)
my_car.display_info()
            
print(my_car.horsepower)