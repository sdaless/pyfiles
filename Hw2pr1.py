# Name: 
# Hw2pr1.py
# STRING slicing and indexing challenges

h = "harvey"
m = "mudd"
c = "college"

# Problem 1: hey

answer1 = h[0] + h[4:6]
print(answer1,"\n")


# Problem 2: collude

answer2 = c[0:4] + m[1:3] + c[-1]
print(answer2,"\n")

# Problem 3: arveyudd

answer3 = h[1:] + m[1:]
print(answer3,"\n")

# Problem 4: hardeharharhar

answer4 = h[:3] + m[-1] + c[-1] + (h[:3]*3)
print(answer4,"\n")

# Problem 5: legomyego

answer5 = c[3:6] + c[1] + m[0] + h[-1] + c[4:6] + c[1]
print(answer5,"\n")

# Problem 6: clearcall

answer6 = c[0] + c[3:5] + h[1:3] + c[0] + h[1] + c[2:4]
print(answer6,"\n")


# LIST slicing and indexing challenges
#   

pi = [3,1,4,1,5,9]
e = [2,7,1]

# Example problem (problem 0): [2,7,5,9]
answer0 = e[0:2] + pi[-2:]
print(answer0,"\n")

# Problem 7: creating [7,1]
answer7 = e[1:]
print(answer7,"\n")

# Problem 8: creating [9,1,1]
answer8 = pi[-1:-6:-2]
print(answer8,"\n")

# Problem 9: creating [1,4,1,5,9]
answer9 = pi[1:]
print(answer9,"\n")

# Problem 10: creating: [1,2,3,4,5]
answer10 = e[-1:-4:-2] + pi[0:5:2]
print(answer10)