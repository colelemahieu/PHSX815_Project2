# program to roll fair dice

# import external packages
from __future__ import print_function 
import sys
import numpy as np
from fractions import Fraction

# import our Random class
from Random import Random


# main function 
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)

    # default seed
    seed = 5555

    # default dice roll probabilities (fair dice)
    prob1 = Fraction(1,6)
    prob2 = Fraction(1,6)
    prob3 = Fraction(1,6)
    prob4 = Fraction(1,6)
    prob5 = Fraction(1,6)

    # default number of dice rolls (per experiment)
    Nroll = 1

    # default number of experiments
    Nexp = 1

    # get number of rolls and experiments from the command line
    if '-Nroll' in sys.argv:
        p = sys.argv.index('-Nroll')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            Nroll = Nt
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne

    # class instance of our Random class using seed
    random = Random(seed)

   # generate fair dice rolls
    for e in range(0,Nexp):
        for t in range(0,Nroll):
            print(random.DiceRoll(prob1,prob2,prob3,prob4,prob5), end=" ")
        print(" ")

