#Author: Shreya Panthee
#Date Modified:2025-02-21
#Description:

user_input = int(input("Choose an option to calculate the volume of (1: Cube, 2: Sphere, 3: Cone, 4: Cylinder)"))

match user_input:
    case 1:
        print("You chose to calculate the volume of a cube")
        length = int(input("Enter length of the cube and press Enter "))
        volume = length**3
        print("The volume of the cube is " + str(volume))
    
    case 2:
        print("You chose to calculate the volume of a sphere")
        radius = int(input("Enter the radius of the sphere and press Enter "))
        volume = 4/3 * 3.14 * radius
        print("The volume of the sphere is " + str(volume))

    case 3:
        print("You chose to calculate the volume of a cone")
        radius = int(input("Enter the radius of the base of the cone and press Enter "))
        height = int(input("Enter the height of the cone and press Enter "))
        volume = 1/3 * 3.14 * radius**2 * height
        print("The volume of the cone is " + str(volume))

    case 4:
        print("You chose to calculate the volume of a cylinder")
        radius = int(input("Enter the radius of the cylinder and press Enter "))
        height = int(input("Enter the height of the cylinder and press Enter "))
        volume = 3.14 * radius**2 * height

    case _:
        print("Invalid option, please try again.")