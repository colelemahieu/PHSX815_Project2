# this file calculates log likelihood ratios and performs analysis

# import packages
import sys
import numpy as np
import matplotlib.pyplot as plt
from math import *
from fractions import Fraction

# define the file inputs
p0 = sys.argv.index("-input0")
p1 = sys.argv.index("-input1")

# inititalize number of experiments
nexp0 = 0
nexp1 = 0

# count the number of experiments, file0
with open(sys.argv[p0+1], "r") as file0:
    for line in file0:
        nexp0 +=1

# get the file data, file0
with open(sys.argv[p0+1], "r") as file0:
    file0string = file0.read()
    file0list = file0string.split(" ")

# count the number of experiments, file1
with open(sys.argv[p1+1], "r") as file1:
    for line in file1:
        nexp1 += 1

# get the file data, file1
with open(sys.argv[p1+1], "r") as file1:
    file1string = file1.read()
    file1list = file1string.split(" ")

# get rid of the \n symbols
file0list_b = []
for x in file0list:
    file0list_b.append(x.strip())

file1list_b = []
for x in file1list:
    file1list_b.append(x.strip())

# delete empty spaces in the list
file0list_clean = [x for x in file0list_b if x]
file1list_clean = [x for x in file1list_b if x]

# calculate number of rolls per experiment
rolls_0 = len(file0list_clean)/nexp0
rolls_1 = len(file1list_clean)/nexp1

# get arrays of float dice rolls
sum0 = []
sum1 = []
for i in range(0, len(file0list_clean)):
    sum0.append(float(file0list_clean[i]))
for i in range(0, len(file1list_clean)):
    sum1.append(float(file1list_clean[i]))

# make an array divided into subarrays for each experiment
array0 = np.array(sum0)
array1 = np.array(sum1)
sum0arr = np.reshape(array0, (-1, rolls_0))
sum1arr = np.reshape(array1, (-1, rolls_1))

# we sample our distribution to integrate over it
# (count how many times each number appears to calculate probability)
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0
for i in range(0, len(sum0)):
    if sum1[i] == 1:
        ones += 1
    elif sum1[i] == 2:
        twos += 1
    elif sum1[i] == 3:
        threes += 1
    elif sum1[i] == 4:
        fours += 1
    elif sum1[i] == 5:
        fives += 1
    else:
        sixes += 1
        
# calculate the probability from our sampele
cp1 = float(ones) / len(sum1)
cp2 = float(twos)/len(sum1)
cp3 = float(threes)/len(sum1)
cp4 = float(fours)/len(sum1)
cp5 = float(fives)/len(sum1)
cp6 = float(sixes)/len(sum1)
print(cp1)
print(cp2)
print(cp3)
print(cp4)
print(cp5)
print(cp6)
print(cp1+cp2+cp3+cp4+cp5+cp6)

# initialize LLR distribution arays
LLR0 = []
LLR1 = []
