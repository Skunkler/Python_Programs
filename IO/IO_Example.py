

#importing the two modules we'll need to run the program
import math
import os


#This function was designed to answer task 4, it takes two years that are inputed by the user and the filepath pointing to the csv file
def PopChange(Year1, Year2, filePath):
    #this if statement checks to make sure the user has entered a valid set of years
    if int(Year1)%5 == 0 and int(Year2)%5 == 0 and int(Year1) >= 1970 and int(Year1) <= 2010 and int(Year2) >= 1970 and int(Year2) <= 2010:

        #prompts the user as to where they want the output csv
        outputFile_dir = raw_input("Please enter an output directory for the csv containing the population change.\n ")
        #this variable points to the output csv file we are going to open and write to
        finalOutputFilePath = outputFile_dir + '\\' + 'CityPopChg.csv'

        #This opens up and reads the citypop csv and reads it and stores the contents in two separate variables
        citypop_file = open(filePath,"r")
        citypop_file2 = open(filePath,"r")

        #open up a new csv named CityPopChg.csv that will be our output file and set the mode to write
        Population_change_output = open(finalOutputFilePath, "w")

        #write the header information in the first line of this new output file
        Population_change_output.write('id'+','+'City'+','+'Population_change' +'\n')
    
        #create three empty lists that are to be used during the next few rounds of calculations
        baseline_list = []
        calc_list = []
        City_list = []

        #loop through the contents of the citypop_file variable
        for line in citypop_file:
            #create a list of lines by spliting the line by the comma
            line_reader = line.split(',')

            #igore the first line of the csv as it is just the header information
            if line_reader[0] != 'id':
                #if the user entered 1970 grab the 5th element of every line that is split by the comma, convert the string data type to a float
                #and add it to the baseline_list
                if Year1 == '1970':
                    baseline_list.append(float(line_reader[5]))

                #Same thing as before but only if the user enters 1975 as the baseline year, then grab the 6th element of every line, convert the string data type to a float
                #add it to the baseline_list
                elif Year1 == '1975':
                    baseline_list.append(float(line_reader[6]))

                #if the user entered 1980 as the baseline year, grab the 7th element of every line, convert it to the proper data type and add it to the baseline_list
                elif Year1 == '1980':
                    baseline_list.append(float(line_reader[7]))    

                #if the user entered 1985 as the baseline year, grab the 8th element of every line, convert it to the proper data type and add it to the baseline_list
                elif Year1 == '1985':
                    baseline_list.append(float(line_reader[8]))

                #if the user entered 1990 as the baseline year, grab the 9th element of every line, convert it to the proper data type and add it to the baseline_list
                elif Year1 == '1990':
                    baseline_list.append(float(line_reader[9]))

                #if the user entered 1995 as the baseline year, grab the 10th element of every line, convert it to the proper data type and add it to the baseline_list
                elif Year1 == '1995':
                    baseline_list.append(float(line_reader[10]))

                #if the user entered 2000 as the baseline year, grab the 11th element of every line, convert it to the proper data type and add it to the baseline_list
                elif Year1 == '2000':
                    baseline_list.append(float(line_reader[11]))

                #if the user entered 2005 as the baseline year, grab the 12th element of every line, convert it to the proper data type and add it to the baseline_list
                elif Year1 == '2005':
                    baseline_list.append(float(line_reader[12]))

                #if the user entered 2010 as the baseline year, grab the 13th element of every line, convert it to the proper data type and add it to the baseline_list
                elif Year1 == '2010':
                    baseline_list.append(float(line_reader[13]))

        #loop through the contents of citypop_file2 which is another version of the CityPop csv
        for line in citypop_file2:
            #split the lines by the comma thus creating each line into a list
            line_reader = line.split(',')
            #skip the first line of the file as it just contains the header information
            if line_reader[0] != 'id':
                #since second year needs to be greater than our baseline year we must start at a minimum of 1975
                #we also add the the name of every city from the 4th element of every line in the file here and add it to the City_list no matter which of the valid inputs the user gives
                #if the user entered 1975 as the second year, grab the 6th element of every line, convert it to the proper data type and add it to the calc_list
                
                if Year2 == '1975':
                    City_list.append(line_reader[4])
                    calc_list.append(float(line_reader[6]))

                #if the user entered 1980 as the second year, grab the 7th element of every line, convert it to the proper data type and add it to the calc_list
                elif Year2 == '1980':
                    City_list.append(line_reader[4])
                    calc_list.append(float(line_reader[7]))    

                #if the user entered 1985 as the second year, grab the 8th element of every line, convert it to the proper data type and add it to the calc_list
                elif Year2 == '1985':
                    City_list.append(line_reader[4])
                    calc_list.append(float(line_reader[8]))

                #if the user entered 1990 as the second year, grab the 9th element of every line, convert it to the proper data type and add it to the calc_list
                elif Year2 == '1990':
                    City_list.append(line_reader[4])
                    calc_list.append(float(line_reader[9]))

                #if the user entered 1995 as the second year, grab the 10th element of every line, convert it to the proper data type and add it to the calc_list
                elif Year2 == '1995':
                    City_list.append(line_reader[4])
                    calc_list.append(float(line_reader[10]))

                #if the user entered 2000 as the second year, grab the 11th element of every line, convert it to the proper data type and add it to the calc_list
                elif Year2 == '2000':
                    City_list.append(line_reader[4])
                    calc_list.append(float(line_reader[11]))

                #if the user entered 2005 as the second year, grab the 12th element of every line, convert it to the proper data type and add it to the calc_list
                elif Year2 == '2005':
                    City_list.append(line_reader[4])
                    calc_list.append(float(line_reader[12]))

                #if the user entered 2010 as the second year, grab the 13th element of every line, convert it to the proper data type and add it to the calc_list
                elif Year2 == '2010':
                    City_list.append(line_reader[4])
                    calc_list.append(float(line_reader[13]))


        #initialize a count variable and set it to 1
        count = 1
        #created a for loop based on the length of baseline_list as its length, the length of City_list, and the length of calc_list should all be the same
        for i in range(len(baseline_list)):
            #write the output with the count being the id, the name of the city, and the difference between the year in the future and the baseline year thus giving you
            #the population change, convert every data type that isn't a string to a string and add a new line character to write the new line with each iteration of the for loop
            Population_change_output.write(str(count) + ','+ City_list[i] + ',' + str(calc_list[i] - baseline_list[i]) + '\n')
            #after writing the line to the output increment the count variable
            count += 1

        #close the output file and our two variables containing the CityPop csv data
        Population_change_output.close()
        citypop_file.close()
        citypop_file2.close()
    #This print statement will be executed if the user did not enter a valid set of years
    else:
        print "Sorry please enter a valid set of years"
                
                
    
                
        
                
