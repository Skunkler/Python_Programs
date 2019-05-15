# This program calculates the area of a triangle or trapazoid and gives the user 3 chances to enter a valid value for each input.

# This part of the code prints the message "This program finds the area of a triangle"
print "This program finds the area of a triangle or trapazoid based on user input."
print 	


#This loopCount variable is set to 0 and is used to increment with the while loop
loopCount = 0
#While the count variable is less than 4 we increment the loopCount variable by 1
while loopCount<4:
    loopCount += 1
    #Then we try the following codeblock

    try:
        #prompt the user for geometry type to be calculated
        Geometry_type = input("Do you wish to calculate a trapazoid(1) or a triangle(2)? Please enter 1 or 2: ")

        #If 1 is selected the user is prompted for the input values to calculate the area of the trapazoid
        if Geometry_type == 1:
            height = input("Please enter the height of the trapozoid: ")
            side1 = input("Please enter one of the sides of the trapazoid: ")
            side2 = input("Please enter the other side of the trapazoid: ")

            #We store the resulting calculation for the area of the trapazoid in a variable called area 
            area = (0.5*(side1 + side2)) * height
            #print out a message to the user showing them the results
            print "The area of a trapazoide with base1 of ", side1, " and a base2 of ", side2, " and a height of ", height, "is ", area, "."

        #If 2 is selected the user is prompted to input the values for calculating the area of a triangle
        elif Geometry_type == 2:
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

    #With this except statement we catch any bad user input and go to the top of the loop where we increment
    # The loopCount variable by 1 and prompt the user again for inputs just 2 more times
    # if the user fails to input a valid value the program with end without crashing
    except:
        print "\nyou entered a value that is not valid! Please try again"
