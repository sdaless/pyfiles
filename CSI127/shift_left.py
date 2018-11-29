#Name:  Sara D'Alessandro
#Date: September 12, 2018
#This program prompts the user to enter a word and then prints the word with each letter shifted left by 1. 

word = input("Enter a lowercase word: ")
codedWord = ""
for ch in word:
    offset = ord(ch) - ord('a') - 1 
    wrap = offset % 26  
    newChar = chr(ord('a') + wrap)  
    codedWord = codedWord + newChar 
    
print("Your word in code is: ", codedWord)
    


