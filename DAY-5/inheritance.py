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

class trunk(audi):
    def __init__(self, windows, doors, enginetype, horsepower, capacity):
        super().__init__(windows, doors, enginetype, horsepower)
        self.capacity = capacity
    def display_info(self):
        print("trunk is used to carry goods")

my_trunk = trunk(2, 2, "V8", 500, "2000kg")
my_trunk.display_info()

my_car = audi(4, 4, "V6", 300)
my_car.display_info()

print(my_car.horsepower)









# class methods and class variables
class car:
    base_price = 100000
    def __init__(self, windows, doors, power):
        self.windows = windows
        self.doors = doors
        self.power = power
    def what_base_price(self):
        print(f"Base price of car is {car.base_price}")

    @classmethod
    def update_base_price(cls, new_price):
        cls.base_price = new_price * cls.base_price
        print(f"Base price updated to {cls.base_price}")
my_car = car(4, 4, "150hp")
my_car.what_base_price()
car.update_base_price(1.2)
my_car.what_base_price()




