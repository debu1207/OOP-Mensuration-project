from shapes2D import *
from shapes3D import *


def area_perimeter_menu():
    msg = """
		 =================================
		||  1. Area                      ||
		||  2. Perimeter/circumference   ||
		 =================================

		 (b) Back                   (q) Quit

	"""
    print(msg)


def surfaceArea_volume_menu():
    msg = """
		 ======================
		||  1. Surface area   ||
		||  2. Volume         ||
		 ======================

		 (b) Back                   (q) Quit

	"""
    print(msg)


def shapes_menu_3D():
    menu = """
		 ================= 3D SHAPES ===============
		||                                         ||
		||  1. Cube    2. Cuboid    3. Cylinder    ||
		||                                         ||
		||  4. Cone    5. Sphere    6. Hemisphere  ||
		||                                         ||
		 ===========================================

		 (b) Back                              (q) Quit
	"""

    print(menu)


def shapes_menu_2D():
    menu = """
		 ================= 2D SHAPES ==================
		||                                            ||
		||  1. Square    2. Rectangle      3. Circle  ||
		||                                            ||
		||  4. Triangle  5. Parallelogram  6. Ellipse ||
		||                                            ||
		||  7. Trapezoid                              ||
		||                                            ||
		 ==============================================

		 (b) Back                              (q) Quit
	"""

    print(menu)


def shape3D_operations(res):
    if res == '1':
        cube = Cube()
        surfaceArea_volume_menu()
        resp = input("enter your choice: ")
        if resp == '1':
            print(f'\n Surface area of cube: {cube.surfaceArea()}')
        elif resp == '2':
            print(f'\n Volume of cube: {cube.volume()}')
        elif resp == 'b':
            choose_2Dshape()
        elif resp == 'q':
            exit()
        else:
            print(f'\nPlease enter a valid choice!!')

    elif res == '2':
        cuboid = Cuboid()
        surfaceArea_volume_menu()
        resp = input("enter your choice: ")
        if resp == '1':
            print(f'\n Surface area of cuboid: {cuboid.surfaceArea()}')
        elif resp == '2':
            print(f'\n Volume of cuboid: {cuboid.volume()}')
        elif resp == 'b':
            choose_2Dshape()
        elif resp == 'q':
            exit()
        else:
            print(f'\nPlease enter a valid choice!!')

    elif res == '3':
        cy = Cylinder()
        surfaceArea_volume_menu()
        resp = input("enter your choice: ")
        if resp == '1':
            print(f'\n Surface area of cylinder: {cy.surfaceArea()}')
        elif resp == '2':
            print(f'\n Volume of cylinder: {cy.volume()}')
        elif resp == 'b':
            choose_2Dshape()
        elif resp == 'q':
            exit()
        else:
            print(f'\nPlease enter a valid choice!!')

    elif res == '5':
        sphere = Sphere()
        surfaceArea_volume_menu()
        resp = input("enter your choice: ")
        if resp == '1':
            print(f'\n Surface area of sphere: {sphere.surfaceArea()}')
        elif resp == '2':
            print(f'\n Volume of sphere: {sphere.volume()}')
        elif resp == 'b':
            choose_2Dshape()
        elif resp == 'q':
            exit()
        else:
            print(f'\nPlease enter a valid choice!!')

    elif res == '4':
        cone = Cone()
        surfaceArea_volume_menu()
        resp = input("enter your choice: ")
        if resp == '1':
            print(f'\n Surface area of cone: {cone.surfaceArea()}')
        elif resp == '2':
            print(f'\n Volume of cone: {cone.volume()}')
        elif resp == 'b':
            choose_2Dshape()
        elif resp == 'q':
            exit()
        else:
            print(f'\nPlease enter a valid choice!!')

    elif res == '6':
        hemisphere = Hemisphere()
        surfaceArea_volume_menu()
        resp = input("Enter your choice: ")
        if resp == '1':
            print(f'\n Surface area of hemisphere: {hemisphere.surfaceArea()}')
        elif resp == '2':
            print(f'\n Volume of hemisphere: {hemisphere.volume()}')
        elif resp == 'b':
            choose_2Dshape()
        elif resp == 'q':
            exit()
        else:
            print(f'\nPlease enter a valid choice!!')


