#Author: Shreya Panthee
#Date Modified: 2025-02-22
#Description: Code that calculates the discriminant of a quadratic formula by reading the values of a, b and c from the user.

#Taking user input for the value of a, b and c in the quadratic formula.
a = int (input("Enter a then press Enter "))
b = int (input("Enter b then press Enter "))
c = int (input("Enter c then press Enter "))

#Calculating and printing the discriminant of the quadratic equation.
Discriminant = b**2 - 4*a*c
print("The Discriminant is " + str(Discriminant))
