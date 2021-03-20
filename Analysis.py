# this file calculates log likelihood ratios and performs analysis

# import packages
import sys
import numpy as np
import matplotlib.pyplot as plt
from math import *
from fractions import Fraction
from Random import Random

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

#print(cp1)
#print(cp2)
#print(cp3)
#print(cp4)
#print(cp5)
#print(cp6)

# initialize LLR distribution arays
LLR0 = []
LLR1 = []

# loop over rolls for each experiment to find LLR
for i in range(0, nexp0):
    LogLikeRatio_0 = float(0)
    for j in range(0, rolls_0):
        
        # the various prob. for H0
        if sum0arr[i][j]==1:
            LogLikeRatio_0 -=log(Fraction(1,6))
        elif sum0arr[i][j]==2:
            LogLikeRatio_0 -=log(Fraction(1,6))
        elif sum0arr[i][j]==3:
            LogLikeRatio_0 -=log(Fraction(1,6))
        elif sum0arr[i][j]==4:
            LogLikeRatio_0 -=log(Fraction(1,6))
        elif sum0arr[i][j]==5:
            LogLikeRatio_0 -=log(Fraction(1,6))
        else:
            LogLikeRatio_0 -=log(Fraction(1,6))

        # the various prob. for H1
        if sum0arr[i][j]==1:
            LogLikeRatio_0 +=log(cp1)
        elif sum0arr[i][j]==2:
            LogLikeRatio_0 +=log(cp2)
        elif sum0arr[i][j]==3:
            LogLikeRatio_0 +=log(cp3)
        elif sum0arr[i][j]==4:
            LogLikeRatio_0 +=log(cp4)
        elif sum0arr[i][j]==5:
            LogLikeRatio_0 +=log(cp5)
        else:
            LogLikeRatio_0 +=log(cp6)

    LLR0.append(LogLikeRatio_0)

for i in range(0, nexp1):
    LogLikeRatio_1 = float(0)
    for j in range(0, rolls_1):
        
        # the various prob. for H0
        if sum1arr[i][j]==1:
            LogLikeRatio_1 -=log(Fraction(1,6))
        elif sum1arr[i][j]==2:
            LogLikeRatio_1 -=log(Fraction(1,6))
        elif sum1arr[i][j]==3:
            LogLikeRatio_1 -=log(Fraction(1,6))
        elif sum1arr[i][j]==4:
            LogLikeRatio_1 -=log(Fraction(1,6))
        elif sum1arr[i][j]==5:
            LogLikeRatio_1 -=log(Fraction(1,6))
        else:
            LogLikeRatio_1 -=log(Fraction(1,6))

        # the various prob. for H1
        if sum1arr[i][j]==1:
            LogLikeRatio_1 +=log(cp1)
        elif sum1arr[i][j]==2:
            LogLikeRatio_1 +=log(cp2)
        elif sum1arr[i][j]==3:
            LogLikeRatio_1 +=log(cp3)
        elif sum1arr[i][j]==4:
            LogLikeRatio_1 +=log(cp4)
        elif sum1arr[i][j]==5:
            LogLikeRatio_1 +=log(cp5)
        else:
            LogLikeRatio_1 +=log(cp6)

    LLR1.append(LogLikeRatio_1)

# sort the arrays
LLR0.sort()
LLR1.sort()

# enter desired alpha value
alpha = 0.1
lambda_c = len(LLR0)-int(floor((len(LLR0))*alpha))

# find beta
count = float(0)
for x in range(0,len(LLR1)):
    if LLR1[x] < LLR0[lambda_c]:
        count += 1

beta = count/len(LLR1)

# plotting code
plt.figure()
plt.hist(LLR0, bins=60, alpha=0.75, label="$\\mathbb{H}_{0}$")
plt.hist(LLR1, bins=60, alpha=0.75, label="$\\mathbb{H}_{1}$")

# get axis limits
left, right = plt.xlim()
bottom, top = plt.ylim()

plt.xlabel('$x = \\log({\\cal L}_{\\mathbb{H}_{1}}/{\\cal L}_{\\mathbb{H}_{0}})$')
plt.ylabel("Frequency")
plt.title("Log Likelihood Ratio (%i rolls per exp, %i exp)" %(rolls_0, nexp0))
plt.legend(loc="upper left",shadow=True)

plt.axvline(LLR0[lambda_c], color="k", linestyle="solid", linewidth=1.25)
plt.text(LLR0[lambda_c]-1, .95*top, "$\\lambda_{c}$", rotation=90)
plt.text(left+.2,.75*top, "$\\alpha$ = %.2f" %(alpha), fontweight="bold")
plt.text(left+.2,.70*top, "$\\beta$ = %.4f" %(beta), fontweight="bold")

# exponential distribution for Gaussian standard deviation
random = Random()
exp_arr = []
for i in range(0, 10000):
    exp_arr.append(random.Exponential(10))
plt.figure()
plt.hist(exp_arr, bins=100)
plt.xlabel("Exponential Distribution")
plt.ylabel("Frequency")
plt.title("Posterior Distr. to Sample $\\sigma$");

# posterior Gaussian distribution for this particular project
norm_arr = []
for i in range(0, 10000):
    norm_arr.append(random.box_muller(sigma=0.071890315957))
plt.figure()
plt.hist(norm_arr, bins=100)
plt.xlabel("Gaussian Distribution")
plt.ylabel("Frequency")
plt.title("Posterior Distr. to Sample Roll Probability")

# plot comparing roll outcomes between H0 and H1
plt.figure()
plt.hist(sum0, bins=6, alpha=0.65, density=True, label="$\\mathbb{H}_{0}$")
plt.hist(sum1, bins=6, alpha=0.65, density=True, label="$\\mathbb{H}_{0}$")
plt.xlabel("Rolled Number")
plt.ylabel("Probability")
plt.title("Rolled Number Distributions of 2 Dice")
plt.legend()

plt.show()

