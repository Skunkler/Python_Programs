# This program calculates the area of a triangle or a trapazoid based on user input 

# This part of the code prints the message "This program finds the area of a triangle"
print "This program finds the area of a triangle or trapazoid."
print 	

#This prompts the user if they wish to calculate a trapazoid or a triangle by entering in the values 1 or 2
Geometry_type = input("Do you wish to calculate a trapazoid(1) or a triangle(2)? Please enter 1 or 2: ")

#Here our if statement checks to see if the 1 was entered and if so prompt the user for the height and two side values
#to calculate the trapazoid
if Geometry_type == 1:
    height = input("Please enter the height of the trapozoid: ")
    side1 = input("Please enter one of the sides of the trapazoid: ")
    side2 = input("Please enter the other side of the trapazoid: ")

    #I assigned area to be equal to the equation that gives us the area of a trapazoid
    area = (0.5*(side1 + side2)) * height
    print "The area of a trapazoide with base1 of ", side1, " and a base2 of ", side2, " and a height of ", height, "and the area is ", area, ""."

#This elif statement checks to see if 2 was selected and if so the codeblock used to calculate the area of a triangle is executed
elif Geometry_type == 2:
    # Here we assign the height and the base variables equal to the user input
    # when the script is run the user will be prompted to enter in values that are
    # used to calculate the area of a triangle
    height = input("Please enter the height of the triangle: ")
    base = input("Please enter the base length of the triangle: ")

    # Here we assign the area variable to one half the base times the height
    # The height and base variables are assigned by the user in the previous commands
    area = 0.5 * height * base

    # This last bit prints out the message displaying the height and base and the calculated area
    # in a message
    print "The area of a triangle with height", height, "and base", base, "is", area, "."
