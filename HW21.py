class Auto:
    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1


my_car = Auto(brand="Mazda", age=30, mark="626", color="Red", weight=1240)

print(f"Brand: {my_car.brand}")
print(f"Age: {my_car.age}")
print(f"Mark: {my_car.mark}")
print(f"Color: {my_car.color}")
print(f"Weight: {my_car.weight}")

my_car.move()

my_car.stop()

my_car.birthday()

print(f"New Age after birthday: {my_car.age}")
