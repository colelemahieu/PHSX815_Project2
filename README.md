# PHSX815_Project2

## *Instructions*

#### Step 1

Generate fair and unfair dice rolls using "DiceRollFair.py" and "DiceRoll.py" respectively. For both files, number of rolls and number of experiments can be specified from the command line using "-Nroll " and "-Nexp ".

For example: "python DiceRoll.py -Nroll 10 -Nexp 12".

Please pipe these results to .txt files.

#### Step 2

Pass the fair and unfair text files to Analysis.py, where "-input0 " specifies the fair file and "input1 " specifies the unfair file.

For example: "python Analysis.py -input0 fair.txt -input1 unfair.txt"

#### Optional

The parameters of the posterior distributions can always be altered by changing what rate feeds into the "random.Exponential()" method or what mean feeds into the "random.box_muller()" method.