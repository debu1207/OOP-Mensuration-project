# 2D shapes

import math

class Cube:
    def __init__(self):
        self.edge = 0
        self.enter_data()

    def enter_data(self):
        self.edge = float(input("Enter the edge: "))

    def surfaceArea(self):
        return float(6 * self.edge * self.edge)

    def volume(self):
        return float(self.edge ** 3)


class Cuboid:
    def __init__(self):
        self.length = 0
        self.width = 0
        self.height = 0
        self.enter_data()

    def enter_data(self):
        self.length = float(input("Enter the length: "))
        self.width = float(input("Enter the width: "))
        self.height = float(input("Enter the height: "))

    def surfaceArea(self):
        return float(2 * (self.width * self.length + self.height * self.length + self.height * self.width))

    def volume(self):
        return self.width * self.height * self.length


class Cylinder:
    def __init__(self):
        self.radius = 0
        self.height = 0
        self.enter_data()

    def enter_data(self):
        self.radius = float(input("Enter the cylinder radius: "))
        self.height = float(input("Enter height: "))

    def surfaceArea(self):
        return 2 * math.pi * (self.radius + self.height)

    def volume(self):
        return math.pi * self.radius * self.radius * self.height


class Cone:
    def __init__(self):
        self.radius = 0
        self.slant = 0
        self.height = 0
        self.enter_data()

    def enter_data(self):
        self.radius = float(input("Enter Cone radius: "))
        self.slant = float(input("Enter Cone slant height: "))
        self.height = math.sqrt(pow(self.slant, 2) - pow(self.radius, 2))

    def surfaceArea(self):
        return math.pi * self.radius * (self.radius + self.slant)

    def volume(self):
        return (1 / 3) * math.pi * (self.radius ** 2) * self.height


class Sphere:
    def __init__(self):
        self.radius = 0
        self.enter_data()

    def enter_data(self):
        self.radius = float(input("Enter radius: "))

    def surfaceArea(self):
        return 4 * math.pi * self.radius * self.radius

    def volume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)


class Hemisphere:
    def __init__(self):
        self.radius = 0
        self.enter_data()

    def enter_data(self):
        self.radius = float(input("Enter radius: "))

    def surfaceArea(self):
        return 3 * math.pi * self.radius * self.radius

    def volume(self):
        return (2 / 3) * math.pi * (self.radius ** 3)
