#Write a Python program that calculates the area of a circle based on the radius entered by the user.

import math

r=float(input("Please input a radius: "))

print("{:.2f}".format(math.pi * (r**2)))

print(math.pi * (r**2))