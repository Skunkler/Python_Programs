#create a latlon_count and set it to 0
latlon_count = 0

#While the latlon_count is less than 4 run the program
while latlon_count <4:

    #increment latlon_count by 1
    latlon_count += 1

    #program the user for to input values for longitude and latitude
    longitude = raw_input("Please enter a value for longitude: ")

    latitude = raw_input("Please enter a value for latitude: ")

    #Try the following code block after the longitude and latitude    
    try:
        #create a long and lat variable and set it to the user inputs casted as a int data type
        Long = int(longitude)
        lat = int(latitude)


        #if the lat variable is equal to 0 notify the user that the location is on the equator
        if lat == 0:
            print "That location is on the equator."

        #lat variable is greater than 0 and less than 90 notify the user the location is north of the equator    
        elif lat >= 0 and lat <= 90:
            print "That location is north of the equator."

        #if the lat is greater than -90 but less than 0 notify the user the location is south of the equator    
        elif lat >= -90 and lat <= 0:
            print "That location is south of the equator."

        #if the lat is greater than 90 or less than -90 then notify the user the location does not have a valid latitude    
        elif lat >= 90 or lat <= -90:
            print "That location does not have a valid latitude!"
            
        #if Long equals 0 then notify the user the location is on the prime meridian
        if Long == 0:
            print "That location is on the prime meridian."

        #if the long variable is greater than 0 and less than 180 notify the user the location is east of the prime meridian    
        elif Long >= 0 and Long <= 180:
            print "That location is east of the prime meridian."

        #if the long variable is greater than -180 and less than 0 notify the user the location is west of the prime meridian
        elif Long >= -180 and Long <= 0:
            print "That location is west of the prime meridian."

        #if the long variable is greater than 180 or less than -180 notify the user that that longitude value is not valid
        elif Long > 180 or Long < -180:
            print "That location does not have a valid longitude!"

    #This except statement catches bad user input and if there is bad user input we go back to the top of the loop and prompt the
    #user again for inputs. The user has a total of three chances to input a value before the program will end without crashing.
    except:
        print "Please enter a valid numeric type."

