class car:
    name = ""
    cylinder = 0
    model = 1900
    price = 234
    color =""
    def __init__(self, name, model, sylinder, price, color):
        print("new car")
        self.name = name
        self.model = model
        self.sylinder = sylinder
        self.price = price
        self.color = color
car_1 = car("mercedes", "2002", 4 , 12000, "red")
car_2 = car("mersedes", "2023" , 8 , 35000, "red")
print(car_1.color,car_2.name)