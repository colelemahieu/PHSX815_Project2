# import packages
import sys
import numpy as np
import matplotlib.pyplot as plt
from math import *

from Random import Random

# instantiate our Random class
random = Random()

# generate the probabilities for rolling numbers 1-6 using a normal distribution
# This code guarantees the probabilities add up to 1
p1 = random.box_muller()
while (p1>1):
    p1 = random.box_muller()
    
p2 = random.box_muller()
while ((p1+p2)>1):
    p2 = random.box_muller()

p3 = random.box_muller()
while ((p1+p2+p3)>1):
    p3 = random.box_muller()

p4 = random.box_muller()
while ((p1+p2+p3+p4)>1):
    p4 = random.box_muller()

p5 = random.box_muller()
while ((p1+p2+p3+p4+p5)>1):
    p5 = random.box_muller()

p6 = 1-(p1+p2+p3+p4+p5)

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p1+p2+p3+p4+p5+p6)

