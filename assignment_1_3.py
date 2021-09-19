'''
Write a Python program to find the volume of a sphere with diameter 12 cm.
'''
import math
def volume_sphere(radius):
    pi = math.pi
    r = radius * radius * radius
    return (4 * pi * r) / 3

diameter = 12
radius = diameter / 2
vol = volume_sphere(radius)

print("volume of sphere is ",vol)