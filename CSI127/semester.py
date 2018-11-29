#Sara D'Alessandro
#A program that calculates the number of days left in the semester into weeks.
#October 9th, 2018

days = int(input("Enter the number of days left in the semester: "))

weeks = days // 7
leftover = days % 7

print("There are", weeks, "weeks and", leftover, "days left in the semester.")
