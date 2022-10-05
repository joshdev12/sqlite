# class Car:
    
#     def __init__(self, name, brand):
#         self.name = name
#         self.brand = brand

#     def start(self, name):
#         print(f"{name} start... Boooom!")
    

# car1 = Car("Toyota", "Camry")
# car1.no_of_door = 2

# car2 = Car("Mazda", "Something")
# car2.no_of_door = 4

# print(car1.name)
# print(car2.name)

# car1.start(car1.name)
# car2.start(car2.name)

# print(type(car1))

import turtle

class Polygon:

    name = "Sdfs"
    
    def __init__(self, name, side, length, pensize=2):
        self.pensize = pensize
        self.name = name
        self.side = side
        self.length = length
        self.interior_angles = (self.side - 2) * 180
        self.angle = self.interior_angles / self.side

    def __str__(self):
        return f"{self.name} has {self.side} sides"

    def __len__(self):
        return self.side

    

    def draw(self):
        turtle.pensize(self.pensize)
        for i in range(self.side):
            turtle.forward(self.length)
            turtle.left(180 - self.angle)

        turtle.done()


triangle = Polygon("Triangle", 3, 100)
square = Polygon("Square", 4, 100)

# print(square.side)
# triangle.draw()

print(triangle)
print(square)
print(len(triangle))
        