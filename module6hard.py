import math


class Figure:
    sides_count = 0

    def __init__(self, color: list, *sides: int):
        self.__color = [*color] if self.__is_valid_color(*color) else [0, 0, 0]
        self.__sides = [*sides] if len(sides) == self.sides_count else [1] * self.sides_count
        self.filled = False

    def __is_valid_color(self, r, g, b):
        if not all(isinstance(value, int) for value in (r, g, b)):
            return False
        if not all(0 <= value <= 255 for value in (r, g, b)):
            return False
        return True

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]

    def __is_valid_sides(self, *args):
        if all(isinstance(value, (int, float)) and value > 0 for value in args):
            if len(args) == self.sides_count:
                return True
        return False

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: list, circumference=1):
        super().__init__(color, circumference)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius**2

    def get_radius(self):
        return self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: list, *sides: int):
        super().__init__(color, *sides)
        a, b, c = self.get_sides()
        self.__p = (a + b + c) / 2
        self.__a, self.__b, self.__c = a, b, c

    def get_square(self):
        return math.sqrt(
            self.__p * (self.__p - self.__a) * (self.__p - self.__b) * (self.__p - self.__c)
        )


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: list, side=1):
        super().__init__(color, *[side] * self.sides_count)

    def get_volume(self):
        return self.get_sides()[0] **3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

triangle1 = Triangle((100, 150, 200), 3, 4, 5)
print(triangle1.get_square())

print(cube1.get_volume())