#This function is written to answer task 3 it takes two inputs from the user that must be two cities as well as the filepath
#pointing to the CityPop csv
def Dist_calc(input1, input2, filePath):

    #checks to make sure the cities input by the user exist in CityPop.csv
    city_list = []
    #open and read contents of CityPop.csv
    city_check_file = open(filePath, "r")
    #loop through the contents of CityPop.csv and add the names of each city to city_list
    for line in city_check_file:
        city = line.split(',')[4]
        city_list.append(city)

    #close the CityPop.csv file 
    city_check_file.close()

    #if both inputs provided by the user are in the CityPop.csv then procede with the program
    if input1 in city_list and input2 in city_list:
    

        #open up the CityPop csv file, read the contents and store them in the citypop_file variable
        citypop_file = open(filePath, "r")

        #open up the CityPop csv file again, read the contents and store them in the citypop_file2 variable
        citypop_file2 = open(filePath, "r")

        #create two empty lists that will be used to store the data and calculate the distance
        City1_coord = []
        City2_coord = []

        #loop through the lines of CityPop csv
        for line in citypop_file:

            #assign the name variable to the 4th element of the line that is split by the comma
            #assign the lat variable to the 1st element of the line and assign the lon variable to the 2nd element of the line
            name = line.split(',')[4]
            lat = line.split(',')[1]
            lon = line.split(',')[2]
            #if the first input provided by the user matches one of the city names in one of the lines
            #then append the name, lat, and lon variables that are associated with the line in the file that
            #match the user input to the City1_coord list
            if input1 == name:
                City1_coord.append(name)
                City1_coord.append(lat)
                City1_coord.append(lon)

        #loop through the lines of CityPop csv that were stored in the citypop_file2 variable
        for line2 in citypop_file2:
            #assign the name2 variable to the 4th element of the line that is split by the comma
            #assign the lat variable to the 1st element of the line and assign the lon variable to the 2nd element of the line 
            name2 = line2.split(',')[4]
            lat = line2.split(',')[1]
            lon = line2.split(',')[2]

            #if the second input provided by the user matches one of the city names in one of the lines
            #then append the name2, lat, and lon variables that are associated with the line in the file that
            #match the user input to the City2_coord list
            if input2 == name2:
                City2_coord.append(name2)
                City2_coord.append(lat)
                City2_coord.append(lon)

        #grab the longitude and latitude coordinates stored in each of the two lists, and convert them to a float data type
        #and then convert from degrees to radians
        #store the lon and lat coordinates for each of the cities in the corresponding lon and lat POI variables
        lat_POI1 = math.radians(float(City1_coord[1]))
        lat_POI2 = math.radians(float(City2_coord[1]))
        lon_POI1 = math.radians(float(City1_coord[2]))
        lon_POI2 = math.radians(float(City2_coord[2]))

        #great circle distance formula with our input put in
        d = math.acos(math.sin(lat_POI1) * math.sin(lat_POI2) + math.cos(lat_POI1) * math.cos(lat_POI2) * math.cos(lon_POI1 - lon_POI2))

        #assign our final answer in terms of kilometers
        answer = 6300 * d

        #print the message and answer to the user
        print 'the distance between ' + input1 + ' and ' + input2 + ' is ' + str(answer) + ' Kilometers.'

        #close citypop_file and citypop_file2
        citypop_file.close()
        citypop_file2.close()
    #if one or both of the inputs are not provided by the user then print this error message to the screen
    else:
        print "sorry but one or both of the cities you entered does not exist in the file, please try again"
        
        


            
                
                
