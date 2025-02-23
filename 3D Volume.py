#Author: Shreya Panthee
#Date Modified:2025-02-23
#Description: Code that calculates the volume of a cube, sphere, cone, or cylinder based on user input and takes the required parameters to calculate the volume from the user.

def safe_int_input(prompt):
    """Prompt the user until a valid integer is entered."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Prompt the user for the volume calculation option
user_input = safe_int_input("Choose an option to calculate the volume of (1: Cube, 2: Sphere, 3: Cone, 4: Cylinder) ")

match user_input:
    case 1:#Case to calculate the volume of a cube
        
        print("You chose to calculate the volume of a cube")
        
        #Taking user input for length of the cube
        length = safe_int_input("Enter length of the cube and press Enter: ")
        
        #Calculating the volume of the cube and printing it
        volume = length**3
        print("The volume of the cube is: " + str(volume))
    
    case 2:#Case to calculate the volume of a sphere
        
        print("You chose to calculate the volume of a sphere")
        
        #Taking user input for the radius of the sphere
        radius = safe_int_input("Enter the radius of the sphere and press Enter: ")
        
        #Calculating and printing the volume of the sphere
        volume = 4/3 * 3.14 * radius
        print("The volume of the sphere is: " + str(volume))

    case 3:#Case to calculate volume of a sphere
        
        print("You chose to calculate the volume of a cone")
        
        #Taking user input for the radius and height of the cone 
        radius = safe_int_input("Enter the radius of the base of the cone and press Enter: ")
        height = safe_int_input("Enter the height of the cone and press Enter: ")
        
        #Calculating and printing the volume of the cone
        volume = 1/3 * 3.1416 * radius**2 * height
        print("The volume of the cone is: " + str(volume))

    case 4:#Case to calculate the volume of a cylinder
        
        print("You chose to calculate the volume of a cylinder")
        
        #Taking user input for radius and height of cylinder
        radius = safe_int_input("Enter the radius of the cylinder and press Enter: ")
        height = safe_int_input("Enter the height of the cylinder and press Enter: ")
        
        #Calculating and printing the volume of the cylinder
        volume = 3.1416 * radius**2 * height
        print("The volume of the cylinder is: " + str(volume))

    case _:
        print("Invalid option, please try again.")