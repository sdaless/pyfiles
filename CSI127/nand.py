#Name: Sara D'Alessandro
#Date: 16 October 2017
#Program: Computes NAND of two inputs, using only AND, OR, and NOT gates

#nand gate: both off, light on.  either off, light on.  both on, light off.

out = (in1 not in2) or (in1 or in2) not (in1 and in2)