#This function is written to answer task 2 it takes a city input from the user and a year and a path pointing to
# the CityPop csv        
def find_cityPop_Year(user_city, user_year, filePath):

    city_file_check = open(filePath, "r")
    city_list = []

    for line in city_file_check:
        city = line.split(',')[4]
        city_list.append(city)

    city_file_check.close()

    if user_city in city_list:
    
        #open up the contents of CityPop.csv and read the contents and store the content in citypop_file
        citypop_file = open(filePath, "r")

        #if the year prodivided by the user is valid then proceded
        if int(user_year)%5 == 0 and int(user_year) >= 1970 and int(user_year) <= 2010:

            #loop through the contents of the CityPop csv
            for line in (citypop_file):
                #split each line up by the comma and turn it into a list
                line_reader = line.split(',')

                #skip the first line as this is just the header information
                if line_reader[0] != 'id':
                    #assign the lat_coord variable to the 1st element in the line
                    lat_coord = line_reader[1]

                    #assign the lon_coord to the 2nd element of the line
                    lon_coord = line_reader[2]
                    #assign the city variable to the 4th element of the line
                    city = line_reader[4]
                    #assign the yr_1970 variable to the 5th element of the line
                    yr_1970 = line_reader[5]
                    #assign the yr_1975 variable to thee 6th element of the line
                    yr_1975 = line_reader[6]
                    #assign the yr_1980 variable to the 7th element of the line
                    yr_1980 = line_reader[7]
                    #assign the yr_1985 variable to the 8th element of the line
                    yr_1985 = line_reader[8]
                    #assign the yr_1990 variable to the 9th element of the line
                    yr_1990 = line_reader[9]
                    #assign the yr_1995 variable to the 10th element of the line
                    yr_1995 = line_reader[10]
                    #assign the yr_2000 variable to the 11th element of the line
                    yr_2000 = line_reader[11]
                    #assign the yr_2005 variable to the 12th element of the line
                    yr_2005 = line_reader[12]
                    #assign the yr_2010 variable to the 13th element of the line
                    yr_2010 = line_reader[13]

                    #if the input provided by the user equals the name of the city in the line and the year provided by the user is 1970 the print
                    #the following city name and the population data associated with the year and the city are printed out to the user on the screen
                    if user_city == city and user_year == '1970':
                        print "The population for city of " + city + " for the year 1970 is " + yr_1970

                    #if the input provided by the user equals the name of the city in the line and the year provided by the user is 1975 the print
                    #the following city name and the population data associated with the year and the city are printed out to the user on the screen
                    elif user_city == city and user_year == '1975':
                        print "The population for the city of " + city + " for the year 1975 is " + yr_1975

                    #if the input provided by the user equals the name of the city in the line and the year provided by the user is 1980 the print
                    #the following city name and the population data associated with the year and the city are printed out to the user on the screen
                    elif user_city == city and user_year == '1980':
                        print "The population for the city of " + city + " for the year 1980 is " + yr_1980

                    #if the input provided by the user equals the name of the city in the line and the year provided by the user is 1985 the print
                    #the following city name and the population data associated with the year and the city are printed out to the user on the screen
                    elif user_city == city and user_year == '1985':
                        print "The population for the city of " + city + " for the year 1985 is " + yr_1985

                    #if the input provided by the user equals the name of the city in the line and the year provided by the user is 1990 the print
                    #the following city name and the population data associated with the year and the city are printed out to the user on the screen
                    elif user_city == city and user_year == '1990':
                        print "The population for the city of " + city + " for the year 1990 is " + yr_1990

                    #if the input provided by the user equals the name of the city in the line and the year provided by the user is 1995 the print
                    #the following city name and the population data associated with the year and the city are printed out to the user on the screen
                    elif user_city == city and user_year == '1995':
                        print "The population for the city of " + city + " for the year 1995 is " + yr_1995

                    #if the input provided by the user equals the name of the city in the line and the year provided by the user is 2000 the print
                    #the following city name and the population data associated with the year and the city are printed out to the user on the screen
                    elif user_city == city and user_year == '2000':
                        print "The population for the city of " + city + " for the year 2000 is " + yr_2000

                    #if the input provided by the user equals the name of the city in the line and the year provided by the user is 2005 the print
                    #the following city name and the population data associated with the year and the city are printed out to the user on the screen
                    elif user_city == city and user_year == '2005':
                        print "The population for the city of " + city + " for the year 2005 is " + yr_2005

                    #if the input provided by the user equals the name of the city in the line and the year provided by the user is 2010 the print
                    #the following city name and the population data associated with the year and the city are printed out to the user on the screen
                    elif user_city == city and user_year == '2010':
                        print "The population for the city of " + city + " for the year 2010 is " + yr_2010
        #else if the user inputs a year that is not valid, print the following error message and close citypop_file    
        else:
            print "sorry the year you provided is not valid, please restart the program and try again."
        citypop_file.close()
    else:
        print "sorry but the city you entered is not in the file, please restart the program and try again."



