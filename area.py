import math
def area(i):
    if i == 'circle':
        r = float(input('Input the radius:'))
        return math.pi*r*r
    elif i == 'square':
        a = float(input('Enter the side of square:'))
        return a*a
    elif i == 'rectangle':
        l = float(input('Enter length:'))
        b = float(input('Enter breadth:'))
        return l*b
    elif i == 'triangle':
        a = input('Please enter "y" if the type of triangle is equilateral or "n" for others:')
        if a == 'y':
            b = float(input('Please enter the side:'))
            return math.sqrt(3)/4*b*b
        else:
            b = float(input('Enter the base of the triangle:'))
            h = float(input('Enter the perpendicular of the triangle:'))
            return b*h/2
    elif i == 'parallelogram':
        b = float(input('Enter the base of the parallelogram:'))
        h = float(input('Enter the perpendicular of the parallelogram:'))
        return b*h
    elif i == 'trapezium':
        b1 = float(input('Enter the base of the trapezium:'))
        b2 = float(input('Enter the parallel side of the trapezium:'))
        h = float(input('Enter the height of the trapezium:'))
        return h*(b1+b2)/2
