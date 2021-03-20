# program to roll a die with probabilites sampled from a normal distribution

# import packages
from __future__ import print_function
import sys
import numpy as np
import matplotlib.pyplot as plt
from math import *

from Random import Random

# instantiate our Random class
random = Random()

# generate a width from an exponential distribution for our probability gaussian
sigma_exp = random.Exponential(10)
while (sigma_exp>1):
    sigma_exp = random.Exponential(10)

# generate the probabilities for rolling numbers 1-6 using a normal distribution
# This code guarantees the probabilities add up to 1
p1 = random.box_muller(sigma=sigma_exp)
while (p1>1 and p1<0):
    p1 = random.box_muller(sigma=sigma_exp)
    
p2 = random.box_muller(sigma=sigma_exp)
while ((p1+p2)>1 and p2<0):
    p2 = random.box_muller(sigma=sigma_exp)

p3 = random.box_muller(sigma=sigma_exp)
while ((p1+p2+p3)>1 and p3<0):
    p3 = random.box_muller(sigma=sigma_exp)

p4 = random.box_muller(sigma=sigma_exp)
while ((p1+p2+p3+p4)>1 and p4<0):
    p4 = random.box_muller(sigma=sigma_exp)

p5 = random.box_muller(sigma_exp)
while ((p1+p2+p3+p4+p5)>1 and p5<0):
    p5 = random.box_muller(sigma_exp)

p6 = 1-(p1+p2+p3+p4+p5)


# default number od dice rolls (per experiment)
Nroll = 1

# default number of experiments
Nexp = 1

# read user-provided arguments from command line 
if "-Nroll" in sys.argv:
    p = sys.argv.index("-Nroll")
    Nt = int(sys.argv[p+1])
    if Nt > 0:
        Nroll = Nt
if "-Nexp" in sys.argv:
    p = sys.argv.index("-Nexp")
    Ne = int(sys.argv[p+1])
    if Ne > 0:
        Nexp = Ne

# output rolls
for e in range(0,Nexp):
            for t in range(0,Nroll):
                print(random.DiceRoll(p1,p2,p3,p4,p5), end=" ")
            print(" ")

#print(p1)
#print(p2)
#print(p3)
#print(p4)
#print(p5)
#print(p6)
#print(p1+p2+p3+p4+p5+p6)