#assign the filePath variable to the location of the CityPop.csv
filePath = r"C:\UW-Madison\Geog378\lab5\CityPop.csv"
#check to make sure it exists
if os.path.exists(filePath):
    

    #prompt the user as to what they would like to do with the data in CityPop.csv
    User_input = raw_input("to look up a city by year and population press (1), if you you would like to calculate the distance between two different cities press (2), else if you would like to calculate the population change between two different years press (3): ")
    
        #if the user enters 1 then prompt them for the necessary inputs for the find_cityPop_Year() function
    if User_input == '1':
        user_city = raw_input("Please enter the name of a city: ")
        user_year = raw_input("Please enter a year for the population: ")
    
        #call find_cityPop_Year with the inputs provided by the user and the path pointing to the CityPop.csv file
        find_cityPop_Year(user_city, user_year, filePath)
   
            
        #if the user enters 2 then prompt them for the necessary inputs to call the Dist_calc() function
    elif User_input == '2':
        user_City_input1 = raw_input("Please enter a city you would like to calculate a distance with: ")
        user_City_input2 = raw_input("Please enter another city:")
        
        #call the Distance function with the user inputs of city 1 and city 2 as well as the filepath pointing to the CityPop.csv
        Dist_calc(user_City_input1, user_City_input2, filePath)            

    #if the user enters 3 then prompt them for the necessary inputs to call the PopChange() function
    elif User_input == '3':
        user_year_1 = raw_input("please enter a baseline year: ")
        user_year_2 = raw_input("please enter another year to track population change between from the baseline year: ")

        #if the first input is greater than the second, reverse the order you would input the years to the function so that the calc_year is always greater than
        #the baseline year
        if int(user_year_1) > int(user_year_2): 
            PopChange(user_year_2, user_year_1, filePath)

        #if the first input is less than the second, input the order normally as the first input year is the baseline year
        elif int(user_year_1) < int(user_year_2):

            PopChange(user_year_1, user_year_2, filePath)

        #if the first and second years input by the user are the same, print the error message to the screen and prompt the user to try again
        elif int(user_year_1) == int(user_year_2):
            print "sorry please enter two different years and try again."
        #if the user doesn't enter a value that is either 1, 2, or 3 print the following error message
    else:
        print "sorry, " + User_input + " is not a valid answer. Please restart the program and try again."

#if the filepath pointing to the CityPop.csv doesn't exist print the following error message
else:
    print "sorry the file does not exist."
