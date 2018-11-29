#CSci 127 Teaching Staff
#November 2018
#A template for a program that computes Copenhagen transit fares.
#Modified by: Sara D'Alessandro

def computeFare(zone, ticketType):
     """
     Takes as two parameters: the zone and the ticket type.
     Returns the MetroNorth Railroad fare.
     If the zone is 1 and the ticket type is "peak", the fare is 6.75.
     If the zone is 1 and the ticket type is "off-peak", the fare is 5.00.
     If the zone is 1 and the ticket type is "senior", the fare is 3.25.
     
     If the zone is 2 and the ticket type is "peak", the fare is 7.50.
     If the zone is 2 and the ticket type is "off-peak", the fare is 5.75.
     If the zone is 2 and the ticket type is "senior", the fare is 3.75.
     
     If the zone is 3 and the ticket type is "peak", the fare is 9.25.
     If the zone is 3 and the ticket type is "off-peak", the fare is 7.00.
     If the zone is 3 and the ticket type is "senior", the fare is 4.50.
     
     If the zone is greater than 3, return a negative number (since your calculator does not handle inputs that high).
     """
     
     fare = 0
     
     if zone == 1 and ticketType == "peak":
         print(fare + 6.75)
         
     elif zone == 1 and ticketType == "off-peak":
         print(fare + 5.00)

     elif zone == 1 and ticketType == "senior":
         print(fare + 3.25)

     elif zone == 2 and ticketType == "peak":
         print(fare + 7.50)
         
     elif zone == 2 and ticketType == "off-peak":
         print(fare + 5.75)

     elif zone == 2 and ticketType == "senior":
         print(fare + 3.75)

     elif zone == 3 and ticketType == "peak":
         print(fare + 9.25)
                    
     elif zone == 3 and ticketType == "off-peak":
         print(fare + 7.00)
                         
     elif zone == 3 and ticketType == "senior":
         print(fare + 4.50)

     else:
         print(fare == -1)

     return(fare)

def main():
     z = int(input('Enter the number of zones: '))
     t = input('Enter the ticket type (peak/off-peak/senior): ').lower()
     fare = computeFare(z,t)
     print('The fare is', fare)

#Allow script to be run directly:
if __name__ == "__main__":
     main()
