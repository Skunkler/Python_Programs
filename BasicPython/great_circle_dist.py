

#Import the math module in order to run the calculation for the distance
import math

#Set up a count variable and set a while loop that increments the count variable 3 times and try to catch for bad user input
calc_dist_count = 0

while calc_dist_count < 4:

    calc_dist_count += 1

    #Prompt the user to enter the latitude and longitude coordinates for two different locations
    Lat1_coordinate = raw_input("Please enter latitude coordinate of first point: ")
    Lat2_coordinate = raw_input("Please enter latitude coordinate of second point: ")
    Lon1_coordinate = raw_input("Please enter longitude coordinate of first point: ")
    Lon2_coordinate = raw_input("Please enter longitude coordinate of second point: ")

    
    #Try to execute the following code block    
    try:
        #Set the lat1, lat2, lon1, lon2 variables equal to the corresponding user inputs and cast them as a float data type
        lat1 = float(Lat1_coordinate)
        lat2 = float(Lat2_coordinate)
        Lon1 = float(Lon1_coordinate)
        Lon2 = float(Lon2_coordinate)

        #convert the lat1, lat2, lon1, lon2 variables from degrees to radians using math.radians()
        #store the results in new variables lat1_rad, lat2_rad, lon1_rad, lon2_rad
        lat1_rad = math.radians(lat1)
        lat2_rad = math.radians(lat2)
        lon1_rad = math.radians(Lon1)
        lon2_rad = math.radians(Lon2)

        #set the variable d equal to the equation that gives us distance. We calculate acos using math.acos() and we calculate sin and cos using math.sin() and math.cos()
        #We use the values entered by the user after they were converted to radians
        d = math.acos(math.sin(lat1_rad) * math.sin(lat2_rad) + math.cos(lat1_rad)*math.cos(lat2_rad)*math.cos(lon1_rad-lon2_rad))

        #we store the final answer in a variable called answer that takes our calculation from the last part and multiply it by 6300 in order to convert it to km
        answer = 6300 * d

        #display the distance between the two points to the user
        print answer

    #This except statement catches bad user input and prompts the user to try again in entering a lat lon values for the two locations
    #The user has three attempts before the program ends without crashing
    except:
        "please enter valid numeric type"
