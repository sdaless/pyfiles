#Sara D'Alessandro
#A program that blanks
#October 2nd, 2018

s = input("Enter a string: ")

ls = len(s)

for i in range(ls):
    print('*' * i)
    
for i in range(ls, 0, -1):
    print( '*' * i)

print("So long and goodnight.")
