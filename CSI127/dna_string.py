#Name:  Sara D'Alessandro
#Date: September 23, 2018
#This program prompts the user for a DNA string, and then prints the length and GC-content.

dna = input("Enter a DNA string: ")

l = len(dna)
print("The length is", l)

numC = dna.count('C')
numG = dna.count('G')

gc = (numC + numG) / l
print('GC-content is', gc)
