#Name: Sara D'Alessandro
#Date: October 17, 2017
#Program: Asks the user for a list of nouns and approximates the fraction that are plural by counting the fraction that end in "s".

a = input("Enter nouns: ")

words = a.count(' ') + 1

print("Number of words: ", words)

plural = a.count('s ')

if a[-1] == 's':
    plural = plural + 1

print("The fraction of your words that are plural is: ", float(plural/words))
