

# This program calculates the area of a triangle.

# This part of the code prints the message "This program finds the area of a triangle"
print "This program finds the area of a triangle."
print 	

# Here we assign the height and the base variables equal to the user input
# when the script is run the user will be prompted to enter in values that are
# stored in each variable
height = input("Please enter the height of the triangle: ")
base = input("Please enter the base length of the triangle: ")

# Here we assign the area variable to one half the base times the height
#The height and base variables are assigned by the user in the previous commands
area = 0.5 * height * base

# This last bit prints out the message displaying the height and base and the calculated area
# in a message
print "The area of a triangle with height", height, "and base", base, "is", area, "."