def shape2D_operation(res):
    if res == '1':
        square = Square()
        area_perimeter_menu()
        resp = input("enter your choice: ")
        if resp == '1':
            print(f'\n Area of square: {square.area()}')
        elif resp == '2':
            print(f'\n Perimeter of square: {square.perimeter()}')
        elif resp == 'b':
            choose_2Dshape()
        elif resp == 'q':
            exit()
        else:
            print(f'\nPlease enter a valid choice!!')

    elif res == '2':
        rect = Rectangle()
        area_perimeter_menu()
        resp = input("enter your choice: ")
        if resp == '1':
            print(f'\n Area of rectangle: {rect.area()}')
        elif resp == '2':
            print(f'\n Perimeter of rectangle: {rect.perimeter()}')
        elif resp == 'b':
            choose_2Dshape()
        elif resp == 'q':
            exit()
        else:
            print(f'\nPlease enter a valid choice!!')

    elif res == '3':
        circle = Circle()
        area_perimeter_menu()
        resp = input("enter your choice: ")
        if resp == '1':
            print(f'\n Area of rectangle: {circle.area()}')
        elif resp == '2':
            print(f'\n Perimeter of rectangle: {circle.circumference()}')
        elif resp == 'b':
            choose_2Dshape()
        elif resp == 'q':
            exit()
        else:
            print(f'\nPlease enter a valid choice!!')

    elif res == '4':
        triangle = Triangle()
        area_perimeter_menu()
        resp = input("enter your choice: ")
        if resp == '1':
            print(f'\n Area of rectangle: {triangle.area()}')
        elif resp == '2':
            print(f'Enter the traingle sides for perimeter: ')
            sides = [float(i) for i in input().split()]
            print(f'\n Perimeter of rectangle: {triangle.perimeter(sides[0], sides[1], sides[2])}')
        elif resp == 'b':
            choose_2Dshape()
        elif resp == 'q':
            exit()
        else:
            print(f'\nPlease enter a valid choice!!')

    elif res == '5':
        para = Parallelogram()
        area_perimeter_menu()
        resp = input("enter your choice: ")
        if resp == '1':
            print(f'\n Area of rectangle: {para.area()}')
        elif resp == '2':
            print(f'\n Perimeter of rectangle: {para.perimeter()}')
        elif resp == 'b':
            choose_2Dshape()
        elif resp == 'q':
            exit()
        else:
            print(f'\nPlease enter a valid choice!!')

    elif res == '6':
        eli = Ellipse()
        area_perimeter_menu()
        resp = input("enter your choice: ")
        if resp == '1':
            print(f'\n Area of rectangle: {eli.area()}')
        elif resp == '2':
            print(f'\n Perimeter of rectangle: {eli.perimeter()}')
        elif resp == 'b':
            choose_2Dshape()
        elif resp == 'q':
            exit()
        else:
            print(f'\nPlease enter a valid choice!!')

    elif res == '7':
        trapz = Trapezoid()
        area_perimeter_menu()
        resp = input("enter your choice: ")
        if resp == '1':
            print(f'\n Area of rectangle: {trapz.area()}')
        elif resp == '2':
            print(f'\n Perimeter of rectangle: {trapz.perimeter()}')
        elif resp == 'b':
            choose_2Dshape()
        elif resp == 'q':
            exit()
        else:
            print(f'\nPlease enter a valid choice!!')


def choose_3Dshape():
    while True:
        shapes_menu_3D()
        res = input("\n Choose option: ")
        if res == 'b':
            main()
        if res == 'q':
            quit()
        shape3D_operations(res)


def choose_2Dshape():
    while True:
        shapes_menu_2D()
        res = input("\n   Choose option: ")
        if res == 'b':
            main()
        if res == 'q':
            exit()
        shape2D_operation(res)


Menu_message = """
    	====== Welcome to shapes Menu ======

       1. 2D SHAPES   2. 3D SHAPES   3. EXIT
               """


def main():
    while True:
        print(Menu_message)
        response = input("\nEnter you choice: ")

        if response == "1":
            choose_2Dshape()
        elif response == "2":
            choose_3Dshape()
        elif response == "3":
            exit()

if __name__ == '__main__':
    main()