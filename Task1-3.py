# 3) Add 4 different subclasses for class Shape. Triangle, Square, Pentagon, Circle.
# Define constructor for each of them to assign the necessary parameters required for calculating the area.
# Define the area method for each of the classes. When invoked it Should return the area of the shape by calculating it Create an object for each of the subclasses and call the area method on the objects.


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

class Pentagon(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return 1.25 * self.side**2 / (4 * 0.7265)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius**2

triangle = Triangle(base=8, height=6)
print(f"Area of the Triangle: {triangle.area()}")

square = Square(side=6)
print(f"Area of the Square: {square.area()}")

pentagon = Pentagon(side=4)
print(f"Area of the Pentagon: {pentagon.area()}")

circle = Circle(radius=5)
print(f"Area of the Circle: {circle.area()}")
