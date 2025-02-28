#Author: Shreya Panthee
#Date Modified: 2025-02-28
#Description: Code that calculates the discriminant of a quadratic formula by reading the values of a, b and c from the user.

try:
    print ("Enter values of a, b and c from the standard form of a quadratic equation. y = an^2 + bn + c\n")
    #Taking user input for the value of a, b and c in the quadratic formula.
    a = float (input("Enter 'a' value then press Enter: "))
    b = float (input("Enter 'b' then press Enter: "))
    c = float (input("Enter 'c' then press Enter: "))

    if a==0:
        print("The value of 'a' can't be zero for a quadratic equation. Please try again.")
    else:
        #Calculating and printing the discriminant of the quadratic equation.
        Discriminant = b**2 - 4*a*c
        print("The Discriminant is: " + str(Discriminant))

        if Discriminant > 0:
            print("The equation has 2 x-intercepts/roots")
        elif Discriminant == 0:
            print("The equation has 1 x-intercept/root")
        else:
            print("The equation has no x-intercepts/roots")

except ValueError:
    print("Invalid input, please try again.")