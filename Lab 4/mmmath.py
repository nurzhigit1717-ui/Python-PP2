import math

# Exercise 1
degree = float(input("Input degree: "))
radian = math.radians(degree)
print("Output radian:", radian)

print()

# Exercise 2
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = (base1 + base2) * height / 2
print("Area of trapezoid:", area)

print()

# Exercise 3
n = int(input("Input number of sides: "))
side = float(input("Input the length of a side: "))

polygon_area = (n * side ** 2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", polygon_area)

print()

# Exercise 4
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

parallelogram_area = base * height
print("Area of parallelogram:", parallelogram_area)