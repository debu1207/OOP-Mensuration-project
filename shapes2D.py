# All shapes
import math


class Square:
	def __init__(self):
		self.side = 0
		self.enter_data()

	def area(self):
		return float(self.side * self.side) 

	def perimeter(self):
		return float(4 * self.side)

	def enter_data(self):
		self.side = float(input("Enter side of square: "))



class Rectangle:
	def __init__(self):
		self.width = 0
		self.height = 0
		self.enter_data()

	def enter_data(self):
		self.width = float(input("\nEnter width: "))
		self.height = float(input("\nEnter height: "))

	def area(self):
		return float(self.width * self.height)

	def perimeter(self):
		return float(2 * (self.width + self.height))



class Circle:
	def __init__(self):
		self.radius = 0
		self.enter_data()

	def enter_data(self):
		self.radius = float(input("\nEnter circle radius: "))


	def area(self):
		return  math.pi * self.radius * self.radius

	def circumference(self):
		return 2 * math.pi * self.radius

	def sector_area(self, angle):
		return (angle/360) * self.area()


class Triangle:
	def __init__(self):
		self.base = 0
		self.height = 0
		self.enter_data()

	def enter_data(self):
		self.base = float(input("\nEnter base: "))
		self.height = float(input("\nEnter height: "))

	def area(self):
		return float(0.5 * self.base * self.height)

	def perimeter(self, a, b, c):
		return a + b + c


class Parallelogram:
	def __init__(self):
		self.base = 0
		self.height = 0
		self.side = 0
		self.enter_data()
	def enter_data(self):
		self.base = float(input("Enter base: "))
		self.height = float(input("Enter height: "))
		self.side = float(input("Enter side: "))

	def area(self):
		return float(self.base * self.height)


	def perimeter(self):
		return float(2 * (self.base + self.side))


class Ellipse:
	def __init__(self):
		self.a = 0
		self.b = 0
		self.enter_data()

	def enter_data(self):
		self.a = float(input("Enter x-axis a: "))
		self.b = float(input("Enter y-axis b: "))

	def area(self):
		return math.pi * self.a * self.b 

	def perimeter(self):
		print(f'Not defined')
		return



class Trapezoid:
	def __init__(self):
		self.a = 0
		self.b = 0
		self.height = 0
		self.enter_data()

	def enter_data(self):
		self.a = float(input("Enter side a: "))
		self.b = float(input("Enter side b: "))
		self.height = float(input("Enter height: "))

	def area(self):
		return self.height * (self.a + self.b) * 0.5

	def perimeter(self):
		pass