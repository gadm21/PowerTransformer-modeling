

from math import cos ,tan , pi, sqrt 
import numpy as np

def deg2rad(deg) : return (deg*pi) / 180 

r=  0.5 
x = r 
z = sqrt(x**2 + r**2) 
print(cos(deg2rad(r/z)))
print(r/z)